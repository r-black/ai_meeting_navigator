FROM python:3.11-slim-bookworm AS compile-image

ENV \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1



RUN apt-get update && apt-get --no-install-recommends install -y build-essential git openssh-client \
ffmpeg build-essential git curl libopenblas-dev apt-transport-https ca-certificates gnupg && apt-get clean && rm -rf /var/lib/apt/lists/*

# Установка рабочей директории
WORKDIR /app

# Установка Python-зависимостей
COPY backend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY backend/ ./
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]