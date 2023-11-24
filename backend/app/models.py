# backend/app/models.py

from backend.app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    senha = db.Column(db.String(100))

    def __repr__(self):
        return f"<Usuario {self.nome}>"