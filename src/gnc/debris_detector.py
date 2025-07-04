import numpy as np

class DebrisDetector:
    """
    Détecteur de débris basé sur la distance.
    debris_positions : liste de positions (ex : [[x1, y1], [x2, y2], ...])
    detection_radius : rayon de détection (même unité que les positions)
    """
    def __init__(self, debris_positions, detection_radius=5.0):
        self.debris_positions = debris_positions
        self.detection_radius = detection_radius

    def detect(self, sat_position):
        for debris in self.debris_positions:
            if np.linalg.norm(np.array(sat_position) - np.array(debris)) < self.detection_radius:
                return True
        return False
