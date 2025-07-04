from src.gnc.kalman_filter import SatelliteTracker
from src.gnc.debris_detector import DebrisDetector
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Paramètres réalistes (orbite LEO ~400km)
    altitude = 400  # km
    duration = 600  # secondes (10min)
    dt = 1.0  # intervalle temps
    
    # Trajectoire réaliste (incluant une perturbation)
    time_steps = np.arange(0, duration, dt)
    true_positions = altitude + 10 * np.sin(0.01 * time_steps)  # oscillation réaliste
    
    # Bruit capteur réaliste (±5km)
    noisy_measurements = true_positions + np.random.normal(0, 5, len(time_steps))
    
    # Initialisation
    realistic_velocity = (np.max(true_positions) - np.min(true_positions)) / duration
    tracker = SatelliteTracker(initial_pos=true_positions[0], initial_vel=realistic_velocity, dt=dt)

    # --- Détection de débris ---
    # Exemple : 2 débris à des positions fixes (en 1D pour l'instant)
    debris_positions = [[410], [390]]  # km
    detector = DebrisDetector(debris_positions=debris_positions, detection_radius=5.0)
    debris_events = []  # Pour logguer les détections (nouveaux uniquement)

    # Simulation
    estimated_positions = []
    distances_to_debris = [[] for _ in debris_positions]  # Historique des distances à chaque débris
    for i, z in enumerate(noisy_measurements):
        est = tracker.update(z)
        estimated_positions.append(est)
        # Calcul de la distance à chaque débris
        for idx, debris in enumerate(debris_positions):
            dist = abs(est - debris[0])
            distances_to_debris[idx].append(dist)
        # Détection de nouveaux débris à chaque pas de temps
        new_detected = detector.detect([est])
        for idx in new_detected:
            debris_events.append((time_steps[i], est, idx))
            print(f"Nouveau débris détecté (#{idx}) à t={time_steps[i]:.0f}s, altitude satellite={est:.1f} km, altitude débris={debris_positions[idx][0]:.1f} km, distance={abs(est-debris_positions[idx][0]):.2f} km")

    # Visualisation simple
    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, true_positions, 'g-', linewidth=2, label='True trajectory')
    plt.plot(time_steps, noisy_measurements, 'r.', markersize=4, alpha=0.5, label='Noisy measurements')
    plt.plot(time_steps, estimated_positions, 'b-', label='Kalman estimation')
    # Affichage des distances à chaque débris
    for idx, dists in enumerate(distances_to_debris):
        plt.plot(time_steps, dists, '--', label=f'Distance au débris #{idx}')
    # Affichage des premières détections de chaque débris
    if debris_events:
        t_debris, alt_debris, idx_debris = zip(*debris_events)
        plt.scatter(t_debris, alt_debris, c='black', marker='x', s=80, label='Nouveau débris détecté')
    plt.title("Kalman filtering + debris detection for a CubeSat in LEO", fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Altitude (km) / Distance (km)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('images/trajectory.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --- Log d'expérience ---
    with open('experiments/debris_detector_log.md', 'a') as log:
        log.write(f"\n\n## Résultat du {np.datetime64('now')}\n")
        log.write(f"Débris simulés aux positions : {debris_positions} (rayon {detector.detection_radius} km)\n")
        log.write(f"Nombre de nouveaux débris détectés : {len(debris_events)}\n")
        for t, alt, idx in debris_events:
            log.write(f"- Nouveau débris #{idx} détecté à t={t:.0f}s, altitude estimée={alt:.1f} km\n")
        log.write(f"Débris détectés au final (indices) : {detector.get_detected()}\n")