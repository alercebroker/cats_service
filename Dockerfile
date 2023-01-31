FROM python:3.10.6

RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
RUN cd catsHTM && pip install -e .
EXPOSE 5001
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "5001", "--forwarded-allow-ips", "*", "src:app"]
