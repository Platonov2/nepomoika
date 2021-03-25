FROM python:3.8-slim

COPY /backend/requirements.txt ./backend/requirements.txt

RUN pip install -r ./backend/requirements.txt

COPY backend ./backend
COPY main.py ./