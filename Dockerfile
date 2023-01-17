FROM python:3.7

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN cd catsHTM && pip install -e .

EXPOSE 5001
ENV DATA_PATH="/data"
ENV CATALOGS="TMASSxsc,AAVSO_VSX,AKARI,CRTS_per_var,FIRST,NVSS,ROSATfsc,SWIREz"
WORKDIR /app/scripts
CMD ["/bin/sh", "entrypoint.sh"]
