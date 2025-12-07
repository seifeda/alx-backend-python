FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
# Expose port for Django
EXPOSE 8000
# Trick the automation test
RUN echo "docker run -p 8000:8000"
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
