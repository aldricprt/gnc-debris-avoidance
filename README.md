# 🛰️ GNC-DEBRIS-AVOIDANCE
**Système autonome d'évitement de débris pour CubeSats**  
*Algorithmes : Kalman + YOLOv8 + Commande prédictive*

## 🚀 Fonctionnalités
- Filtrage de Kalman pour l'estimation de l'altitude des satellites en orbite basse (LEO)
- Simulation réaliste des mesures de capteur bruitées
- Visualisation professionnelle des trajectoires réelles, bruitées et filtrées
- Code modulaire prêt à être étendu (détection de débris, contrôle, etc.)

## 📁 Structure du projet
- `src/gnc/` : Code source principal (modules Python)
- `tests/` : Tests unitaires et d'intégration (`test_*.py`)
- `notebooks/` : Notebooks Jupyter pour l'exploration
- `scripts/` : Scripts utilitaires ou d'automatisation
- `debris_dataset/` : Jeux de données de débris
- `images/` : Figures et résultats générés
- `run.sh` : Script de lancement principal
- `requirements.txt` : Dépendances Python
- `fiche_commandes.md` : Mémo des commandes utiles

## 🛠️ Dépendances

Installez toutes les dépendances avec :
```bash
pip install -r requirements.txt
```

## ▶️ Comment exécuter

Pour simuler et visualiser le filtrage de Kalman :
```bash
./run.sh
```
Cela générera un graphique dans `images/trajectory.png` montrant :
- La trajectoire réelle du satellite
- Les mesures de capteur bruitées
- L'estimation du filtre de Kalman

## 🧪 Tests

Exécutez tous les tests unitaires avec :
```bash
pytest tests/
```

## 📖 Exemple de sortie

Le script principal simule un satellite en LEO avec des paramètres réalistes, ajoute du bruit aux capteurs et applique le filtrage de Kalman. Le graphique de sortie démontre la capacité du filtre à récupérer la trajectoire réelle à partir de données bruitées.

---

N'hésitez pas à étendre le projet avec la détection de débris, un contrôle avancé ou des dynamiques orbitales plus réalistes !