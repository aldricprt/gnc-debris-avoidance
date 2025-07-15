#!/bin/bash
# Script à exécuter manuellement pour activer l'environnement virtuel du projet
# Usage : ./scripts/auto_activate_venv.sh

if [ -f "$PWD/.venv/bin/activate" ]; then
    source "$PWD/.venv/bin/activate"
    echo "Environnement virtuel activé."
else
    echo "Aucun environnement virtuel trouvé dans $PWD/.venv."
fi
