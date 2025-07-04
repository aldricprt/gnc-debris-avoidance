# Makefile pour automatiser la création d'une nouvelle expérimentation

.PHONY: new-experiment

new-experiment:
	@echo "Usage : make new-experiment NAME=nom_branche"

new-experiment-%:
	python3 scripts/create_experiment.py $*
