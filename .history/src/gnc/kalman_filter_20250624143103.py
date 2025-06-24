import numpy as np
from filterpy.kalman import KalmanFilter

class SatelliteTracker:
    def __init__(self, initial_pos=0, initial_vel=0, dt=1.0):
        self.kf = KalmanFilter(dim_x=2, dim_z=1)
        self.kf.x = np.array([initial_pos, initial_vel])
        self.kf.F = np.array([[1., dt], [0., 1.]])  # Matrice d'état
        self.kf.H = np.array([[1., 0.]])            # Matrice d'observation
    
    def update(self, measurement):
        """Filtrage d'une nouvelle mesure"""
        self.kf.predict()
        self.kf.update(measurement)
        return self.kf.x[0]  # Position estimée