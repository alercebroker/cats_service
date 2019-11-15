FROM python:3.7

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN pip install gunicorn && cd catsHTM && pip install -e .

EXPOSE 5001
ENV DATA_PATH="/usr/local/catalogsHTM/"
ENV APP_WORKERS=4
WORKDIR /app/scripts
CMD ["/bin/sh", "entrypoint.sh"]
