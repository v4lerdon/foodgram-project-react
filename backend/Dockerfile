FROM python:3.7-slim

WORKDIR /backend

COPY . .

RUN pip install --upgrade pip && pip install -r backend/requirements.txt

CMD ["gunicorn", "app.wsgi:application", "--bind", "0:8000" ]
