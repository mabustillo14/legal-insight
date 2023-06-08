import os
from dotenv import load_dotenv
import openai


# Cargar variables de entorno
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY', '')

# Asignar la API Key
openai.api_key = OPENAI_KEY


def mychatbot(query, contract_knowledge):
    # Chatbot que hace consultas "query" a una base de conocimiento "contract_knowledge"

    # Enviar solicitud a la api OpenAI con el modelo "GPT-3.5-turbo"
    res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": "Responda mis consultas de acuerdo con el contexto dado. Si no se tiene una respuesta clara o sin información se debe indicar. \nContexto: {}".format(str(contract_knowledge))},
            {"role": "assistant", "content": "¡Ok, seguro!"},
            {"role": "user", "content": query}
        ]
    )

    # Del diccionario extraer la informacion correspondiente al id "content"
    conclusion = res['choices'][0]['message']['content']
    
    return conclusion