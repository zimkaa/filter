FROM python:slim-buster

COPY ./workflow .

RUN python3 -m pip install -r requirements.txt

ENTRYPOINT python3 filter.py