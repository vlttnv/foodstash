import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    quantity_type = db.Column(db.String(80), nullable=False)
    portions = db.Column(db.Integer, nullable=False)
    food_type = db.Column(db.String(80))


@app.route('/')
def home():
    i = Ingredient(quantity=1, quantity_type='a', portions=1)
    db.session.add(i)
    db.session.commit()
    # cur = db.execute('select title, text from entries order by id desc')
    # entries = cur.fetchall()
    return 'hello'


@app.route('/add_ingredient', methods=['POST'])
def add_ingredient():
    json_req = request.json
    ingredient = Ingredient(
        name=json_req['name'],
        quantity=int(json_req['quantity']),
        quantity_type=json_req['quantity_type'],
        portions=int(json_req['portions']),
        food_type=json_req.get('food_type'),
    )
    db.session.add(ingredient)
    db.session.commit()
    return 'ingredient added'


@app.route('/subtract_ingredient/<int:ingredient_id>', methods=['POST'])
def subtract_ingredient(ingredient_id):
    return 'ingredient subtracted'


@app.route('/topup_ingredient/<int:ingredient_id>', methods=['POST'])
def topup_ingredient(ingredient_id):
    return 'ingredient topped up'


@app.route('/get_ingredients', methods=['GET'])
def get_ingredients():
    return 'some ingredients'
