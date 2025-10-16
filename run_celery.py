from dotenv import load_dotenv
import os

load_dotenv('.env.local')
os.system('celery -A config worker -l INFO -P eventlet')
# Для Celery Beat
os.system('celery -A config beat')
