import speech_recognition as sr
import pyttsx3
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia
import pyaudio


#Escuchar nuestro microfono y devolver el audio como texto

def transf_audio_en_texto():

    #Almacenar el reconocedor en una variable
    r = sr.Recognizer()

    #Configurar microfono
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.8


        #Informar que comenzo la grabación
        print("Ya puedes hablar ")

        #Guardar lo que escuche cómo audio
        audio = r.listen(origen)


        try:
            #Buscar en google
            pedido = r.recognize_google(audio, language="es-es")

            #prueba de que pudo ingresar
            print("Dijiste: "+ pedido)


        #En caso de que no comprenda el usuario
        except sr.UnknownValueError:

            #prueba de que no comprendió
            print("Ups, no hay servicio")

            #devolver error
            return "Sigo esperando"

        #En caso de no resolver el pedido
        except sr.RequestError:

            # prueba de que no comprendió
            print("Ups no entendí")

            # devolver error
            return "Sigo esperando"


        #Error inesperado
        except:
            # prueba de que no comprendió
            print("Ups algo ha salido mal")

            # devolver error
            return "Sigo esperando"


transf_audio_en_texto()
