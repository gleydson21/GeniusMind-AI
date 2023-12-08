from flask import Flask, request
import tensorflow as tf

def load_model():
    # Caminho para o arquivo modelo.h5
    model_path = './data/modelo.h5'
    
    try:
        # Carregar o modelo salvo no arquivo .h5
        model = tf.keras.models.load_model(model_path)
            
        return model
    except Exception as e:
        print(f'Erro ao carregar o modelo: {str(e)}')
        return None

def predict_student(input_data):
    model = load_model()
    
    if model:
        # Realiza a previsão com base nos dados do formulário
        prediction = model.predict(input_data)
        
        # Verifica se o aluno foi aprovado ou reprovado
        if prediction == 1:
            return 'Aprovado'
        else:
            return 'Reprovado'
    else:
        return 'Não foi possível carregar o modelo'
    
  
