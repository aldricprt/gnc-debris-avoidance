from src.gnc.kalman_filter import SatelliteTracker
from src.gnc.debris_detector import DebrisDetector
from src.gnc.controller import GNController
import matplotlib.pyplot as plt

# Initialisation
tracker = SatelliteTracker()
detector = DebrisDetector()
controller = GNController(tracker, detector)

# Simulation
positions = [tracker.update(z) for z in noisy_measurements]
plt.plot(positions)
plt.savefig('images/trajectory.png')