import gradio as gr
from src.tools import contract_api
from src.database import extract_contract


def dar_ejemplo(contract_examples, contract_examples_categorias, contract_examples_question):
    ejemplo = []
    for i in range(len(contract_examples)):
        aux_ejemplo = []
        aux_ejemplo.append(extract_contract(contract_examples[i]))
        aux_ejemplo.append(contract_examples_categorias[i])
        aux_ejemplo.append(contract_examples_question[i])
        ejemplo.append(aux_ejemplo)
    return ejemplo


# Descripción del Header
title = 'Legal Insight.ai 💼'
description = """
<center><h2><b>Análisis inteligente de contratos 📑💡 </b></h2>
Simplemente carga el contrato 📂, elige la categoría de análisis y obtén conclusiones detalladas.
</center>
"""

# Descripción del Footer
article = """
<b>¿Por qué elegirnos?</b>
<br><b>Legal Insight AI</b>, tu aliado inteligente para el análisis de contratos.<br>Simplifica la comprensión legal, toma decisiones informadas y optimiza tu flujo de trabajo.
<br>Descubre el poder de la inteligencia artificial aplicada a contratos legales.💡
<br><center><b>Mario Bustillo 2023 🚀</b> | [Github](https://github.com/mabustillo14) | [Linkedin](https://www.linkedin.com/in/mario-bustillo/) 🤗</center>
"""

# Inputs
contrato = gr.Textbox(label='1) Cargar Contrato 📂') # Texto
checkbox_categorias =  gr.CheckboxGroup(
    label='2) Seleccionar Parámetros de Análisis ⚙️', 
    choices = ["Idea Principal", "Plazos y Fechas", "Notas Importantes", "Pagos y Tarifas","Condiciones y Términos", "Letra Pequeña" ], 
    ) # Lista
pregunta = gr.Textbox(label='3) Pregunta Puntual ❓ [OPCIONAL]') # Texto
input = [contrato, checkbox_categorias, pregunta]

# Outputs
conclusiones = gr.Textbox(label="Conclusiones del análisis del Contrato 📝🔍")
output = [conclusiones]


# Ejemplos precargados
contract_examples = ["Alquilar Departamento", "Makers Coding Challenge", "Contrato Profesional"]
contract_examples_categorias = [["Letra Pequeña"], ["Idea Principal"], []]
contract_examples_question = ["¿Cuánto es el aumento mensual?","","¿De que tipo es mi jornada laboral?"]
ejemplo_default = dar_ejemplo(contract_examples, contract_examples_categorias, contract_examples_question)

# GUI
demo = gr.Interface(
    fn=contract_api, 
    inputs=input, 
    outputs=output,
    title=title,
    description=description, 
    article=article,
    examples = ejemplo_default
    )

demo.launch(enable_queue=False,debug=True)