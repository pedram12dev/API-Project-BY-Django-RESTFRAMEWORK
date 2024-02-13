FROM python:alpine3.19
LABEL maintainer = "pedram najafi"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt

COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN echo -e "http://nl.alpinelinux.org/alpine/v3.19/main\nhttp://nl.alpinelinux.org/alpine/v3.19/community" > /etc/apk/repositories
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user
