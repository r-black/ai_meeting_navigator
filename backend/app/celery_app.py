from celery import Celery
import os


celery_app = Celery(
    "worker",
    broker=os.getenv("REDIS_URL", "redis://redis:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://redis:6379/0")
)

celery_app.autodiscover_tasks(['app']) 