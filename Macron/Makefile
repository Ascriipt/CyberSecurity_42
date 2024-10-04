CONTAINER_NAME = rancongiciel
IMAGE_NAME = rancongiciel

.PHONY: re build run stop rm join all

re: stop rm build run join

clean: stop rm

start: build run

all: build run join

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run -d --name ${CONTAINER_NAME} ${IMAGE_NAME}

stop:
	-docker stop ${CONTAINER_NAME}

rm:
	-docker rm ${CONTAINER_NAME}

join:
	@-docker exec -it ${CONTAINER_NAME} /bin/bash
