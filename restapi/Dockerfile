FROM python:3.6.6

RUN mkdir -p /usr/src/app/toy_application
WORKDIR /usr/src/app/toy_application
COPY src/ /usr/src/app/toy_application/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--workers=1", "--threads=5", "--timeout=120", "--bind=0.0.0.0:8000", "--forwarded-allow-ips='*'", "wsgi:app"]

EXPOSE 8000

