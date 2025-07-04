import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from gnc.kalman_filter import SatelliteTracker

def test_kalman_convergence():
    tracker = SatelliteTracker()
    tracker.update(10)
    assert tracker.kf.x[0] == pytest.approx(10, abs=1.0)