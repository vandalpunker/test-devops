FROM python:3.7

WORKDIR /app

# Install poetry and dependencies
COPY src/pyproject.toml /app
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH=$PATH:/root/.poetry/bin/
RUN poetry --version \
    && poetry install \
    && poetry add environs \
    && poetry env use python

# Copy source code
COPY src/ /app/src/

# Run gunicorn
ENV GUNICORN_CMD_ARGS "--log-level debug --reload --bind :9000 --workers 1"
CMD ["bash", "-c", "$(poetry env info --path)/bin/gunicorn --chdir src/http_api main:app"]

