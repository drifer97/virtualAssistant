import speech_recognition as sr
import os
import datetime
import webbrowser
import pyttsx3
import random

# Inicializa o sintetizador de voz
engine = pyttsx3.init()
engine.setProperty('rate', 200)  # Ajusta a velocidade da fala
engine.setProperty('volume', 0.9)  # Define o volume de 0.0 a 1.0

# Função para capturar áudio do microfone
def get_audio():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            r.adjust_for_ambient_noise(source)  # Ajusta para ruído ambiente
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=7)  # Timeout para evitar travamento
                said = r.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {said}")
                return said.lower()
            except sr.UnknownValueError:
                print("Desculpe, não consegui entender.")
                return ""
            except sr.RequestError:
                print("Erro com o serviço de reconhecimento.")
                return ""
            except sr.WaitTimeoutError:
                print("Tempo limite esgotado para início de fala.")
                return ""
    except OSError as e:
        print("Erro no microfone:", str(e))
        speak("Por favor, conecte um microfone e tente novamente.")
        return ""
    except Exception as e:
        print(f"Exceção: {str(e)}")
        return ""

# Função para converter texto em fala e reproduzir áudio
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Erro na síntese de fala: {str(e)}")

# Função para contar piadas em português
def get_joke():
    jokes = [
        "Por que o matemático foi ao médico? Porque ele estava com problemas de cálculo!",
        "O que o zero disse para o oito? Que cinto bonito!",
        "Por que a plantinha não foi atendida no hospital? Porque só tinha médico de plantão!"
    ]
    return random.choice(jokes)

# Função principal do assistente virtual
def virtual_assistant():
    print("Elana está ativo. Diga 'sair' para encerrar.")
    speak("Olá, eu sou a Elana. Como posso ajudá-lo hoje?")

    while True:
        text = get_audio()

        if "olá" in text:
            speak("Olá, como você está?")
        elif "seu nome" in text:
            speak("Meu nome é Elana.")
        elif "horas" in text:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"Agora são {current_time}.")
        elif "piada" in text:
            joke = get_joke()
            speak(joke)
        elif "buscar" in text:
            speak("O que você quer buscar?")
            search_query = get_audio()
            if search_query:
                url = "https://google.com/search?q=" + search_query
                webbrowser.open(url)
                speak(f"Aqui está o que encontrei sobre {search_query}.")
            else:
                speak("Não consegui entender o que você quer buscar.")
        elif "sair" in text:
            speak("Até logo! Tenha um ótimo dia.")
            break
        elif text:
            speak("Não entendi, mas estou sempre aprendendo. Por favor, tente novamente.")

# Inicializa o assistente
if __name__ == "__main__":
    virtual_assistant()
