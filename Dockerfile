FROM python:3.12
WORKDIR /app
COPY requirements.txt /app/requirements.txt
copy /app /app
RUN pip install --no-cache-dir -r requirements.txt