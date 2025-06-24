from src.gnc.kalman_filter import SatelliteTracker
from src.gnc.debrus_detector import DebrisDetector
from src.gnc.controller import GNController
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    # Exemple de mesures bruitées simulées
    noisy_measurements = np.random.normal(loc=0, scale=1, size=50)
    tracker = SatelliteTracker()
    detector = DebrisDetector()
    controller = GNController(tracker, detector)

    # Simulation
    positions = [tracker.update(z) for z in noisy_measurements]
    plt.plot(positions)
    plt.title("Estimation de la trajectoire (Kalman)")
    plt.xlabel("Étape")
    plt.ylabel("Position estimée")
    plt.savefig('images/trajectory.png')
    plt.show()