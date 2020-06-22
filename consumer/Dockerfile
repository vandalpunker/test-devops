FROM python:3.7

WORKDIR /app

ENV GUNICORN_CMD_ARGS "--log-level debug  --reload --bind :9001 --workers 1"

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python \
    && /root/.poetry/bin/poetry --version

# Copy source code
COPY src/ /app/

# Install dependencies
RUN /root/.poetry/bin/poetry install

CMD ["bash", "-c", "/root/.cache/pypoetry/virtualenvs/src-9TtSrW0h-py3.8/bin/gunicorn http_api main:app"]