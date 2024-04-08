SHELL:=/bin/bash
# ignore files/folders that match target names. eg. Python packages
# create a `build` folder, which breaks the `make build` target with:
# `make: 'build' is up to date.`.
.PHONY: test build lint

create-venv:
	rm -rf .venv || true
	python -m venv .venv

activate-venv:
	. .venv/bin/activate

install-deps:
	@( \
		. .venv/bin/activate; \
		pip install .; \
	)

install-build-deps:
	@( \
		. .venv/bin/activate; \
		pip install .[build]; \
	)

install-lint-deps:
	@( \
		. .venv/bin/activate; \
		pip install .[lint]; \
	)

install-test-deps:
	@( \
		. .venv/bin/activate; \
		pip install .[test]; \
	)

dev-setup: create-venv install-build-deps install-lint-deps install-test-deps
	@( \
		. .venv/bin/activate; \
		pip install --editable .; \
	)

lint:
	@( \
		. .venv/bin/activate; \
		ruff check \
	)

lint-fix:
	@( \
		. .venv/bin/activate; \
		ruff check --fix \
	)

lint-fix-unsafe:
	@( \
		. .venv/bin/activate; \
		ruff check --fix --unsafe-fixes \
	)

build:
	@( \
		. .venv/bin/activate; \
		python -m build \
	)

test:
	@( \
		. .venv/bin/activate; \
		pytest \
	)

semantic-release:
	docker build --progress=plain -f .dev/semantic-release/Dockerfile -t semantic-release .
	docker run --rm --name sr -e GITHUB_TOKEN=${GITHUB_TOKEN} -v "${PWD}":/app  -v ~/.ssh:/root/.ssh/ semantic-release

run-dev:
	@( \
		. .venv/bin/activate; \
		python src/rules_engine/main.py \
	)
