FROM python:3.7


WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt && pip install gunicorn && cd catsHTM && pip install -e .

EXPOSE 5000
ENV DATA_PATH="/usr/local/catalogsHTM/"
WORKDIR /app/scripts
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "wsgi:app"]
