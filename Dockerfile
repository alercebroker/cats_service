FROM python:3.10.6

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN cd catsHTM && pip install -e .
EXPOSE 5001
ENV CATALOGS="TMASSxsc,AAVSO_VSX,AKARI,CRTS_per_var,FIRST,NVSS,ROSATfsc,SWIREz"
ENV DATA_PATH="/data"
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5001", "src:app"]
