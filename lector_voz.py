import pyttsx3 as pt

def configurar_velocidad(velocidad):
    engine = pt.init()
    engine.setProperty('rate', velocidad)

def configurar_volumen(volumen):
    engine = pt.init()
    engine.setProperty('volume', volumen)

def obtener_voces():
    engine = pt.init()
    voces = engine.getProperty('voices')
    for voice in voces:
        print("Nombre: ", voice.name)
        print("Id: ", voice.id)

def usar_voz_preferida(voz_preferida):
    engine = pt.init()
    engine.setProperty('voice', voz_preferida)

def generar_habla(texto):
    engine = pt.init()
    engine.say(texto)
    engine.runAndWait()

