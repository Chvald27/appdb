import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", 
        "postgresql://postgres:DevOps2024*@localhost:5432/webappdb"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = "filesystem"


