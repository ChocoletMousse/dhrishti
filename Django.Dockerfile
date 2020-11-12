FROM python:3
WORKDIR /dhrishti
COPY ["./dhrishtirest", "./dhrishtisettings"]
RUN make create-env && source .venv/bin/activate && make requirements
# CMD python manage.py runserver