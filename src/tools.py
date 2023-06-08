from database import extract_prompt


def contract_api(contrato, checkbox_categorias, pregunta):

    # Verificar que existe un contrato
    if len(contrato) == 0:
        return "[ERROR]: ¡Ups!, Carga un contrato para que pueda analizarlo."

    # Variables
    tot_prompt = "" # Todos los prompt que voy a solicitar
    caracteres = 50 # Cantidad de caracteres para la respuesta por prompt
    cant_caracteres = 0 
    
    # Extraer los datos de entrada
    if len(checkbox_categorias) != 0: # Si hay alguna categoria seleccionada
        for categoria in checkbox_categorias:
            tot_prompt += extract_prompt(categoria) + " \n"
            cant_caracteres += caracteres
        
    elif len(checkbox_categorias) == 0 and len(pregunta) == 0: 
        # Si no se selecciona ninguna categoria y no hay una pregunta, devuelve la idea principal
        tot_prompt += extract_prompt("Idea Principal")
        cant_caracteres += caracteres

    
    if len(pregunta) != 0: # Verificar si hay una pregunta puntual
        tot_prompt += " " + pregunta + " "
        cant_caracteres += caracteres

    tot_prompt += " Dame un parrafo de maximo " + str(cant_caracteres) + " caracteres." 

    return tot_prompt
    



