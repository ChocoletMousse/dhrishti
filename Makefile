#!make
-include .env
export

create-env:
	python3 -m venv .venv

requirements:
	pip install -r requirements.txt

run: 
	python manage.py runserver