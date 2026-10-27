# Pinned to what the 1.2.0 image was built with, so a rebuild changes only the code.
FROM python:3.7.16-bullseye

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN pip install gunicorn==20.1.0 && cd catsHTM && pip install -e .

EXPOSE 5001
ENV DATA_PATH="/usr/local/catalogsHTM/"
WORKDIR /app/scripts
CMD ["/bin/sh", "entrypoint.sh"]
