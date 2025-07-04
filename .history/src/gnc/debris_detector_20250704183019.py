import numpy as np

class DebrisDetector:
    """
    Détecteur de débris basé sur la distance, avec suivi d'historique.
    debris_positions : liste de positions (ex : [[x1, y1], [x2, y2], ...])
    detection_radius : rayon de détection (même unité que les positions)
    """
    def __init__(self, debris_positions, detection_radius=5.0):
        self.debris_positions = debris_positions
        self.detection_radius = detection_radius
        self.detected_history = set()  # Indices des débris déjà détectés

    def detect(self, sat_position):
        detected_now = []
        for idx, debris in enumerate(self.debris_positions):
            if np.linalg.norm(np.array(sat_position) - np.array(debris)) < self.detection_radius:
                if idx not in self.detected_history:
                    self.detected_history.add(idx)
                    detected_now.append(idx)
        return detected_now  # Liste des indices de nouveaux débris détectés

    def get_detected(self):
        """Retourne la liste des indices de tous les débris déjà détectés."""
        return list(self.detected_history)
