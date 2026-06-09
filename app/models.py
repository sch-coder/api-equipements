from sqlalchemy import Column, Integer, String
from app.database import Base

class Equipement(Base):
    __tablename__ = "equipements"

    id      = Column(Integer, primary_key=True, index=True)
    nom     = Column(String, nullable=False)
    type    = Column(String, nullable=False)
    service = Column(String, nullable=False)
    etat    = Column(String, nullable=False)