FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev libssl-dev libffi-dev build-essential && \
    pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

COPY . /memberspartyapp
WORKDIR /memberspartyapp
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
