FROM python:3.9-alpine3.13

WORKDIR /app/
COPY ./app /app
# COPY ./requirements.txt /app


ENV PYTHONPATH=/app \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  INSTALL_DEV=true

RUN apk add --no-cache --virtual .build-deps gcc \
        libc-dev make build-base openssl-dev \
        libffi-dev libxml2-dev libxslt-dev postgresql-dev \
        musl-dev cargo jpeg-dev zlib-dev libjpeg \
      && apk add netcat-openbsd curl  postgresql-client

# RUN apk add netcat-openbsd curl

ADD requirements.txt .

RUN pip install -r requirements.txt


RUN apk add tzdata
ENV TZ=Asia/Jakarta

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload", "--port=80"]