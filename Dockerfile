FROM python:3.8.12

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

RUN pip3 install poetry

WORKDIR $PYSETUP_PATH

COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install


WORKDIR /app
COPY . .

EXPOSE 8000
RUN chmod +x /app/entrypoint.sh
CMD [ "/app/entrypoint.sh" ]