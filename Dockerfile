# ========================
# Etapa 1: Build (instala dependências)
# ========================
FROM python:3.12-alpine AS builder

WORKDIR /app

# Instala dependências do sistema necessárias para psycopg2
RUN apk add --no-cache build-base libpq-dev

# Copia apenas requirements para aproveitar cache do Docker
COPY app/requirements.txt .

# Instala dependências em um diretório temporário
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ========================
# Etapa 2: Runtime (imagem leve)
# ========================
FROM python:3.12-alpine

WORKDIR /app

# Instala apenas bibliotecas necessárias para execução (sem compilar)
RUN apk add --no-cache libpq

# Copia as libs já instaladas do builder
COPY --from=builder /install /usr/local

# Copia código da aplicação
COPY app /app

# Copia variáveis de ambiente (opcional)
COPY .env /app/.env

# Evita buffering de logs
ENV PYTHONUNBUFFERED=1

# Expõe a porta usada pelo FastAPI
EXPOSE 8000

# Comando padrão de inicialização
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
