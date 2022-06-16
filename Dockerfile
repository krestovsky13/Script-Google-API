FROM python:3.10

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python3 -m pip install --upgrade pip

COPY ./req.txt .
RUN pip install -r req.txt

COPY . .
