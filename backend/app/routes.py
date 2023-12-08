# from flask import Blueprint, request, jsonify

# form_blueprint = Blueprint('form', __name__)

# @form_blueprint.route('/enviar', methods=['POST'])
# def enviar_dados():
#     if request.method == 'POST':
#         data = request.json  # Obtém os dados JSON da solicitação

#         # Verifique se os campos desejados estão presentes no JSON
#         if 'idade' in data and 'sexo' in data:
#             idade = data['idade']
#             sexo = data['sexo']
#             escolaridade = data.get('escolaridade', '')  # Use get para campos opcionais
#             bolsa = data.get('bolsa', '')
#             trabalho_adicional = data.get('trabalho_adicional', '')
#             horas_estudadas = data.get('horas_estudadas', '')
#             impactos_atividades = data.get('impactos_atividades', '')
#             frequencia_aulas = data.get('frequencia_aulas', '')
#             discussao = data.get('discussao', '')
#             media = data.get('media', '')
#             id_curso = data.get('Id_Curso', '')

#             # Faça o processamento dos dados conforme necessário

#             resposta = {'mensagem': 'Dados recebidos com sucesso!'}
#             return jsonify(resposta)
#         else:
#             return jsonify({'mensagem': 'Campos obrigatórios ausentes'}), 400  # Resposta de erro

#     return 'Método não permitido', 405
