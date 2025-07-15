import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from gnc.debris_detector import DebrisDetector

# Test simple : détection prédictive positive

def test_debris_detected_predictive():
    sat_pos = [0, 0]
    sat_vel = [1, 0]
    debris_states = [
        {'pos': [2, 0], 'vel': [0, 0]},  # Sur la trajectoire
    ]
    detector = DebrisDetector(debris_states, detection_radius=1.5)
    alerts = detector.detect_predictive(sat_pos, sat_vel, horizon=5, dt=1.0)
    assert len(alerts) == 1
    idx, dmin, tmin = alerts[0]
    assert dmin < 1.5

# Test négatif : pas de débris détecté

def test_no_debris_detected_predictive():
    sat_pos = [0, 0]
    sat_vel = [1, 0]
    debris_states = [
        {'pos': [10, 10], 'vel': [0, 0]},  # Trop loin
    ]
    detector = DebrisDetector(debris_states, detection_radius=1.0)
    alerts = detector.detect_predictive(sat_pos, sat_vel, horizon=5, dt=1.0)
    assert alerts == []

# Test avec plusieurs débris

def test_multiple_debris_predictive():
    sat_pos = [0, 0]
    sat_vel = [1, 0]
    debris_states = [
        {'pos': [2, 0], 'vel': [0, 0]},
        {'pos': [10, 10], 'vel': [0, 0]},
    ]
    detector = DebrisDetector(debris_states, detection_radius=1.5)
    alerts = detector.detect_predictive(sat_pos, sat_vel, horizon=5, dt=1.0)
    detected_indices = [idx for idx, dmin, tmin in alerts]
    assert 0 in detected_indices
    assert 1 not in detected_indices
