FROM python:3.9.4

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./template.yml /code/template.yml

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]