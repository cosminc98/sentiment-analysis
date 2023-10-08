.PHONY: venv test start docker-image start-docker

venv:
	bash scripts/setup_venv.sh

test:
	bash scripts/run_tests.sh

start:
	bash scripts/run_api_server.sh

docker-image:
	bash scripts/create_docker_image.sh

start-docker:
	bash scripts/run_from_docker.sh
