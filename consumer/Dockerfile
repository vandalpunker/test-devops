FROM python:3.7

WORKDIR /app

# Copy source code
COPY src/ /app/src/
COPY src/pyproject.toml /app

# Install poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH=$PATH:/root/.poetry/bin/
RUN poetry --version \
    && poetry install \
    && poetry add environs \
    && poetry env use python

# Run gunicorn
ENV GUNICORN_CMD_ARGS "--log-level debug  --reload --bind :9001 --workers 1"
CMD ["bash", "-c", "$(poetry env info --path)/bin/gunicorn --chdir src/http_api main:app"]