#!make
-include .env
export


create-env:
	python3 -m venv .venv
	# source ./.venv/bin/activate


requirements:
	pip install -r requirements.txt


react-requirements:
	npm install


run: 
	python manage.py runserver


docker-django:
	docker build -f Django.Dockerfile -t dhrishti-backend .


django-run:
	docker run -d -p 8000:8000 --name dhrishti dhrishti-backend


docker-nginx:
	docker build -f Node.Dockerfile -t nginx-server frontend







