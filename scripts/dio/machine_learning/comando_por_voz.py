
import speech_recognition as sr
import os

# Função para ouvir e reconhecer a fala
def ouvir_microfone():

    # Habilita o reconhecimento de voz
    microfone = sr.Recognizer()

    # Chama o microfone
    with sr.Microphone() as source:

        # Chama um algoritmo de redução de ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o usuário dizer algo
        print('Diga alguma coisa: ')

        # Armazena o que foi dito em uma variável
        audio = microfone.listen(source)

    try:
        # Passa a variável para o algoritmo reconhecer padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "navegador" in frase.lower():
            os.system("start Chrome.exe")
            return False

        elif "excel" in frase.lower():
            os.system("start Excel.exe")
            return False

        elif "powerpoint" in frase.lower():
            os.system("start POWERPNT.exe")
            return False

        elif "edge" in frase.lower():
            os.system("start msedge.exe")
            return False

        elif "fechar" in frase.lower():
            return True

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    except sr.UnknownValueError:
        print("Não entendi")

    except sr.RequestError:
        print("Erro ao conectar com o serviço de reconhecimento de voz")

    return frase


while True:
    if ouvir_microfone():
        break
