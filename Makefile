#!make
-include .env
export 

create-env:
	python3 -m venv env


install-reqs:
	pip install -r requirements.txt
