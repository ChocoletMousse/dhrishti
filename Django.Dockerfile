FROM python:3
WORKDIR /dhrishti
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000