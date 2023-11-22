FROM python:3.8-slim

WORKDIR /app
COPY src/main /app/src/main/
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH "${PYTHONPATH}:/app"
EXPOSE 80


CMD ["python", "src/main/main_application.py"]
