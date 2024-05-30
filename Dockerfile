FROM python:3.11.7

ENV DB_NAME Eknis
ENV DB_USER postgres
ENV DB_PASSWORD Shurikgat2704
ENV DB_HOST host.docker.internal

RUN mkdir code

WORKDIR /code/ship-backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=80"]

