FROM python:3.8-slim

RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean

WORKDIR /src/

RUN mkdir model

RUN cd model

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install --upgrade pip

COPY . .

EXPOSE 3000

CMD ["python", "main.py"]