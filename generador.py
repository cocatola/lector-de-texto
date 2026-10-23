import pyttsx3


def speak(text):
    engine = pyttsx3.init()

    engine.setProperty("rate", 200)
    engine.setProperty("volume", 1.0)

    voices = engine.getProperty("voices")
    if len(voices) > 1:
        engine.setProperty("voice", voices[1].id)

    engine.say(text)
    engine.runAndWait()


print("==========================================")
print("    lectctor de texto                     ")
print("==========================================")
print("Escribe 'salir' para cerrar el programa.\n")

while True:
    texto = input("Escribe algo: ")

    if texto.strip().lower() == "salir":
        speak("¡Hasta luego!")
        print("Programa finalizado.")
        break

    if texto.strip():
        speak(texto)
    else:
        print("Por favor, escribe algún texto.")