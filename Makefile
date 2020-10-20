#!make
-include .env
export


create-env:
	python3 -m venv .venv
	source ./.venv/bin/activate


requirements:
	pip install -r requirements.txt
	npm


run: 
	# npm run dev
	python manage.py runserver


docker-django:
	docker build -f Django.Dockerfile -t dhrishti-backend .


react-requirements:
	npm install


