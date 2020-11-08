FROM python:3
RUN mkdir /dhrishti
WORKDIR /dhrishti
COPY . .
RUN pip install -r requirements.txt
ENV DJANGO_DEBUG 1
ENV DJANGO_ALLOWED_HOSTS '0.0.0.0,localhost,127.0.0.1'
EXPOSE 8000
CMD gunicorn --bind :8000 dhrishtisettings.wsgi:application