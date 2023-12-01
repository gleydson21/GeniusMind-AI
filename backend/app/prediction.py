# import pickle

# def load_model():
#     # Caminho para o arquivo modelo.pkl gerado por sua IA
#     model_path = '/data/modelo.pkl'
    
#     try:
#         # Carrega o modelo salvo no arquivo .pkl
#         with open(model_path, 'rb') as file:
#             model = pickle.load(file)
            
#         return model
#     except Exception as e:
#         print(f'Erro ao carregar o modelo: {str(e)}')
#         return None

# def predict_student(input_data):
#     model = load_model()
    
#     if model:
#         # Realiza a previsão com base nos dados do formulário
#         prediction = model.predict(input_data)
        
#         # Verifica se o aluno foi aprovado ou reprovado
#         if prediction == 1:
#             return 'Aprovado'
#         else:
#             return 'Reprovado'
#     else:
#         return 'Não foi possível carregar o modelo denovo'
    
#     # A função load_model carrega o modelo treinado salvo no arquivo .pkl.
#     # Em seguida, a função predict_student utiliza o modelo carregado para fazer a previsão com base nos dados do formulário.
#     # No caso de uma previsão de valor 1, significa que o aluno foi aprovado, caso contrário, se for uma previsão de valor 0, o aluno foi reprovado.