import numpy as np
from gnc.debris_detector import DebrisDetector

def test_predictive_detection():
    # Satellite initial position and velocity
    sat_pos = [0, 0]
    sat_vel = [1, 0]  # Avance sur x

    # Un débris qui va croiser la trajectoire du satellite
    debris_states = [
        {'pos': [10, 5], 'vel': [0, -1]},  # Descend sur y, croisement prévu
        {'pos': [20, 20], 'vel': [0, 0]},  # Trop loin, pas de risque
    ]
    detector = DebrisDetector(debris_states, detection_radius=2.0)
    alerts = detector.detect_predictive(sat_pos, sat_vel, horizon=20, dt=0.5)
    detected_indices = [idx for idx, dmin, tmin in alerts]
    print(f"Distances minimales calculées : {[detector._min_distance_over_horizon(sat_pos, sat_vel, d['pos'], d['vel'], 20, 0.5)[0] for d in debris_states]}")
    print(f"Indices détectés : {detected_indices}")
    assert 0 in detected_indices
    assert 1 not in detected_indices
    for idx, dmin, tmin in alerts:
        assert dmin < 2.0
        assert tmin > 0

def test_no_false_positive():
    sat_pos = [0, 0]
    sat_vel = [1, 0]
    debris_states = [
        {'pos': [100, 100], 'vel': [0, 0]},
    ]
    detector = DebrisDetector(debris_states, detection_radius=2.0)
    alerts = detector.detect_predictive(sat_pos, sat_vel, horizon=50, dt=1.0)
    assert alerts == []
