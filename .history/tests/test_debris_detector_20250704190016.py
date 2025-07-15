import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from gnc.debris_detector import DebrisDetector

# Test simple : détection positive
def test_debris_detected():
    detector = DebrisDetector(debris_positions=[[0, 0]], detection_radius=2.0)
    assert detector.detect([1, 1]) != []  # Détection attendue

# Test négatif : pas de débris détecté
def test_no_debris_detected():
    detector = DebrisDetector(debris_positions=[[0, 0]], detection_radius=1.0)
    assert detector.detect([2, 2]) == []  # Pas de détection

# Test avec plusieurs débris
def test_multiple_debris():
    detector = DebrisDetector(debris_positions=[[0, 0], [5, 5]], detection_radius=1.5)
    assert detector.detect([5, 6]) != []  # Détection attendue
    assert detector.detect([10, 10]) == []  # Pas de détection
