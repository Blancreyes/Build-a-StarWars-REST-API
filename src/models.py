from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    favorites = db.relationship("Favorites", backref="user", lazy=True)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "surname":self.surname,
            "email": self.email,
            "favorites": self.favorites
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))
    character_birth_year = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    height = db.Column(db.Integer)
    gender = db.Column(db.String(250))
    mass = db.Column(db.Integer)
    favorites = db.relationship("Favorites", backref="character", lazy=True)


    def __repr__(self):
        return '<Character %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.character_name,
            "birth_year":self.character_birth_year,
            "hair_color": self.hair_color,
            "height":self.height,
            "gender":self.gender,
            "mass": self.mass,
            "favorites": self.favorites
        }

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    planet_name = db.Column(db.String(250))
    climate = db.Column(db.String(250))
    population = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    favorites = db.relationship("Favorites", backref='planets', lazy=True)

    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.planet_name,
            "climate":self.climate,
            "population": self.population,
            "orbital_period":self.orbital_period,
            "diameter":self.diameter,
            "favorites": self.favorites
            }

class Favorites(db.Model):
    __tablename__ = 'favorites'
    # # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    planets_id = db.Column(db.Integer, db.ForeignKey("planets.id") , nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id") , nullable=False)

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
                "id":self.id,
                "user":self.user_id,
                "planets":self.planets_id,
                "character":self.character_id
            }
