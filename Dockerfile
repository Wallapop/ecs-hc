FROM python:3.7-alpine

COPY script.py health.sh /var/

EXPOSE 8000

ENTRYPOINT ["/var/script.py"]
