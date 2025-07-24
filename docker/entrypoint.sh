#!/bin/bash
set -e

if [ "$1" = "worker" ]; then
  echo "[+] Starting Celery worker"
  exec celery -A app.celery_app worker --loglevel=info
else
  echo "[+] Starting FastAPI app"
  exec uvicorn app.main:app --host 0.0.0.0 --port 8000
fi
