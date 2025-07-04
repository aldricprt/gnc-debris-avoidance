import pytest
from gnc.debris_detector import DebrisDetector

# Test simple : détection positive

def test_debris_detected():
    detector = DebrisDetector(debris_positions=[[0, 0]], detection_radius=2.0)
    assert detector.detect([1, 1]) is True

# Test négatif : pas de débris détecté

def test_no_debris_detected():
    detector = DebrisDetector(debris_positions=[[0, 0]], detection_radius=1.0)
    assert detector.detect([2, 2]) is False

# Test avec plusieurs débris

def test_multiple_debris():
    detector = DebrisDetector(debris_positions=[[0, 0], [5, 5]], detection_radius=1.5)
    assert detector.detect([5, 6]) is True
    assert detector.detect([10, 10]) is False
