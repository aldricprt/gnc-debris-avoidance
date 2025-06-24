from src.gnc.kalman_filter import SatelliteTracker
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
    tracker = SatelliteTracker(initial_pos=true_positions[0], dt=dt)
    
    # Simulation
    estimated_positions = []
    for z in noisy_measurements:
        tracker.update(z)
        estimated_positions.append(tracker.kf.x[0])
    
    # Visualisation pro
    plt.figure(figsize=(12, 6))
    plt.plot(time_steps, true_positions, 'g-', linewidth=2, label='Trajectoire réelle')
    plt.plot(time_steps, noisy_measurements, 'r.', markersize=4, alpha=0.5, label='Mesures bruitées')
    plt.plot(time_steps, estimated_positions, 'b-', label='Estimation Kalman')
    
    plt.title("Filtrage de Kalman pour un CubeSat en LEO", fontsize=14)
    plt.xlabel("Temps (s)", fontsize=12)
    plt.ylabel("Altitude (km)", fontsize=12)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('images/trajectory.png', dpi=300, bbox_inches='tight')
    plt.show()