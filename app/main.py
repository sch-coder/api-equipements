from fastapi import FastAPI
from app.database import engine
from app import models

# Crée les tables dans la base de données au démarrage
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Gestion Équipements Informatiques",
    description="Une API REST pour gérer un inventaire d'équipements informatiques",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de gestion d'équipements informatiques"}