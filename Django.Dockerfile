FROM python:3
RUN mkdir /dhrishti
WORKDIR /dhrishti
COPY . .
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000
EXPOSE 8000