import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from gnc.kalman_filter import SatelliteTracker

# Test 1 : Convergence immédiate si état initial = mesure

def test_kalman_convergence():
    tracker = SatelliteTracker(initial_pos=10.0, initial_vel=0.0, min_altitude=None)
    tracker.update(10)
    assert tracker.kf.x[0] == pytest.approx(10, abs=1.0)

# Test 2 : Convergence progressive depuis un mauvais état initial

def test_kalman_convergence_from_far():
    tracker = SatelliteTracker(initial_pos=400.0, initial_vel=0.0, min_altitude=None)
    # On augmente le nombre d'itérations pour laisser le temps au filtre de converger
    for _ in range(100):
        tracker.update(10)
    assert tracker.kf.x[0] == pytest.approx(10, abs=2.0)

# Test 3 : Stabilité face au bruit de mesure

def test_kalman_with_noisy_measurements():
    tracker = SatelliteTracker(initial_pos=400.0, initial_vel=0.0, min_altitude=None)
    import numpy as np
    np.random.seed(42)
    measurements = 10 + np.random.normal(0, 5, 50)
    for z in measurements:
        tracker.update(z)
    # L'estimation doit rester proche de la moyenne des mesures
    assert tracker.kf.x[0] == pytest.approx(10, abs=3.0)

# Test 4 : Respect de la contrainte d'altitude minimale

def test_kalman_min_altitude():
    tracker = SatelliteTracker(initial_pos=200.0, initial_vel=0.0, min_altitude=180)
    tracker.update(100)  # Mesure très basse
    assert tracker.kf.x[0] >= 180