#!/bin/sh
set -e

if [ "$1" = "web" ]; then
    alembic upgrade head
    exec uvicorn app.app:app --host 0.0.0.0 --port 8000
elif [ "$1" = "worker" ]; then
    exec celery -A app.app.celery worker --loglevel=info
else
    exec "$@"
fi
