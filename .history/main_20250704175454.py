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
    debris_positions = [[450], [390]]  # km
    detector = DebrisDetector(debris_positions=debris_positions, detection_radius=5.0)
    debris_events = []  # Pour logguer les détections

    # Simulation
    estimated_positions = []
    for i, z in enumerate(noisy_measurements):
        est = tracker.update(z)
        estimated_positions.append(est)
        # Détection de débris à chaque pas de temps
        # On suppose que le satellite est sur l'axe x (1D)
        if detector.detect([est]):
            debris_events.append((time_steps[i], est))
            print(f"Débris détecté à t={time_steps[i]:.0f}s, altitude estimée={est:.1f} km")

    # Visualisation simple
    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, true_positions, 'g-', linewidth=2, label='True trajectory')
    plt.plot(time_steps, noisy_measurements, 'r.', markersize=4, alpha=0.5, label='Noisy measurements')
    plt.plot(time_steps, estimated_positions, 'b-', label='Kalman estimation')
    # Affichage des détections de débris
    if debris_events:
        t_debris, alt_debris = zip(*debris_events)
        plt.scatter(t_debris, alt_debris, c='black', marker='x', s=80, label='Débris détecté')
    plt.title("Kalman filtering + debris detection for a CubeSat in LEO", fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Altitude (km)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('images/trajectory.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --- Log d'expérience ---
    with open('experiments/debris_detector_log.md', 'a') as log:
        log.write(f"\n\n## Résultat du {np.datetime64('now')}\n")
        log.write(f"Débris simulés aux positions : {debris_positions} (rayon {detector.detection_radius} km)\n")
        log.write(f"Nombre de détections : {len(debris_events)}\n")
        for t, alt in debris_events:
            log.write(f"- Débris détecté à t={t:.0f}s, altitude estimée={alt:.1f} km\n")