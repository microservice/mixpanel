FROM python:3.8-alpine

RUN         mkdir /app
ADD         requirements.txt /app
RUN         pip install -r /app/requirements.txt
ADD         app.py /app

ENTRYPOINT  ["python", "/app/app.py"]
