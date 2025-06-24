from src.gnc.kalman_filter import SatelliteTracker
from src.gnc.debrus_detector import DebrisDetector
from src.gnc.controller import GNController
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Simulation d'une trajectoire réelle (mouvement linéaire) + bruit
    true_positions = np.linspace(0, 10, 50)
    noisy_measurements = true_positions + np.random.normal(0, 1, 50)
    tracker = SatelliteTracker()
    detector = DebrisDetector()
    controller = GNController(tracker, detector)

    # Simulation
    positions = [tracker.update(z) for z in noisy_measurements]
    plt.plot(true_positions, label="Trajectoire réelle")
    plt.plot(noisy_measurements, label="Mesures bruitées", linestyle=":")
    plt.plot(positions, label="Estimation Kalman")
    plt.title("Estimation de la trajectoire (Kalman)")
    plt.xlabel("Étape")
    plt.ylabel("Position estimée")
    plt.legend()
    plt.savefig('images/trajectory.png')
    plt.show()