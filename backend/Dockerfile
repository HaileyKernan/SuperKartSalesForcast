FROM python:3.12.13

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir --force-reinstall setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:7860", "app:sales_forcast_api"]
