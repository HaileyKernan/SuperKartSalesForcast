FROM python:3.12.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-catch-fir --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:7860", "app:sales_forcast_api"]
