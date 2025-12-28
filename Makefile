.PHONY: lint

lint:
	cd api && uv run ruff check .
	cd api && uv run ruff format --check .
