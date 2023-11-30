from flask import Blueprint, jsonify, request
from app.prediction import predict_student

api = Blueprint('api', __name__)

@api.route('/predict', methods=['POST'])
def make_prediction():
    form_data = request.json
    
    # Chama a função predict_student para obter o resultado da previsão
    result = predict_student(form_data)
    
    return jsonify({'result': result})