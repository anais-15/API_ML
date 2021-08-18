FROM python:3.8.5

COPY API /api
COPY linear_starbucks.joblib /linear_starbucks.joblib
COPY pkg_starbucks /pkg_starbucks
RUN pip install --upgrade pip
COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD uvicorn api.fast_api:app --host 0.0.0.0 --port $PORT
