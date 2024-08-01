FROM python:3.11.6
LABEL authors="chernyshev-pridvorov"

RUN pip install poetry

WORKDIR /var/db_source/

COPY /pyproject.toml /var/db_source/



RUN poetry config virtualenvs.create false \
    && poetry install --no-root \
    && poetry update

COPY . /var/db_source

EXPOSE 5623:5623


ENTRYPOINT ["python", "./src/main.py"]