FROM python:3.8-slim

COPY ./srv_reader /home/app
COPY ./data /tmp/data/

WORKDIR /home/app

RUN pip3.8 install --upgrade pip
RUN pip3.8 install -r requirements.txt

CMD [ "python3.8", "-u", "main.py" ]