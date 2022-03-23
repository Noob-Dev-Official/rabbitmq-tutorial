FROM python:3.9

RUN apt-get -y update

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-u", "/app/sender.py"]

