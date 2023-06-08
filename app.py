import gradio as gr
from src.tools import contract_api

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

enable_queue=False



# Inputs
contrato = gr.Textbox(label='1) Cargar Contrato 📂') # Texto
checkbox_categorias =  gr.CheckboxGroup(
    ["Idea Principal", "Plazos y Fechas", "Notas Importantes", "Pagos y Tarifas","Condiciones y Términos", "Letra Pequeña" ], 
    label='2) Seleccionar Parámetros de Análisis ⚙️') # Lista
pregunta = gr.Textbox(label='3) Pregunta Puntual ❓ [OPCIONAL]') # Texto
input = [contrato, checkbox_categorias, pregunta]

# Outputs
conclusiones = gr.Textbox(label="Conclusiones del análisis del Contrato 📝🔍")
output = [conclusiones]

"""
# Ejemplos precargados
def dar_ejemplo():
    with open('src/contrato.txt', 'r') as archivo:
    # Lee el contenido completo del archivo
        contrato = archivo.read()
    ejemplo = [[contrato, ["Letra Pequeña"], "¿Cuánto es el aumento mensual?"]]
    return ejemplo
"""

# GUI
demo = gr.Interface(
    fn=contract_api, 
    inputs=input, 
    outputs=output,
    title=title,
    description=description, 
    article=article
#    examples = dar_ejemplo()
    )
    

demo.launch(enable_queue=enable_queue,debug=True)