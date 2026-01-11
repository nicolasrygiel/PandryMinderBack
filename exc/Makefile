BUILD_DIR := .

# API
api:
	@PYTHONPATH=$(BUILD_DIR) \
	python api/main.py

# SCRIPTS
create:
	@PYTHONPATH=$(BUILD_DIR) \
	python scripts/db_create.py

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements_freeze.txt

.PHONY: api