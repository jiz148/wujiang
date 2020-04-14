"""
Wujiang API
"""
import os

from flask import abort, Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import exc


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
    type = db.Column(db.String(100))
    race = db.Column(db.String(100))
    attack = db.Column(db.Float)
    defense = db.Column(db.Float)
    speed = db.Column(db.Float)
    ranging = db.Column(db.Float)
    mag = db.Column(db.Float)
    spells = db.Column(db.String(500))
    specs = db.Column(db.String(500))

    def __init__(self, name, level, profession, type, race, attack, defense, speed, ranging, mag, spells, specs):
        self.name = name
        self.level = level
        self.profession = profession
        self.type = type
        self.race = race
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.ranging = ranging
        self.mag = mag
        self.spells = spells
        self.specs = specs


# wujiang Schema
class WujiangSchema(ma.Schema):
    class Meta:
        fields = (
            'id',
            'name',
            'level',
            'profession',
            'type',
            'race',
            'attack',
            'defense',
            'speed',
            'ranging',
            'mag',
            'spells',
            'specs',
        )


# init schema
wujiang_schema = WujiangSchema()
wujiangs_schema = WujiangSchema(many=True)


# create a wujiang
@app.route('/wujiang', methods=['POST'])
def add_wujiang():
    attrs = _get_all_attrs()

    new_wujiang = Wujiang(
        attrs[0],
        attrs[1],
        attrs[2],
        attrs[3],
        attrs[4],
        attrs[5],
        attrs[6],
        attrs[7],
        attrs[8],
        attrs[9],
        attrs[10],
        attrs[11])

    db.session.add(new_wujiang)
    db.session.commit()

    return wujiang_schema.jsonify(new_wujiang)


# Get Single Wujiang
@app.route('/wujiang/<id>', methods=['GET'])
def get_wujiang(id):
    wujiang = Wujiang.query.get_or_404(id)
    return wujiang_schema.jsonify(wujiang)


# get all Wujiangs
@app.route('/wujiang/', methods=['GET'])
def get_wujiangs():
    result = Wujiang.query
    arg_keys, arg_values = request.args.keys(), request.args.values()
    for key, value in zip(arg_keys, arg_values):
        try:
            if key == 'spells':
                search = '%{}%'.format(value)
                result = result.filter(Wujiang.spells.like(search))
            elif key == 'specs':
                search = '%{}%'.format(value)
                result = result.filter(Wujiang.specs.like(search))
            else:
                result = result.filter_by(**{key: value})
        except exc.InvalidRequestError:
            abort(400)
    # print('result!!!!!!!!! is !!!!', result.all())
    return wujiangs_schema.jsonify(result) if result.all() else abort(404)


# update a wujiang
@app.route('/wujiang/<id>', methods=['PUT'])
def update_wujiang(id):
    updating_wujiang = Wujiang.query.get_or_404(id)

    attrs = _get_all_attrs()

    # Update if not None
    updated_wujiang = _update_all_attrs(updating_wujiang, attrs)

    db.session.commit()

    return wujiang_schema.jsonify(updated_wujiang)


# Delete Wujiang
@app.route('/wujiang/<id>', methods=['DELETE'])
def delete_wujiang(id):
    deleting_wujiang = Wujiang.query.get_or_404(id)
    db.session.delete(deleting_wujiang)
    db.session.commit()

    return wujiang_schema.jsonify(deleting_wujiang)


def _get_all_attrs():
    """
    Gets all the attributes of wujiang from asdf
    @return: <Tuple> Tuple of attributes
    """
    name = request.json.get('name')
    level = request.json.get('level')
    profession = request.json.get('profession')
    type = request.json.get('type')
    race = request.json.get('race')
    attack = request.json.get('attack')
    defense = request.json.get('defense')
    speed = request.json.get('speed')
    ranging = request.json.get('ranging')
    mag = request.json.get('mag')
    spells = request.json.get('spells')
    specs = request.json.get('specs')

    return name, level, profession, type, race, attack, defense, speed, ranging, mag, spells, specs


def _update_all_attrs(wujiang, attrs):
    """
    Updates wujiang with tuple of new attributes only if the attribute is not None
    @param wujiang: updating wujiang
    @param attrs: new attrs
    @return: updated wujiang
    """
    if attrs[0]:
        wujiang.name = attrs[0]
    if attrs[1]:
        wujiang.level = attrs[1]
    if attrs[2]:
        wujiang.profession = attrs[2]
    if attrs[3]:
        wujiang.type = attrs[3]
    if attrs[4]:
        wujiang.race = attrs[4]
    if attrs[5]:
        wujiang.attack = attrs[5]
    if attrs[6]:
        wujiang.defense = attrs[6]
    if attrs[7]:
        wujiang.speed = attrs[7]
    if attrs[8]:
        wujiang.ranging = attrs[8]
    if attrs[9]:
        wujiang.mag = attrs[9]
    if attrs[10]:
        wujiang.spells = attrs[10]
    if attrs[11]:
        wujiang.specs = attrs[11]

    return wujiang


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
