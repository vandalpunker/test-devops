FROM python:3.7

WORKDIR /app

# Copy source code
COPY src/ /app/src/

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH=$PATH:/root/.poetry/bin/
RUN poetry --version && cd /app/src/ && poetry install

# Run gunicorn
ENV GUNICORN_CMD_ARGS "--log-level debug  --reload --bind :9001 --workers 1"
CMD ["bash", "-c", "/root/.cache/pypoetry/virtualenvs/src-9TtSrW0h-py3.7/bin/gunicorn --chdir src/http_api main:app"]