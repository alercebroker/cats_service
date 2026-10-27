echo "Starting Cats Service"
# --preload loads the catalog indexes once, before forking, so the workers share them (see service/app.py).
# --max-requests recycles each worker after about 500 requests as a safety net against memory growth.
gunicorn --bind 0.0.0.0:5001 --workers 3 --preload --max-requests 500 --max-requests-jitter 50 wsgi:app
