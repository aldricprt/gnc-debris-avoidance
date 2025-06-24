import numpy as np
from filterpy.kalman import KalmanFilter

class SatelliteTracker:
    def __init__(self, initial_pos=400.0, initial_vel=7.8, dt=1.0):
        """Initialisation avec paramètres orbitaux réalistes.
        
        Args:
            initial_pos (float): Altitude initiale (km) - typ. 400 km pour LEO
            initial_vel (float): Vitesse orbitale (km/s) - typ. 7.8 km/s
            dt (float): Pas temporel (s)
        """
        self.kf = KalmanFilter(dim_x=2, dim_z=1)
        
        # État initial (position, vitesse)
        self.kf.x = np.array([initial_pos, initial_vel])
        
        # Matrice d'état (mouvement képlérien simplifié)
        self.kf.F = np.array([[1., dt], 
                             [0., 1.]])
        
        # Matrice d'observation (on mesure seulement la position)
        self.kf.H = np.array([[1., 0.]])
        
        # Covariance initiale (incertitude)
        self.kf.P = np.diag([10.0, 0.1])  # [±3.2 km, ±0.3 km/s]
        
        # Bruit du capteur (variance en km²)
        self.kf.R = 25.0  # ±5 km d'écart-type
        
        # Bruit du processus (variance)
        self.kf.Q = np.array([[0.1, 0], 
                             [0, 0.01]])  # Perturbations minimes

    def update(self, measurement):
        """Mise à jour avec une nouvelle mesure altimétrique.
        
        Args:
            measurement (float): Mesure de position (km)
        """
        self.kf.predict()
        self.kf.update(np.array([measurement]))
        
        # Forçage physique (altitude toujours positive)
        self.kf.x[0] = max(150, self.kf.x[0])  # Minimum 150 km (évite les valeurs non physiques)
        
        return self.kf.x[0], self.kf.x[1]  # Retourne position ET vitesse