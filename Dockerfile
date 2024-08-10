########## build image ##########
FROM python:3.12.5-bullseye AS builder

## add and install requirements
RUN pip install poetry
WORKDIR /opt
COPY ./pyproject.toml .
COPY ./poetry.lock .
RUN poetry config virtualenvs.in-project true
RUN poetry install

########## service image ##########
FROM python:3.12.5-slim-bullseye AS runtime-image

## add user sbr
RUN addgroup --system sbr && adduser --system --no-create-home --group sbr

## copy service/configs
COPY --chown=sbr:sbr ./service /opt/sbr/service/

## copy venv
COPY --chown=sbr:sbr --from=builder /opt/.venv /opt/.venv

## virtualenv
ENV VIRTUAL_ENV=/opt/.venv
#RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

## switch to non-root user sbr
USER sbr
WORKDIR /opt/sbr

## run server
CMD ["python3", "-m" , "service"]
