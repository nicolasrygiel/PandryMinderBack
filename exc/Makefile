BUILD_DIR := .

# API
api:
	@PYTHONPATH=$(BUILD_DIR) \
	uv run api/main.py

# SCRIPTS
create:
	@PYTHONPATH=$(BUILD_DIR) \
	uv run scripts/db_create.py

# TODO adapt to uv stuff
install:
	uv add -r requirements.txt

# TODO adapt to uv
freeze:
	pip freeze > requirements_freeze.txt

.PHONY: api