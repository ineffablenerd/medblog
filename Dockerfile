FROM python:3.10-buster

ENV PYTHONBUFFERED =1

WORKDIR /medblog

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000