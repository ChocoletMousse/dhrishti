FROM python
WORKDIR /project/dhrishti
COPY . /project/dhrishti
RUN make create-env && source .venv/bin/activate && make requirements
CMD python manage.py runserver