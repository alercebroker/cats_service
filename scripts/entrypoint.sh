echo "Starting Cats Service"
gunicorn --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:5001 wsgi:app
