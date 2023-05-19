import speech_recognition as sr
import pyaudio
import pyttsx3
from lector_voz import *
import sys

# Muestro los microfonos instalados
mic_instalados = sr.Microphone.list_microphone_names()

# Instancio el microfono y uso un micrfono antes mostrado
mic = sr.Microphone(device_index=0)

# Instancio el reconocimiento de voz
r = sr.Recognizer()

# Utilizo un gestor de contexto with para capturar entrada
while True:
    with mic as source:  # --- Uso source por buena practica
        print("Di algo..")
        audio = r.listen(source)  # ---Guardo el audio en audio

    try:
        texto = r.recognize_google(audio, language='Es-es')  # ---Lo reconozco con el API de google
        print(f"Dijiste: {texto}")

        # Uso sys para acabar el chat con una palabra
        if texto=="apagar":
            print("Apagando...")
            sys.exit()

    except sr.UnknownValueError:
        print("No te entendi, lo siento")
    except sr.RequestError as rq:
        print('Hubo un error al reconocer el microfono')
