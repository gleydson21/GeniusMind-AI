from flask import Flask, jsonify, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Carregar o modelo e o scaler
model = joblib.load('novo3_XGBC.pkl')  # Substitua pelo caminho correto do modelo
scaler = joblib.load('scaler.pkl')  # Substitua pelo caminho correto do scaler, se estiver usando

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ajuda')
def ajuda():
    return render_template('ajuda.html')

@app.route('/inserirdados')
def inserir_dados():
    return render_template('inserirdados.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Coleta e processa os dados do formulário
        features = [
            int(request.form['idade']),
            int(request.form['sexo']),
            int(request.form['escolaridade']),
            int(request.form['bolsa']),
            int(request.form['trabalho-adicional']),
            int(request.form['horas-estudadas']),
            int(request.form['impactos-atividades']),
            int(request.form['frequencia-aulas']),
            int(request.form['discussao']),
            int(request.form['media']),
            int(request.form['Id-Curso'])
        ]
        

        # Transforma os dados para o formato numpy array e aplica o scaler
        features_array = np.array([features])
        scaled_features = scaler.transform(features_array)  # Se estiver usando scaler

        # Realiza a predição com o modelo
        prediction = model.predict(scaled_features)

        # Retorna a predição como JSON
        return jsonify({'prediction': prediction.tolist()})
            

    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)