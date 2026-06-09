from sqlalchemy.orm import Session
from app import models, schemas

# CREATE - Créer un équipement
def create_equipement(db: Session, equipement: schemas.EquipementCreate):
    db_equipement = models.Equipement(
        nom=equipement.nom,
        type=equipement.type,
        service=equipement.service,
        etat=equipement.etat
    )
    db.add(db_equipement)
    db.commit()
    db.refresh(db_equipement)
    return db_equipement

# READ ALL - Lire tous les équipements
def get_equipements(db: Session):
    return db.query(models.Equipement).all()

# READ ONE - Lire un équipement par ID
def get_equipement(db: Session, equipement_id: int):
    return db.query(models.Equipement).filter(
        models.Equipement.id == equipement_id
    ).first()

# UPDATE - Modifier un équipement
def update_equipement(db: Session, equipement_id: int, equipement: schemas.EquipementCreate):
    db_equipement = db.query(models.Equipement).filter(
        models.Equipement.id == equipement_id
    ).first()
    if db_equipement:
        db_equipement.nom     = equipement.nom
        db_equipement.type    = equipement.type
        db_equipement.service = equipement.service
        db_equipement.etat    = equipement.etat
        db.commit()
        db.refresh(db_equipement)
    return db_equipement

# DELETE - Supprimer un équipement
def delete_equipement(db: Session, equipement_id: int):
    db_equipement = db.query(models.Equipement).filter(
        models.Equipement.id == equipement_id
    ).first()
    if db_equipement:
        db.delete(db_equipement)
        db.commit()
    return db_equipement