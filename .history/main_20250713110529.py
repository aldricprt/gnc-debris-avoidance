from src.gnc.kalman_filter import SatelliteTracker
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Paramètres simulation
    altitude = 400  # km
    duration = 600  # s
    dt = 1.0
    time_steps = np.arange(0, duration, dt)
    true_positions = altitude + 10 * np.sin(0.01 * time_steps)
    noisy_measurements = true_positions + np.random.normal(0, 5, len(time_steps))
    realistic_velocity = (np.max(true_positions) - np.min(true_positions)) / duration
    tracker = SatelliteTracker(initial_pos=true_positions[0], initial_vel=realistic_velocity, dt=dt)

    # Débris : position et vitesse
    debris_states = [
        {'pos': [415], 'vel': [-0.005]},
        {'pos': [395], 'vel': [0.005]},
    ]
    detection_radius = 1.0  # km (seuil typique pour l'alerte collision dans le spatial)

    # Simulation Kalman
    estimated_positions = []
    for z in noisy_measurements:
        est = tracker.update(z)
        estimated_positions.append(est)

    # Détection réelle (balayage)
    real_collisions = []
    for idx, debris in enumerate(debris_states):
        debris_traj = [debris['pos'][0] + debris['vel'][0]*t for t in time_steps]
        min_dist = float('inf')
        t_collision = None
        alt_collision = None
        for t_idx, (sat, deb) in enumerate(zip(estimated_positions, debris_traj)):
            dist = abs(sat - deb)
            if dist < detection_radius:
                real_collisions.append((time_steps[t_idx], sat, idx, deb, dist))
                print(f"Collision réelle détectée avec débris #{idx} à t={time_steps[t_idx]:.0f}s : "
                      f"altitude satellite={sat:.2f} km, altitude débris={deb:.2f} km, distance={dist:.3f} km")
                break
            if dist < min_dist:
                min_dist = dist
                t_collision = time_steps[t_idx]
                alt_collision = sat
        else:
            print(f"Pas de collision réelle avec débris #{idx}. Distance minimale atteinte : {min_dist:.3f} km à t={t_collision:.0f}s.")

    # Visualisation
    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, true_positions, 'g-', linewidth=2, label='True trajectory')
    plt.plot(time_steps, noisy_measurements, 'r.', markersize=4, alpha=0.5, label='Noisy measurements')
    plt.plot(time_steps, estimated_positions, 'b-', label='Kalman estimation')
    for idx, debris in enumerate(debris_states):
        debris_traj = [debris['pos'][0] + debris['vel'][0]*t for t in time_steps]
        plt.plot(time_steps, debris_traj, '--', linewidth=1.5, label=f'Trajectoire débris #{idx}')
    if real_collisions:
        t_real, alt_real, idx_real, deb_real, dist_real = zip(*real_collisions)
        plt.scatter(t_real, alt_real, c='lime', marker='P', s=120, label='Collision réelle (Kalman)')
    plt.title("Détection de collision réelle (balayage trajectoire Kalman)", fontsize=14)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Altitude (km)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('experiments/debris-detection-experiments/figures/trajectory_collision_reelle.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Log lisible
    print("\nRésumé des collisions :")
    if real_collisions:
        for t, sat, idx, deb, dist in real_collisions:
            print(f"- Collision avec débris #{idx} à t={t:.0f}s : sat={sat:.2f} km, debris={deb:.2f} km, dist={dist:.3f} km")
    else:
        print("Aucune collision détectée sur la trajectoire Kalman.")