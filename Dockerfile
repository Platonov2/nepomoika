FROM python:3.8-slim

WORKDIR /code

#COPY requirements.txt /
#RUN pip install -r /requirements.txt
RUN python -m pip install -U flask-cors
RUN python -m pip install pika
RUN python -m pip install Flask==1.1.1
RUN python -m pip install requests==2.4.2
RUN python -m pip install requests==2.4.2
RUN python -m pip install -U Flask-SQLAlchemy
RUN python -m pip install Flask-Migrate
RUN python -m pip install psycopg2-binary
#RUN python -m pip install pika

#RUN export FLASK_APP=server.py

#ENV FLASK_APP="server.py"
#
#RUN flask db init
#RUN flask db migrate
#RUN flask db upgrade
COPY . .