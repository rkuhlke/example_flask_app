FROM python:3.9-slim
ENV PYTHONBUFFERED True

RUN apt update && apt install dnsutils -y

ENV APP_HOME /example_flask_app
WORKDIR ${APP_HOME}

RUN python3 -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec gunicorn --bind :PORT --workers 1 --threads 8 --timeout 0 'main:create_app()' 