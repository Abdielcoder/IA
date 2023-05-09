import openai
import PySimpleGUI as sg

# Configura la API key de OpenAI
openai.api_key = "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"
context = "Somos una empresa dedicada al desarrollo de agentes de seguros, con más de 18 años de experiencia formada por un equipo de profesionales en la asesoría, administración de riesgos a través de planes financieros y de seguros, siempre de acuerdo a las necesidades de nuestros clientes. Esto nos ha permitido ganar diversos reconocimientos nacionales e internacionales de calidad y productividad. Así como extender nuestras oficinas a distintas ciudades, tales como: Tijuana, Monterrey, Hermosillo y Los Cabos,Desarrollar Agentes de seguros cuya misión sea proteger el patrimonio, proyectos de vida, así como la capacidad productiva de personas, familias y empresas en México.,Proteger a 200,000 clientes a través de agentes certificados en 10 ciudades estratégicas respaldados por los mejores productos con un equipo de colaboradores de gran calidad humana, comprometidos con una cultura de innovación y servicio.,"
# Crea la ventana con las dos cajas de texto
layout = [
    [sg.Text('Introduce el texto a enviar a OpenAI:')],
    [sg.InputText(key='input')],
    [sg.Text('Respuesta de OpenAI:')],
    [sg.Output(size=(60, 10), key='output')],
    [sg.Button('Enviar'), sg.Button('Salir')]
]

window = sg.Window('GPT PATITO', layout)

# Bucle principal de la aplicación
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Salir'):
        break

    if event == 'Enviar':
        # Obtiene la entrada del usuario
        input_text = values['input']

        # Realiza la petición a OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=context.input_text,
            max_tokens=2048
        )

        # Obtiene la respuesta de OpenAI y la muestra en la caja de texto de salida
        output_text = response.choices[0].text
        window['output'].update(output_text)

# Cierra la ventana y termina la aplicación
window.close()

