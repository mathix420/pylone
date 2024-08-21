FROM python:3.12-alpine

RUN apk add gcc musl-dev bash

COPY . /src

RUN cd /src && pip install .
RUN rm -rf /src

CMD ["python3"]
