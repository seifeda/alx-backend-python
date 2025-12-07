FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
docker run -p 8000:8000 ...messaging_app
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


