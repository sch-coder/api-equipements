from fastapi import FastAPI

# On crée une instance de l'application FastAPI
app = FastAPI(
    title="API Gestion Équipements Informatiques",
    description="Une API REST pour gérer un inventaire d'équipements informatiques",
    version="1.0.0"
)

# Notre première route
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de gestion d'équipements informatiques"}