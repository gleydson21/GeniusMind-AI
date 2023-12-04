# from flask import Flask
# from app.routes import api

# app = Flask(__name__)
# app.register_blueprint(api)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request, jsonify, Response

app = Flask(__name__)

@app.route('/main.py', methods=['POST', 'OPTIONS'])
def processar_formulario():
    if request.method == 'OPTIONS':
        # Configurar cabeçalhos para a solicitação OPTIONS
        response = Response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        return response
    # Lógica para processar o formulário
    # ...

    # Configurar o cabeçalho CORS
    response = jsonify({'message': 'Formulário processado com sucesso!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()