#!/bin/bash
# Script à placer dans scripts/ et à sourcer dans ton .zshrc ou .bashrc
# Usage : source /chemin/vers/scripts/auto_activate_venv.sh

if [ -f "$PWD/.venv/bin/activate" ]; then
    source "$PWD/.venv/bin/activate"
fi
