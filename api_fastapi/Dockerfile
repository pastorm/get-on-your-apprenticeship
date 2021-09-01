FROM tiangolo/uvicorn-gunicorn:python3.8-alpine3.10

ARG INSTALL_DEV=false
ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN /bin/sh -c "\
    apk add curl && \
    curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false \
    "

COPY ./poetry.lock ./pyproject.toml /app/

RUN /bin/sh -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install ; else poetry install --no-dev ; fi ; mkdir -p api/static"

COPY ./api /app/

ENV PYTHONPATH=/app
