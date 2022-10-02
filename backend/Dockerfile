FROM python:3.7-slim

WORKDIR /backend

COPY backend .

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["gunicorn", "app.wsgi:application", "--bind", "0:8000" ]
