import numpy as np
from gnc.debris_detector import DebrisDetector

def test_no_false_positive():
    sat_pos = [0, 0]
    sat_vel = [1, 0]
    debris_states = [
        {'pos': [100, 100], 'vel': [0, 0]},
    ]
    detector = DebrisDetector(debris_states, detection_radius=2.0)
    alerts = detector.detect_predictive(sat_pos, sat_vel, horizon=50, dt=1.0)
    assert alerts == []
