#!/bin/zsh
# Script de lancement du projet GNC Debris Avoidance

# Activation de l'environnement virtuel si présent
if [ -d .venv ]; then
    source .venv/bin/activate
fi

# Lancement du script principal
python main.py
