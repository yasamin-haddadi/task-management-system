FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1 \
    PYTHONDONTWRITEBYTECODE  1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev \ 
    gcc \
    python3-dev \    
    && rm -rf /var/lib/apt/lists/*          

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

ENTRYPOINT ["sh", "entrypoint.sh"]

CMD [ "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000" ]


