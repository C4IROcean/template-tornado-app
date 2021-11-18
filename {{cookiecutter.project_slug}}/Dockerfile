FROM python:{{cookiecutter.python_version}}-alpine

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

CMD ["poetry", "run", "python", "-m", "odp.app.{{cookiecutter.project_slug}}", "--port=5000", "--host=0.0.0.0"]