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


docker-django-run:
	docker-compose up


docker-react:
	docker build -f Node.Dockerfile -t nginx-server .


deploy-backend:
	kubectl create -f deploy/deploy.yaml


kubernetes-secrets:
	# kubectl create 


