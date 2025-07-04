# Log: Intégration d'un module de détection de débris (approche simple)

**Date de début : 2025-07-04**

## Objectif
Intégrer un module de détection de débris basé sur la distance dans la simulation GNC, et documenter chaque étape/test/choix technique.

## Étape 1 : Création du module de détection de débris

- Créer un fichier `src/gnc/debris_detector.py`.
- Définir une classe `DebrisDetector` qui prend une liste de positions de débris et un rayon de détection.
- Méthode `detect(sat_position)` qui retourne True si un débris est détecté à proximité.

## Étape 2 : Tests unitaires

- Créer un test dans `tests/test_debris_detector.py` pour valider le comportement du module.

## Étape 3 : Intégration dans la simulation

- Appeler le module de détection à chaque pas de temps.
- Logguer les cas où un débris est détecté.

## Étape 4 : Améliorations et variantes

- Tester avec plusieurs débris, différents rayons, positions bruitées, etc.

---

*Ce fichier sera complété à chaque étape pour garder une trace claire de l'évolution du module.*
