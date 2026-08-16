FROM python:3.12.13-slim

WORKDIR /app
COPY . .

# Install OS networking tools so Gunicorn can bind to ports
RUN apt-get update && apt-get install -y iproute2 iputils-ping procps

# Install packaging tools including pkg_resources
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel pkg_resources

# Install your actual app dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:7860", "app:sales_forcast_api"]
