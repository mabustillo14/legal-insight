import requests
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
SEARCH_URL = os.getenv('SEARCH_URL', '')

# Variables input
contrato = "El Arrendatario se compromete a pagar al Arrendador la cantidad de 150 000 pesos argentinos en concepto de alquiler mensual. El pago se realizará antes del día 10 de cada mes. El Arrendatario deberá realizar los pagos mediante cheques al Arrendador.El Arrendador se reserva el derecho de aumentar el alquiler mensualmente a partir del 10/11/2023. El incremento será de 10% sobre el monto del alquiler vigente en ese momento. El Arrendador notificará por escrito al Arrendatario con al menos treinta (30) días de anticipación sobre cualquier aumento en el alquiler."
opciones = ["Idea Principal"]
pregunta = ""

# Armar data json
data = {
  "data": [contrato, opciones, pregunta]
  }

# Hacer petición
response = requests.post("http://127.0.0.1:7860/run/predict", json=data)
print(response.json())