from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# L'adresse de notre base de données SQLite
DATABASE_URL = "sqlite:///./equipements.db"

# Le moteur de connexion à la base de données
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# La session = la connexion active avec la base de données
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# La classe de base pour nos modèles
Base = declarative_base()

# Fonction pour obtenir une session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()