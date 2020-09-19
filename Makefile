#!make
-include .env
export

create-env:
	python3 -m venv .venv

requirements:
	pip install -r requirements.txt

run: 
	npm run dev
	python manage.py runserver
