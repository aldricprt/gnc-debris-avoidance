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


## Résultat du 2025-07-04T16:57:45
Débris simulés aux positions : [[410], [390]] (rayon 5.0 km)
Nombre de nouveaux débris détectés : 2
- Nouveau débris #0 détecté à t=41s, altitude estimée=405.1 km
- Nouveau débris #1 détecté à t=338s, altitude estimée=394.7 km
Débris détectés au final (indices) : [0, 1]
