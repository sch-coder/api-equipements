from pydantic import BaseModel

# Schéma de base avec les champs communs
class EquipementBase(BaseModel):
    nom: str
    type: str
    service: str
    etat: str

# Schéma pour CRÉER un équipement (sans id)
class EquipementCreate(EquipementBase):
    pass

# Schéma pour LIRE un équipement (avec id)
class EquipementResponse(EquipementBase):
    id: int

    class Config:
        from_attributes = True