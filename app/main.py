from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, get_db
from app import models, schemas, crud

# Crée les tables au démarrage
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Gestion Équipements Informatiques",
    description="Une API REST pour gérer un inventaire d'équipements informatiques",
    version="1.0.0"
)

# GET / - Route d'accueil
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de gestion d'équipements informatiques"}

# POST /equipements - Créer un équipement
@app.post("/equipements", response_model=schemas.EquipementResponse)
def create_equipement(equipement: schemas.EquipementCreate, db: Session = Depends(get_db)):
    return crud.create_equipement(db=db, equipement=equipement)

# GET /equipements - Lire tous les équipements
@app.get("/equipements", response_model=list[schemas.EquipementResponse])
def get_equipements(db: Session = Depends(get_db)):
    return crud.get_equipements(db=db)

# GET /equipements/{id} - Lire un équipement par ID
@app.get("/equipements/{equipement_id}", response_model=schemas.EquipementResponse)
def get_equipement(equipement_id: int, db: Session = Depends(get_db)):
    db_equipement = crud.get_equipement(db=db, equipement_id=equipement_id)
    if db_equipement is None:
        raise HTTPException(status_code=404, detail="Équipement non trouvé")
    return db_equipement

# PUT /equipements/{id} - Modifier un équipement
@app.put("/equipements/{equipement_id}", response_model=schemas.EquipementResponse)
def update_equipement(equipement_id: int, equipement: schemas.EquipementCreate, db: Session = Depends(get_db)):
    db_equipement = crud.update_equipement(db=db, equipement_id=equipement_id, equipement=equipement)
    if db_equipement is None:
        raise HTTPException(status_code=404, detail="Équipement non trouvé")
    return db_equipement

# DELETE /equipements/{id} - Supprimer un équipement
@app.delete("/equipements/{equipement_id}", response_model=schemas.EquipementResponse)
def delete_equipement(equipement_id: int, db: Session = Depends(get_db)):
    db_equipement = crud.delete_equipement(db=db, equipement_id=equipement_id)
    if db_equipement is None:
        raise HTTPException(status_code=404, detail="Équipement non trouvé")
    return db_equipement