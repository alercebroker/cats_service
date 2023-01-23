echo "Starting Cats Service"
uvicorn --host 0.0.0.0 --port 5001 wsgi:app
