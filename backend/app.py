from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inserir_dados')
def inserir_dados():
    return render_template('inserirdados.html')



@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Coleta e processa os dados do formulário
        idade = int(request.form['idade'])
        sexo = int(request.form['sexo'])
        escolaridade = int(request.form['escolaridade'])
        bolsa = int(request.form['bolsa'])
        trabalho_adicional = int(request.form['trabalho-adicional'])
        horas_estudadas = int(request.form['horas-estudadas'])
        impactos_atividades = int(request.form['impactos-atividades'])
        frequencia_aulas = int(request.form['frequencia-aulas'])
        discussao = int(request.form['discussao'])
        media = int(request.form['media'])
        id_curso = int(request.form['Id-Curso'])

        # Adicione aqui sua lógica de processamento com base nos dados coletados
        # Exemplo: cálculo de uma pontuação com base nos valores coletados

        resultado = idade + sexo + escolaridade + bolsa + trabalho_adicional + horas_estudadas + impactos_atividades + frequencia_aulas + discussao + media + id_curso

        return jsonify({'resultado': resultado})

    except Exception as e:
        # Em caso de erro, retorna uma mensagem de erro
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

