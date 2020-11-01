FROM python:3
WORKDIR /dhrishti
COPY . .
RUN pip install -r requirements.txt
CMD python manage.py runserver
EXPOSE 8000