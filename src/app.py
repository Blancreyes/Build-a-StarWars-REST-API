"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Character, Planets, Favorites


app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['POST'])
def create_user():
    #se debe pasar la información a formato json
    request_body=request.json

    # se verifica si el usuario ya existe
    user_info_query=User.query.filter_by(email=request_body["email"]).first()

    #Condicional, para crear el usuario si este no existe (verificado en query anterior)
    if user_info_query is None:
        user = User(
            name=request_body["name"],
            surname=request_body["surname"],
            email=request_body["email"], 
            password=request_body["password"])
        db.session.add(user)
        db.session.commit()
        response_body = {
            "msg": "Usuario creado correctamente", 
        }
        return jsonify(response_body), 200
    
    else: 
        return jsonify("El usuario ya existe"), 400
        
@app.route('/user', methods=['GET'])
def all_users_info():
    #Query para regresar la info de todos los user
    users_query=User.query.all()
    result=list(map(lambda item: item.serialize(), users_query))
    
    response_body = {
        "msg": "OK",
        "result":result
    }

    return jsonify(response_body), 200

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_info(user_id):

    #Query para regresar la info de user especifico
    user_info_query = User.query.filter_by(id=user_id).first()
        
    response_body = {
        "msg": "OK",
        "result":user_info_query.serialize()
    }

    return jsonify(response_body), 200

#Endpoints de Character
@app.route('/character', methods=['POST'])
def create_character():
    #se debe pasar la información a formato json
    request_body=request.json

    # se verifica si el usuario ya existe
    character_info_query=Character.query.filter_by(character_name=request_body["name"]).first()

    #Condicional, para crear el usuario si este no existe (verificado en query anterior)
    if character_info_query is None:
        character = Character(
            character_name=request_body["name"],
            character_birth_year=request_body["birth_year"],
            hair_color=request_body["hair_color"], 
            height=request_body["height"],
            mass=request_body["mass"],
            gender=request_body["gender"]
            )
        db.session.add(character)
        db.session.commit()
        response_body = {
            "msg": "Character successfully created", 
        }
        return jsonify(response_body), 200
    
    else: 
        return jsonify("This Character already exists"), 400

@app.route('/character', methods=['GET'])
def all_characters_info():
    #Query para regresar la info de todos los characters
    characters_query=Character.query.all()
    result=list(map(lambda item: item.serialize(), characters_query))
    
    response_body = {
        "msg": "OK",
        "result":result
    }

    return jsonify(response_body), 200

@app.route('/character/<int:character_id>', methods=['GET'])
def get_character_info(character_id):

    #Query para regresar la info de character especifico
    character_info_query = Character.query.filter_by(id=character_id).first()
        
    response_body = {
        "msg": "OK",
        "result":character_info_query.serialize()
    }

    return jsonify(response_body), 200

#Endpoints de Planets
@app.route('/planets', methods=['POST'])
def create_planet():
    request_body=request.json

    planet_info_query=Planets.query.filter_by(planet_name=request_body["name"]).first()

    if planet_info_query is None:
        planets = Planets(
            planet_name=request_body["name"],
            climate=request_body['climate'],
            population=request_body['population'] ,
            orbital_period=request_body['orbital_period'],
            diameter=request_body['diameter'],
            )
        db.session.add(planets)
        db.session.commit()
        response_body = {
            "msg": "Planet successfully created", 
        }
        return jsonify(response_body), 200
    else: 
        return jsonify("This Planet already exists"), 400


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet_info(planet_id):
    planet_info_query=Planets.query.filter_by(id=planet_id).first()

    response_body={
        "msg":"OK",
        "result":planet_info_query.serialize()
    }

    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def all_planet_info():
    #Query para regresar la info de todos los characters
    planets_query=Planets.query.all()
    result=list(map(lambda item: item.serialize(), planets_query))
    
    response_body = {
        "msg": "OK",
        "result":result
    }

    return jsonify(response_body), 200

@app.route('/favorites/planets/<int:planets_id>', methods=['POST'])
def create_favorite(planets_id):
    
    request_body=request.json

    # if favorite_info_query is None:
    favorites = Favorites(
        user_id=request_body["user"],
        planets_id=planets_id
        )
    db.session.add(favorites)
    db.session.commit()
    response_body = {
        "msg": "Favorite added", 
    }
    return jsonify(response_body), 200
    # else: 
    #     return jsonify("This Favorite already exists"), 400

@app.route('/favorites/character/<int:character_id>', methods=['POST'])
def create_character_favorite(character_id):
    
    request_body=request.json
    # favorites_info_query=Favorites.query.filter_by(user=request_body["user"]).first()

    # if favorite_info_query is None:
    favorites = Favorites(
        user_id=request_body["user"],
        character_id=character_id
        )
    db.session.add(favorites)
    db.session.commit()
    response_body = {
        "msg": "Favorite added", 
    }
    return jsonify(response_body), 200

@app.route('/favorites/planets/<int:planets_id>', methods=['DELETE'])
def delete_planets_favorite(planets_id):
    
    request_body=request.json
    # favorites_info_query=Favorites.query.filter_by(user=request_body["user"]).first()

    favorite_planet_query=Favorites.query.filter_by(user_id=request_body["user"], planets_id=planets_id).first()
    

    # if favorite_info_query is None:
    db.session.delete(favorite_planet_query)
    db.session.commit()
    response_body = {
        "msg": "Favorite deleted", 
    }
    return jsonify(response_body), 200


@app.route('/favorites/character/<int:character_id>', methods=['DELETE'])
def delete_character_favorite(character_id):
    
    request_body=request.json
    # favorites_info_query=Favorites.query.filter_by(user=request_body["user"]).first()

    favorite_character_query=Favorites.query.filter_by(user_id=request_body["user"],id=character_id).first()
    

    # if favorite_info_query is None:
    db.session.delete(favorite_character_query)
    db.session.commit()
    response_body = {
        "msg": "Favorite deleted", 
    }
    return jsonify(response_body), 200


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
