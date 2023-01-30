FROM python:3.10.6

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN cd catsHTM && pip install -e .

EXPOSE 5001
WORKDIR /app/scripts
CMD ["/bin/sh", "entrypoint.sh"]
