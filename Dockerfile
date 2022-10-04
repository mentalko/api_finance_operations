FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -Iv --no-cache-dir uvicorn asyncpg psycopg2-binary
RUN pip install --no-cache-dir -r /code/requirements.txt


COPY ./src /code/src

# CMD python app.py
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]