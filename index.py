# -*- coding: utf-8 -*-
from flask import request, Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    karts = [{'name': 'Kartodromo Aldeia da Serra',
              'lat': -23.508324, 'long': -46.932360},
             {'name': 'Kartodromo Granja Viana',
              'lat': -23.606159, 'long': -46.835993},
             {'name': 'SP diversoes',
              'lat': -23.572050, 'long': -46.712519},
             {'name': 'Speedland',
              'lat': -23.532239, 'long': -46.585014},
             {'name': 'Kartodromo Ayrton Senna',
              'lat': -23.703668, 'long': -46.693728}]
    if request.method == 'POST':
        return "POST"
    else:
        return jsonify(karts)
