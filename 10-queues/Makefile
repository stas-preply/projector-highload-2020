.PHONY: help
help:
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
.DEFAULT_GOAL := help

build:
	docker-compose down
	docker-compose build


run-beanstalkd:		## Build and run beanstalkd project
	docker-compose down
	docker-compose up -d beanstalkd beanstalk_console producer receiver
	docker logs -f 10-queues_receiver_1


run-redis:		## Build and run redis project
	docker-compose down
	docker-compose up -d redis && docker-compose up -d producer receiver
	docker logs -f 10-queues_receiver_1


siege:			## Run siege
	docker-compose run --rm siege -d1 -r20 -c25 http://producer:5000


down:				## docker-compose down
	docker-compose down