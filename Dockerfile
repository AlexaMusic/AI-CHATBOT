FROM python:3.9.7-slim
RUN apt-get update
RUN apt-get install -y python3 python3-pip python-dev build-essential python3-venv
RUN mkdir -p /code
ADD . /code
WORKDIR /code
RUN pip3 install -r requirements.txt
CMD python3 -m Aibot
