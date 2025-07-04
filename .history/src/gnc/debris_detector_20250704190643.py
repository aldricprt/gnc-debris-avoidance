import numpy as np

class DebrisDetector:
    """
    Détecteur de débris prédictif (position + vitesse).
    debris_states : liste de dicts {'pos': [x, y], 'vel': [vx, vy]}
    detection_radius : seuil d'alerte (distance minimale prédite)
    """
    def __init__(self, debris_states, detection_radius=5.0):
        self.debris_states = debris_states
        self.detection_radius = detection_radius
        self.detected_history = set()

    def predict_min_distance(self, sat_pos, sat_vel, horizon=60, dt=1.0):
        """
        Prédit la distance minimale entre le satellite et chaque débris sur un horizon donné (en secondes).
        Retourne une liste de tuples (idx, d_min, t_min).
        """
        results = []
        for idx, debris in enumerate(self.debris_states):
            d_min, t_min = self._min_distance_over_horizon(
                sat_pos, sat_vel, debris['pos'], debris['vel'], horizon, dt
            )
            results.append((idx, d_min, t_min))
        return results

    def detect_predictive(self, sat_pos, sat_vel, horizon=60, dt=1.0):
        """
        Détecte les débris dont la distance minimale prédite passe sous le seuil.
        Retourne la liste des indices de débris à risque.
        """
        alerts = []
        for idx, d_min, t_min in self.predict_min_distance(sat_pos, sat_vel, horizon, dt):
            if d_min < self.detection_radius and idx not in self.detected_history:
                self.detected_history.add(idx)
                alerts.append((idx, d_min, t_min))
        return alerts

    @staticmethod
    def _min_distance_over_horizon(sat_pos, sat_vel, debris_pos, debris_vel, horizon, dt):
        t_vals = np.arange(0, horizon, dt)
        min_dist = float('inf')
        t_min = 0
        for t in t_vals:
            sat = np.array(sat_pos) + t * np.array(sat_vel)
            debris = np.array(debris_pos) + t * np.array(debris_vel)
            dist = np.linalg.norm(sat - debris)
            if dist < min_dist:
                min_dist = dist
                t_min = t
        return min_dist, t_min

    def get_detected(self):
        """Retourne la liste des indices de tous les débris déjà détectés."""
        return list(self.detected_history)
