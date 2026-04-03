#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_NAME = shopping-x
PYTHON_VERSION = 3.13
PYTHON_INTERPRETER = python

#################################################################################
# COMMANDS                                                                      #
#################################################################################


## Install Python dependencies
.PHONY: requirements
requirements:
	$(PYTHON_INTERPRETER) -m pip install -U pip
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	



## Delete all compiled Python files
.PHONY: clean
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete


## Format source code with ruff
.PHONY: format
format:
	ruff format . | isort .



## Run tests
.PHONY: test
test:
	python -m pytest tests


## Set up Python interpreter environment
.PHONY: env
env:
	python -m venv .venv


#################################################################################
# PROJECT RULES                                                                 #
#################################################################################

.PHONY: all
all: dataset features train predict

dataset:
	$(PYTHON_INTERPRETER) src/dataset.py

features:
	$(PYTHON_INTERPRETER) src/features.py

plots:
	$(PYTHON_INTERPRETER) src/plots.py

train:
	$(PYTHON_INTERPRETER) src/modeling/train.py

predict:
	$(PYTHON_INTERPRETER) src/modeling/predict.py


#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys; \
lines = '\n'.join([line for line in sys.stdin]); \
matches = re.findall(r'\n## (.*)\n[\s\S]+?\n([a-zA-Z_-]+):', lines); \
print('Available rules:\n'); \
print('\n'.join(['{:25}{}'.format(*reversed(match)) for match in matches]))
endef
export PRINT_HELP_PYSCRIPT

help:
	@$(PYTHON_INTERPRETER) -c "${PRINT_HELP_PYSCRIPT}" < $(MAKEFILE_LIST)
