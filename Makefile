.PHONY: clean venv test start build-image start-docker test-docker

clean:
	rm -rf venv/ server.log .pytest_cache vaderapi/__pycache__ tests/__pycache__

venv:
	bash scripts/setup_venv.sh

test:
	bash scripts/run_tests.sh

start:
	bash scripts/run_api_server.sh

build-image:
	bash scripts/build_docker_image.sh

start-docker:
	bash scripts/run_api_docker.sh

test-docker:
	bash scripts/run_tests_docker.sh
