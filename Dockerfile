FROM python:3.5

ENV PYTHONUNBUFFERED = 1

ENV WEBAPP_DIR=/raports_app

WORKDIR $WEBAPP_DIR

ADD requirements.txt $WEBAPP_DIR/

RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR/
