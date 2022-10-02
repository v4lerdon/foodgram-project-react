FROM python:3.7-slim

RUN mkdir /backend

WORKDIR /backend

COPY . .

RUN pip3 install -r /backend/requirements.txt --no-cache-dir

CMD ["gunicorn", "app.wsgi:application", "--bind", "0:8000" ]
