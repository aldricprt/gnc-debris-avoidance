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
    
    # Vitesse réelle très faible (variation d'altitude ~10 km sur 600 s)
    # v = delta_altitude / delta_temps ≈ 20 km / 600 s ≈ 0.033 km/s
    realistic_velocity = (np.max(true_positions) - np.min(true_positions)) / duration

    # Définition des scénarios de paramètres
    scenarios = [
        {
            'name': 'Smooth (high R, low Q)',
            'color': 'b',
            'params': dict(P=np.diag([10.0, 0.1]), R=100.0, Q=np.array([[0.01, 0], [0, 0.001]]), initial_pos=true_positions[0], initial_vel=realistic_velocity)
        },
        {
            'name': 'Reactive (low R, high Q)',
            'color': 'm',
            'params': dict(P=np.diag([10.0, 0.1]), R=1.0, Q=np.array([[1.0, 0], [0, 0.1]]), initial_pos=true_positions[0], initial_vel=realistic_velocity)
        },
        {
            'name': 'Bad init (wrong pos, high P)',
            'color': 'c',
            'params': dict(P=np.diag([1000.0, 10.0]), R=25.0, Q=np.array([[0.1, 0], [0, 0.01]]), initial_pos=350.0, initial_vel=realistic_velocity)
        },
        {
            'name': 'Rigid model (very low Q)',
            'color': 'orange',
            'params': dict(P=np.diag([10.0, 0.1]), R=25.0, Q=np.array([[0.0001, 0], [0, 0.0001]]), initial_pos=true_positions[0], initial_vel=realistic_velocity)
        },
        {
            'name': 'Noisy sensor (very high R)',
            'color': 'k',
            'params': dict(P=np.diag([10.0, 0.1]), R=400.0, Q=np.array([[0.1, 0], [0, 0.01]]), initial_pos=true_positions[0], initial_vel=realistic_velocity)
        },
        {
            'name': 'Precise sensor (very low R)',
            'color': 'g',
            'params': dict(P=np.diag([10.0, 0.1]), R=1.0, Q=np.array([[0.1, 0], [0, 0.01]]), initial_pos=true_positions[0], initial_vel=realistic_velocity)
        }
    ]

    plt.figure(figsize=(14, 7))
    plt.plot(time_steps, true_positions, 'k-', linewidth=2, label='True trajectory')
    plt.plot(time_steps, noisy_measurements, 'r.', markersize=3, alpha=0.3, label='Noisy measurements')

    for scenario in scenarios:
        tracker = SatelliteTracker(initial_pos=scenario['params']['initial_pos'], initial_vel=scenario['params']['initial_vel'], dt=dt)
        tracker.kf.P = scenario['params']['P']
        tracker.kf.R = scenario['params']['R']
        tracker.kf.Q = scenario['params']['Q']
        est = []
        for z in noisy_measurements:
            est.append(tracker.update(z))
        plt.plot(time_steps, est, color=scenario['color'], label=scenario['name'])

    plt.title("Kalman filter scenarios: effect of parameters", fontsize=15)
    plt.xlabel("Time (s)", fontsize=12)
    plt.ylabel("Altitude (km)", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('images/kalman_scenarios.png', dpi=300, bbox_inches='tight')
    plt.show()