IMAGE_NAME=shopify_django_app

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -d --name $(IMAGE_NAME) -v $(PWD):/app -p 8000:8000 $(IMAGE_NAME)

stop:
	docker stop $(IMAGE_NAME)
	docker rm $(IMAGE_NAME)

shell:
	docker run -it $(IMAGE_NAME) /bin/bash

migration:
	docker run -it -v $(PWD):/app $(IMAGE_NAME) pipenv run python manage.py migrate
