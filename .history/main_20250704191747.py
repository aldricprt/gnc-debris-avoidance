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

    # --- Détection de débris prédictive (moins sévère) ---
    debris_states = [
        {'pos': [415], 'vel': [-0.005]},  # Débris descendant plus lentement
        {'pos': [395], 'vel': [0.005]},   # Débris montant plus lentement
    ]
    detector = DebrisDetector(debris_states=debris_states, detection_radius=2.0)  # Rayon plus petit
    debris_events = []  # Pour logguer les alertes prédictives

    # Simulation
    estimated_positions = []
    estimated_velocities = []
    distances_to_debris = [[] for _ in debris_states]
    for i, z in enumerate(noisy_measurements):
        est = tracker.update(z)
        est_vel = tracker.kf.x[1]
        estimated_positions.append(est)
        estimated_velocities.append(est_vel)
        for idx, debris in enumerate(debris_states):
            dist = abs(est - debris['pos'][0])
            distances_to_debris[idx].append(dist)
        # Détection prédictive moins sévère (horizon plus court, rayon plus petit)
        alerts = detector.detect_predictive([est], [est_vel], horizon=30, dt=1.0)
        for idx, dmin, tmin in alerts:
            debris_events.append((time_steps[i], est, idx, dmin, tmin))
            print(f"Alerte collision prédictive (débris #{idx}) à t={time_steps[i]:.0f}s : distance min={dmin:.2f} km dans {tmin:.1f}s")

    # Visualisation simple
    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, true_positions, 'g-', linewidth=2, label='True trajectory')
    plt.plot(time_steps, noisy_measurements, 'r.', markersize=4, alpha=0.5, label='Noisy measurements')
    plt.plot(time_steps, estimated_positions, 'b-', label='Kalman estimation')
    # Trajectoire des débris (avec vitesse)
    for idx, debris in enumerate(debris_states):
        debris_traj = [debris['pos'][0] + debris['vel'][0]*t for t in time_steps]
        plt.plot(time_steps, debris_traj, '--', linewidth=1.5, label=f'Trajectoire débris #{idx}')
    # Affichage des alertes prédictives
    if debris_events:
        t_debris, alt_debris, idx_debris, dmin_debris, tmin_debris = zip(*debris_events)
        plt.scatter(t_debris, alt_debris, c='orange', marker='x', s=80, label='Alerte collision prédictive')
    plt.title("Kalman filtering + predictive debris detection for a CubeSat in LEO", fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Altitude (km)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('experiments/debris-detection-experiments/figures/trajectory_predictive.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Nouveau graphique : évolution des distances à chaque débris
    plt.figure(figsize=(12, 5))
    for idx, dists in enumerate(distances_to_debris):
        plt.plot(time_steps, dists, label=f'Distance au débris #{idx}')
    plt.axhline(detector.detection_radius, color='red', linestyle='--', label='Rayon de détection')
    plt.title("Distance entre le satellite et chaque débris au cours du temps", fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Distance (km)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('experiments/debris-detection-experiments/figures/debris_distances.png', dpi=300, bbox_inches='tight')
    plt.show()

    # --- Log d'expérience ---
    with open('experiments/debris-detection-experiments/debris_detection_log.md', 'a') as log:
        log.write(f"\n\n## Résultat du {np.datetime64('now')}\n")
        log.write(f"Débris simulés aux positions : {debris_states} (rayon {detector.detection_radius} km)\n")
        log.write(f"Nombre de nouvelles alertes de collision : {len(debris_events)}\n")
        for t, alt, idx, dmin, tmin in debris_events:
            log.write(f"- Alerte débris #{idx} à t={t:.0f}s, altitude estimée={alt:.1f} km, distance min={dmin:.2f} km dans {tmin:.1f}s\n")
        log.write(f"Débris détectés au final (indices) : {detector.get_detected()}\n")