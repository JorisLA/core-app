########## build image ##########
FROM ghcr.io/astral-sh/uv:0.6.7-python3.13-bookworm AS builder

## add Gitlab Repository Access for private git repositories
ENV UV_COMPILE_BYTECODE=1

## add and install requirements
WORKDIR /opt
COPY ./pyproject.toml .
COPY ./uv.lock .
RUN uv sync --no-dev --locked


########## service image ##########
FROM python:3.13-slim-bullseye AS runtime-image
ARG CI_COMMIT_TAG
ARG CI_COMMIT_SHA
ENV CI_COMMIT_TAG=$CI_COMMIT_TAG
ENV CI_COMMIT_SHA=$CI_COMMIT_SHA

## add user jojo
RUN addgroup --system jojo && adduser --system --no-create-home --group jojo

## copy service/configs
COPY --chown=jojo:jojo ./service /opt/jojo/service/
COPY --chown=jojo:jojo ./tests /opt/jojo/tests/

## copy venv
COPY --chown=jojo:jojo --from=builder /opt/.venv /opt/.venv

## virtualenv
ENV VIRTUAL_ENV=/opt/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## switch to non-root user jojo
USER jojo
WORKDIR /opt/jojo

## run server
CMD ["python3", "-m" , "service"]
