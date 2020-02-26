"""
Wujiang API
"""
import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from flask_marshmallow import Marshmallow

# init app
app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(DATA_DIR, 'wujiang_index.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# wujiang Class/Model
class Wujiang(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    level = db.Column(db.Integer)
    profession = db.Column(db.String(100))
    attack = db.Column(db.Float)
    defense = db.Column(db.Float)
    speed = db.Column(db.Float)
    ranging = db.Column(db.Float)
    mag = db.Column(db.Float)
    spells = db.Column(db.String(500))
    specs = db.Column(db.String(500))
    scepter = db.Column(db.String(500))

    def __init__(self, name, level, profession, attack, defense, speed, ranging, mag, spells, specs, scepter):
        self.name = name
        self.level = level
        self.profession = profession
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.ranging = ranging
        self.mag = mag
        self.spells = spells
        self.specs = specs
        self.scepter = scepter


# wujiang Schema
class WujiangSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'level', 'profession', 'attack', 'defense', 'speed', 'ranging', 'mag', 'spells', 'specs', 'scepter')


# init schema
wujiang_schema = WujiangSchema()
wujiangs_schema = WujiangSchema(many=True)


# Get Single Wujiang
@app.route('/wujiang/<id>', methods=['GET'])
def get_product(id):
    wujiang = Wujiang.query.get(id)
    return wujiang_schema.jsonify(wujiang)


# get all Product
@app.route('/wujiang', methods=['GET'])
def get_wujiangs():
    all_wujiangs = Wujiang.query.all()
    name = request.args.get("name", "")
    # result = SQLAlchemy.session.query(Wujiang).get({"name": name})
    result = Wujiang.query.filter_by(name=name)
    print(result)
    # result = wujiangs_schema.dump(all_wujiangs)
    return wujiangs_schema.jsonify(result)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
