FROM python:3.7-alpine

RUN apk add gcc musl-dev bash
RUN pip install pylone

CMD ["python3"]
