# from flask import Flask
# from app.routes import api

# app = Flask(__name__)
# app.register_blueprint(api)

# if __name__ == "__main__":
#     app.run(debug=True)

# from flask import Flask, request, jsonify, Response

# app = Flask(__name__)

# @app.route('/main.py', methods=['POST', 'OPTIONS'])
# def processar_formulario():
#     if request.method == 'OPTIONS':
#         # Configurar cabeçalhos para a solicitação OPTIONS
#         response = Response()
#         response.headers.add('Access-Control-Allow-Origin', '*')
#         response.headers.add('Access-Control-Allow-Methods', 'POST')
#         response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
#         return response
#     # Lógica para processar o formulário
#     # ...

#     # Configurar o cabeçalho CORS
#     response = jsonify({'message': 'Formulário processado com sucesso!'})
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# if __name__ == '__main__':
#     app.run()

from flask import Flask, request, jsonify, Response
# import h5py
# import numpy as np

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
    # try:
    #     with h5py.File('modelo_XGBC.h5', 'r') as file:
    #         # Supondo que você tenha um dataset chamado 'dados' no arquivo .h5
    #         dados = np.array(file['dados'])
    # except Exception as e:
    #     return jsonify({'error': str(e)})

    # Configurar o cabeçalho CORS
    response = jsonify({'message': 'Formulário processado com sucesso!'})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '_main_':
    app.run()