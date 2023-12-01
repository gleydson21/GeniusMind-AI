from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/')
def index():
    return jsonify({'message': 'Tabacudo!'})

@api.route('/hello/<name>')
def hello(name):
    return jsonify({'message': f'Olá, {name}!'})