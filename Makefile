name="example_flask_app"
tag="0.0.1"

del:
	sudo docker system prune -a --volumes -f

build:
	sudo docker build -f Dockerfile -t ${name}:${tag} .

run: 
	sudo docker run ${name}:${tag}

all:
	make build
	make run

private_build:
	sudo docker build -f Dockerfile_local -t ${name}:${tag} .

private_run: 
	sudo docker run ${name}:${tag}

private_all:
	make private_build
	make private_run
