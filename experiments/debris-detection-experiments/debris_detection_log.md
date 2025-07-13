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


## Résultat du 2025-07-04T17:10:41
Débris simulés aux positions : [{'pos': [410], 'vel': [-0.01]}, {'pos': [390], 'vel': [0.01]}] (rayon 5.0 km)
Nombre de nouvelles alertes de collision : 2
- Alerte débris #0 à t=0s, altitude estimée=402.3 km, distance min=3.87 km dans 59.0s
- Alerte débris #1 à t=11s, altitude estimée=402.0 km, distance min=3.34 km dans 59.0s
Débris détectés au final (indices) : [0, 1]


## Résultat du 2025-07-04T17:16:08
Débris simulés aux positions : [{'pos': [410], 'vel': [-0.005]}, {'pos': [390], 'vel': [0.005]}] (rayon 2.0 km)
Nombre de nouvelles alertes de collision : 2
- Alerte débris #0 à t=13s, altitude estimée=402.1 km, distance min=1.31 km dans 29.0s
- Alerte débris #1 à t=44s, altitude estimée=400.9 km, distance min=1.82 km dans 29.0s
Débris détectés au final (indices) : [0, 1]


## Résultat du 2025-07-04T17:16:53
Débris simulés aux positions : [{'pos': [415], 'vel': [-0.005]}, {'pos': [395], 'vel': [0.005]}] (rayon 2.0 km)
Nombre de nouvelles alertes de collision : 2
- Alerte débris #1 à t=6s, altitude estimée=398.1 km, distance min=0.05 km dans 18.0s
- Alerte débris #0 à t=18s, altitude estimée=403.8 km, distance min=1.42 km dans 29.0s
Débris détectés au final (indices) : [0, 1]


## Résultat du 2025-07-04T17:19:42
Débris simulés aux positions : [{'pos': [415], 'vel': [-0.005]}, {'pos': [395], 'vel': [0.005]}] (rayon 2.0 km)
Nombre de nouvelles alertes de collision : 2
- Alerte débris #1 à t=5s, altitude estimée=399.3 km, distance min=0.03 km dans 23.0s
- Alerte débris #0 à t=69s, altitude estimée=407.1 km, distance min=0.18 km dans 20.0s
Débris détectés au final (indices) : [0, 1]


## Résultat du 2025-07-04T17:20:30
Débris simulés aux positions : [{'pos': [415], 'vel': [-0.005]}, {'pos': [395], 'vel': [0.005]}] (rayon 0 km)
Nombre de nouvelles alertes de collision : 0
Débris détectés au final (indices) : []


## Résultat du 2025-07-05T15:11:35
Débris simulés aux positions : [{'pos': [415], 'vel': [-0.005]}, {'pos': [395], 'vel': [0.005]}] (rayon 0.01 km)
Nombre de nouvelles alertes de collision : 2
- Alerte débris #0 à t=42s, altitude estimée=407.9 km, distance min=0.01 km dans 21.0s
- Alerte débris #1 à t=195s, altitude estimée=405.7 km, distance min=0.00 km dans 28.0s
Débris détectés au final (indices) : [0, 1]


## Résultat du 2025-07-13T08:49:26
Débris simulés aux positions : [{'pos': [415], 'vel': [-0.005]}, {'pos': [395], 'vel': [0.005]}] (rayon 0.01 km)
Nombre de nouvelles alertes de collision : 2
- Alerte débris #0 à t=148s, altitude estimée=411.1 km, distance min=0.01 km dans 22.0s
- Alerte débris #1 à t=243s, altitude estimée=403.5 km, distance min=0.00 km dans 26.0s
Débris détectés au final (indices) : [0, 1]
