echo "Starting Cats Service"
gunicorn --bind 0.0.0.0:5001 wsgi:app
