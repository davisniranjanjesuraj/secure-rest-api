import os

class Config:
    SECRET_KEY = "super-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///secure_api.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "jwt-secret-key"
    JWT_IDENTITY_CLAIM = "sub"
    JWT_ACCESS_TOKEN_EXPIRES = 3600
