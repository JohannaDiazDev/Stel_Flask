import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL","postgresql://postgres:Chita701*@localhost:5432/db_stel")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecreto'
    