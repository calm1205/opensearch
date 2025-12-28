.PHONY: lint create_mappings

lint:
	cd api && uv run ruff check .
	cd api && uv run ruff format --check .

create_mappings:
	./scripts/create_mappings.sh

add_index:
	./scripts/add_index.sh