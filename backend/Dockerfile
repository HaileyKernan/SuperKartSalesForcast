FROM python:3.9-slim

WORKDIR /app
COPY . .

# Install your actual app dependencies
RUN pip install --no-cache-dir -r requirements.txt



CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:7860", "app:sales_forcast_api"]
