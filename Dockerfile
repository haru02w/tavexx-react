FROM python:3.11.8-bookworm

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV /venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY . .

RUN pip install -U pip poetry && \
  python3 -m venv $VIRTUAL_ENV && \
  poetry install --no-interaction --no-ansi --without dev

ENTRYPOINT [ "./scripts/dev-server.sh" ]
EXPOSE 8000
