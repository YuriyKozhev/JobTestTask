FROM python:3.10

ENV PYTHONUNBUFFERED=1

USER root

COPY . .

RUN pip install --upgrade pip
RUN pip install pip-tools==6.5.1
RUN pip-compile
RUN pip-sync

CMD python app.py
