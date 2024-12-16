FROM python:3.12
WORKDIR /tests
COPY requirements.txt /tests/requirements.txt
COPY tests.py /tests/tests.py
RUN pip install --no-cache-dir -r requirements.txt