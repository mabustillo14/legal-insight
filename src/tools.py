from src.database import extract_prompt
from src.ai_model import mychatbot

def contract_api(contrato, checkbox_categorias, pregunta):

    # Verificar que existe un contrato
    if len(contrato) == 0:
        return "[ERROR]: ¡Ups!, Carga un contrato para que pueda analizarlo."

    # Variables
    tot_prompt = "" # Todos los prompt que voy a solicitar
    caracteres = 50 # Cantidad de caracteres para la respuesta por cada prompt seleccionado
    cant_caracteres = 0 # Cantidad total de caracteres para la conclusion
    
    # Leer los datos de Input
    if len(checkbox_categorias) != 0: # Si hay alguna categoria seleccionada
        for categoria in checkbox_categorias: # Se extra el prompt de cada categoria
            tot_prompt += extract_prompt(categoria) + " \n"
            cant_caracteres += caracteres
        
    elif len(checkbox_categorias) == 0 and len(pregunta) == 0: 
        # Si no se selecciona ninguna categoria y no hay una pregunta, se seleciona el prompt de la idea principal
        tot_prompt += extract_prompt("Idea Principal")
        cant_caracteres += caracteres

    
    if len(pregunta) != 0: # Verificar si hay una pregunta puntual
        tot_prompt += " " + pregunta + ". " # Añadir pregunta como prompt
        cant_caracteres += caracteres

    # Indicar que tantos caracteres debe tener la conclusion en funcion a la cantidad de prompts
    tot_prompt += " Dame un parrafo de maximo " + str(cant_caracteres) + " caracteres." 

    # Una vez definido los prompts, hacemos la consulta a nuestra base de conocimiento con la api de openAI
    conclusion = " "
    conclusion = mychatbot(tot_prompt, contrato)
    
    return conclusion

