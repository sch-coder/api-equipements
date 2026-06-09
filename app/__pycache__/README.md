# API REST - Gestion d'Équipements Informatiques

Une API REST professionnelle pour gérer un inventaire d'équipements informatiques.

## Technologies utilisées
- **Python** - Langage de programmation
- **FastAPI** - Framework web moderne et rapide
- **SQLite** - Base de données légère
- **SQLAlchemy** - ORM pour la base de données
- **Pydantic** - Validation des données
- **Swagger/OpenAPI** - Documentation interactive

## Fonctionnalités
- ✅ Créer un équipement
- ✅ Lister tous les équipements
- ✅ Consulter un équipement par ID
- ✅ Modifier un équipement
- ✅ Supprimer un équipement

## Installation

### 1. Cloner le projet
```bash
git clone https://github.com/TON_USERNAME/api-equipements.git
cd api-equipements
```

### 2. Créer et activer l'environnement virtuel
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Lancer l'API
```bash
uvicorn app.main:app --reload --port 8080
```

### 5. Accéder à la documentation Swagger