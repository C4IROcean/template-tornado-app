FROM python:3.9-alpine

ENV PYTHONFAULTHANDLER=1
ENV PYTHONBUFFERED=1

RUN apk --no-cache add curl
RUN apk --no-cache add gcc
RUN apk --no-cache add musl-dev
RUN apk --no-cache add libffi-dev

RUN pip install poetry

WORKDIR /src
COPY . .

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

EXPOSE 5000

CMD ["poetry", "run", "python", "-m", "odp.app.myapp"]