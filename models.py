from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class my_movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String(80), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    fecha_de_estreno = db.Column(db.String(10), nullable=False)
