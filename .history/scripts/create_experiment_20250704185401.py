import os
import sys
from datetime import date

TEMPLATE = """# Log: {exp_name} (branche {branch})

**Start date: {today}**

## Objectif
Décrire brièvement l'objectif de l'expérimentation.

## Méthode
- Décrire la méthode, les paramètres, les outils utilisés.

## Résultats
- Résumer les résultats principaux, indiquer les figures générées.

## Analyse
- Analyse critique, points forts/faibles, axes d'amélioration.

## Next steps
- Propositions pour la suite.

---

*Ce log est généré automatiquement pour la traçabilité de l'expérimentation.*
"""

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_experiment.py <nom_branche>")
        sys.exit(1)
    branch = sys.argv[1]
    exp_dir = os.path.join("../experiments", branch)
    figures_dir = os.path.join(exp_dir, "figures")
    log_path = os.path.join(exp_dir, f"{branch}_log.md")
    os.makedirs(figures_dir, exist_ok=True)
    today = date.today().isoformat()
    with open(log_path, "w") as f:
        f.write(TEMPLATE.format(exp_name=branch.replace('-', ' ').capitalize(), branch=branch, today=today))
    print(f"Expérimentation initialisée dans {exp_dir}\n- Log: {log_path}\n- Figures: {figures_dir}")

if __name__ == "__main__":
    main()
