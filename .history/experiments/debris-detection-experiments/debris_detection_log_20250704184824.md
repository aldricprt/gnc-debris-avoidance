# Log: Debris Detection Experiments (branche debris-detection-experiments)

**Start date: 2025-07-04**

## Objective
Integrate and improve a debris detection module in the GNC simulation. Each step, test, and technical choice is documented here.

## Steps

### 1. Module creation
- File: `src/gnc/debris_detector.py`
- Class: `DebrisDetector` (distance-based detection, with history)

### 2. Unit tests
- File: `tests/test_debris_detector.py`
- Tests: detection, no detection, multiple debris, history

### 3. Integration in simulation
- File: `main.py`
- Call the detector at each time step, log new detections, plot results

### 4. Improvements
- Track and plot distance to each debris
- Log only first detection per debris
- Save all figures in this folder

---

*This file is updated for each experiment in this branch. Figures are saved in the same folder.*
