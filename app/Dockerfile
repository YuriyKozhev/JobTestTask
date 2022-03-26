FROM python:3.10

ENV PYTHONUNBUFFERED=1

USER root

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD python app.py
