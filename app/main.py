
from fastapi import FastAPI
import os
import psycopg2

app = FastAPI()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

@app.get("/")
def read_root():
    return {"message": "API FastAPI rodando com PostgreSQL via Docker Compose!"}

@app.get("/db-check")
def check_db_connection():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()
        cur.close()
        conn.close()
        return {"status": "Conectado ao banco!", "versao": version}
    except Exception as e:
        return {"status": "Erro de conexão", "detalhes": str(e)}
