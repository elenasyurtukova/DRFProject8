import os

from dotenv import load_dotenv

load_dotenv(".env.local")
os.system("celery -A config worker -l INFO -P eventlet")
# Для Celery Beat
os.system("celery -A config beat")
