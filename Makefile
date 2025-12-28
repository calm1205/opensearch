.PHONY: lint create_mappings add_index delete_all

lint:
	cd api && uv run ruff check .
	cd api && uv run ruff format --check .

create_mappings:
	./scripts/create_mappings.sh

add_index:
	./scripts/add_index.sh

show_index:
	./scripts/show_index.sh

delete_all:
	./scripts/delete_all.sh

setup:
	make delete_all
	make create_mappings
	make add_index