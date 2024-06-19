from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from controllers.movies_controllers import MoviesController

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/my_collections'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api = Api(app)
api.add_resource(MoviesController, '/movies', '/movies/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
