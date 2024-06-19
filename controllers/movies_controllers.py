from flask_restful import Resource, reqparse, fields, marshal_with
from models import db, my_movies
from datetime import datetime

# Función para formatear la fecha como string
def format_date(date):
    return date.strftime('%Y-%m-%d') if date else None

# Definir un campo de serialización para la película
movie_fields = {
    'id': fields.Integer,
    'autor': fields.String,
    'descripcion': fields.String,
    'fecha_de_estreno': fields.String(attribute=lambda x: format_date(x.fecha_de_estreno))
}

class MoviesController(Resource):
    @marshal_with(movie_fields)
    def get(self, id=None):
        if id:
            movie = my_movies.query.get(id)
            if movie:
                return movie, 200
            return {"message": "Movie no encontrada"}, 404
        movies = my_movies.query.all()
        return movies, 200

    @marshal_with(movie_fields)
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("autor", type=str, required=True, help="Autor no puede estar en blanco!")
        parser.add_argument("descripcion", type=str, required=True, help="Descripcion no puede estar en blanco!")
        parser.add_argument("fecha_de_estreno", type=str, required=True, help="Fecha no puede estar en blanco!")
        data = parser.parse_args()

        # Convertir la cadena de fecha a objeto datetime
        fecha_de_estreno = datetime.strptime(data["fecha_de_estreno"], '%Y-%m-%d')

        new_movie = my_movies(autor=data["autor"], descripcion=data["descripcion"], fecha_de_estreno=fecha_de_estreno)
        db.session.add(new_movie)
        db.session.commit()

        return new_movie, 201  # Devolver el objeto serializado

    @marshal_with(movie_fields)
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("autor", type=str)
        parser.add_argument("descripcion", type=str)
        parser.add_argument("fecha_de_estreno", type=str)
        data = parser.parse_args()

        movie = my_movies.query.get(id)
        if not movie:
            return {"message": "Movie no encontrada"}, 404  # Devolver mensaje de error si no se encuentra la película

        if data["autor"]:
            movie.autor = data["autor"]
        if data["descripcion"]:
            movie.descripcion = data["descripcion"]
        if data["fecha_de_estreno"]:
            # Convertir la cadena de fecha a objeto datetime
            movie.fecha_de_estreno = datetime.strptime(data["fecha_de_estreno"], '%Y-%m-%d')

        db.session.commit()
        return movie, 200  # Devolver el objeto serializado de la película actualizada

    def delete(self, id):
        movie = my_movies.query.get(id)
        if not movie:
            return {"message": "Movie no encontrada"}, 404

        db.session.delete(movie)
        db.session.commit()
        return {"message": "Movie eliminada"}, 200
