from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name":self.name,
            "surname":self.surname,
            "email": self.email
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'character'
    # Here we define db.Columns for the table address.
    # Notice that each db.Column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    character_name = db.Column(db.String(250))
    character_birth_year = db.Column(db.Integer)
    hair_color = db.Column(db.String(250))
    height = db.Column(db.Integer)
    gender = db.Column(db.String(250))
    mass = db.Column(db.Integer)


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
            "mass": self.mass
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
            }

# class Vehicles(db.Model):
#     __tablename__ = 'vehicles'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = db.Column(db.Integer, primary_key=True)
#     planet_name = db.Column(db.String(250))
#     climate = db.Column(db.String(250))
#     population = db.Column(db.Integer)
#     orbital_period = db.Column(db.Integer)
#     diameter = db.Column(db.Integer)