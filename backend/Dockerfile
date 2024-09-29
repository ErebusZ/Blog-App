FROM python:3.11-slim

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
 libpq-dev gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

WORKDIR /code/blog

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
