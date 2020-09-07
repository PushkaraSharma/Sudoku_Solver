FROM python:3.8.0-slim
COPY . /app
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
WORKDIR app
RUN pip install --user --default-timeout=100 -r requirements.txt
ENTRYPOINT uvicorn main:app --reload --host 0.0.0.0 --port 5000
