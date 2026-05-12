FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

COPY skills/million-novel-writer/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY skills/million-novel-writer/scripts /app/scripts
COPY skills/million-novel-writer/templates /app/templates
COPY skills/million-novel-writer/SKILL.md /app/SKILL.md
COPY README.md /app/README.md

EXPOSE 8080

CMD ["uvicorn", "api_server:app", "--app-dir", "/app/scripts", "--host", "0.0.0.0", "--port", "8080"]
