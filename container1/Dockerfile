FROM python:3.9.13-slim

WORKDIR /app

ADD . /app

EXPOSE 5000
RUN pip install -r requirements.txt  && \
    export FLASK_APP=app.py && \
    export FLASK_ENV=development


CMD ["python3", "app.py"]
