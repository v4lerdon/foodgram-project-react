FROM python:3.7-slim

RUN mkdir /backend

COPY /backend /backend

WORKDIR /backend

RUN pip install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "app.wsgi:application", "--bind", "0:8000" ]
