
# Etapa 1: Build (instala dependências)
FROM python:3.12-alpine AS builder

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Etapa 2: Runtime (imagem leve para execução)
FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY app /app

ENV PYTHONUNBUFFERED=1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
