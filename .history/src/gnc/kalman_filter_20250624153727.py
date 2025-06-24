import numpy as np
from filterpy.kalman import KalmanFilter

class SatelliteTracker:
    """
    Kalman Filter-based tracker for satellite altitude and velocity estimation in Low Earth Orbit (LEO).

    This class implements a simple 1D Kalman Filter to estimate the altitude (and optionally velocity)
    of a satellite from noisy altitude measurements. The model assumes a nearly constant velocity
    (Keplerian motion, no drag or maneuvers) and is suitable for educational or prototyping purposes.
    
    Attributes:
        kf (KalmanFilter): The underlying FilterPy KalmanFilter instance.

    Args:
        initial_pos (float): Initial altitude in km (default: 400.0, typical LEO altitude).
        initial_vel (float): Initial velocity in km/s (default: 7.8, typical LEO velocity).
        dt (float): Time step in seconds (default: 1.0).
    """
    def __init__(self, initial_pos=400.0, initial_vel=7.8, dt=1.0):
        """Initialize the Kalman Filter with realistic orbital parameters.

        Args:
            initial_pos (float): Initial altitude in km (default: 400.0)
            initial_vel (float): Initial velocity in km/s (default: 7.8)
            dt (float): Time step in seconds (default: 1.0)
        """
        self.kf = KalmanFilter(dim_x=2, dim_z=1)
        
        # Initial state (position, velocity)
        self.kf.x = np.array([initial_pos, initial_vel])
        
        # State transition matrix (simplified Keplerian motion)
        self.kf.F = np.array([[1., dt], 
                             [0., 1.]])
        
        # Measurement matrix (we only measure position)
        self.kf.H = np.array([[1., 0.]])
        
        # Initial covariance (uncertainty)
        self.kf.P = np.diag([10.0, 0.1])  # [±3.2 km, ±0.3 km/s]
        
        # Sensor noise (variance in km²)
        self.kf.R = 25.0  # ±5 km standard deviation
        
        # Process noise (variance)
        self.kf.Q = np.array([[0.1, 0], 
                             [0, 0.01]])  # Minimal perturbations

    def update(self, measurement):
        """Update the filter with a new altitude measurement.

        Args:
            measurement (float): Noisy altitude measurement in km.

        Returns:
            float: Estimated altitude (km) after filtering.
        """
        self.kf.predict()
        self.kf.update(np.array([measurement]))
        
        # Physical constraint (altitude must remain positive)
        self.kf.x[0] = max(150, self.kf.x[0])  # Minimum 150 km (avoids non-physical values)
        
        return self.kf.x[0]  # Return only the estimated altitude