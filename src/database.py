import os
import json
from dotenv import load_dotenv
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


# Cargar variables de entorno
load_dotenv()

aux_firebase = os.getenv('FIREBASE_CREDENTIALS', '')
FIREBASE_CREDENTIALS = json.loads(aux_firebase)
DATABASE_URL = os.getenv('DATABASE_URL', '')

# Inicializa la conexión con Firebase
cred = credentials.Certificate(FIREBASE_CREDENTIALS)

# Referencia a la base de datos en tiempo real
firebase_admin.initialize_app(cred,{'databaseURL': DATABASE_URL})

# Base de datos "py"
ref = db.reference('py/')
users_ref = ref.child('categorias/')
contract_ref = ref.child('contratos/')


def agregar_prompt():
    # Coleccion con el nombre de categorias
    
    users_ref.set({
        "Idea Principal": {
            'prompt': "¿Cuál es la idea principal o propósito del contrato?. Resume en pocas palabras cuál es el objetivo principal del contrato."
        },

        "Plazos y Fechas":{
            'prompt':"¿Qué fechas son importantes en el contrato?. Menciona las fechas clave, como inicio, finalización, plazos de pago, etc."
            },
        
        "Notas Importantes":{
            'prompt':"¿Hay alguna información relevante o destacada que deba tenerse en cuenta?. Enumera cualquier nota o aspecto importante a considerar dentro del contrato."
            },
        
        "Pagos y Tarifas":{
           'prompt':"¿Cuáles son los pagos y tarifas relacionados con el contrato?. Describe los montos de pago, las tarifas aplicables y cualquier información relacionada con la compensación financiera."
           },
        
        "Condiciones y Términos":{
            'prompt':"¿Cuáles son las condiciones y términos clave del contrato?. Identifica las cláusulas y condiciones más relevantes que rigen el contrato."
            },

        "Letra Pequeña": {
            'prompt': "¿Qué detalles importantes se encuentran en la letra pequeña del contrato?. Señala los aspectos detallados o más específicos del contrato que pueden ser fácilmente pasados por alto."
        }
    })


def agregar_contract():
    contract_ref.set({
        "Alquilar Departamento": {
            'content': 
            "El Arrendatario se compromete a pagar al Arrendador la cantidad de 150 000 pesos argentinos en concepto de alquiler mensual. El pago se realizará antes del día 10 de cada mes. El Arrendatario deberá realizar los pagos mediante cheques al Arrendador.El Arrendador se reserva el derecho de aumentar el alquiler mensualmente a partir del 10/11/2023. El incremento será de 10% sobre el monto del alquiler vigente en ese momento. El Arrendador notificará por escrito al Arrendatario con al menos treinta (30) días de anticipación sobre cualquier aumento en el alquiler."
        },

        "Makers Coding Challenge": {
            'content':
            "Para nuestro proceso de selección, buscamos personas que estén dispuestas a enviar software rápidamente y con alta calidad. Es por eso que nuestro proceso de selección se basa en proyectos. Creemos que será una experiencia increíble para usted y estamos entusiasmados con ella. Construir su propia pieza de software es una experiencia emocionante. Significa aportar algo al mundo. Queremos que trabaje en una idea que requiera software, que puede ser suyo o de nuestra lista seleccionada. Si nos permite, al final de este proceso, compartiremos su proyecto en nuestras plataformas de redes sociales. Tenemos algunos requisitos para su proyecto. Debe: obtener datos de una API, tener una base de datos, tener una API para comunicarse con su base de datos, tener una interfaz de usuario simple y una forma de interactuar con ella. Horas de dedicación: 6 - 8 horas en total (depende de usted cuántas horas quiere dedicar). Plazo: una semana (después de recibir el correo electrónico)"
        },

        "Contrato Profesional":{
            'content':
            "El Empleador, Juan Bustos, contrata al Empleado, Matias Caballeros, para desempeñarse en el puesto de Gerente Comercial en Comercial San Andres. El contrato tendrá una duración indefinido, y el Empleado trabajará en jornada completa. A cambio de sus servicios, el Empleado recibirá un salario de 150 000 pesos argentinos pagadero dentro los primeros 10 dias del mes. Ambas partes acuerdan cumplir con las obligaciones establecidas en este contrato y respetar las leyes laborales y regulaciones aplicables."
        }
    })


def extract_prompt(prompt_class):
    # Leer informacion
    direccion = 'py/categorias/' + prompt_class
    promt_text = db.reference(direccion).get()

    # Segmentar el contenido del prompt
    prompt = ""
    for texto in promt_text.values():
        prompt = promt_text.get('prompt')
    return prompt


def actualizar_prompt(texto):
    hopper_ref = users_ref.child('Contrato')
    hopper_ref.update({
        'prompt': texto
    })


def extract_contract(contract_tittle):
    # Leer informacion
    direccion = 'py/contratos/' + contract_tittle
    contract_text = db.reference(direccion).get()

    # Segmentar el contenido del prompt
    contract = ""
    for texto in contract_text.values():
        contract = contract_text.get('content')    
    return contract


# agregar_prompt()
agregar_contract()
