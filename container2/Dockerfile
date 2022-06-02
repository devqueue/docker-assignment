FROM python:3.9.13-slim

WORKDIR /app

ADD . /app

EXPOSE 6000

RUN pip install -r requirements.txt  && \
    export FLASK_APP=run.py && \
    export FLASK_ENV=development

CMD ["python3", "app.py"]
