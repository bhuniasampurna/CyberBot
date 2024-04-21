import speech_recognition as sr
import pyttsx3
import datetime
import os

Speak = pyttsx3.init()
Listen = sr.Recognizer()

def command_taker():
    try:
        with sr.Microphone() as mics:
            mic = Listen.listen(mics)
            command = str(Listen.recognize_google(mic)).lower()
            
        #if command in ["wikipedia", "search", "play"]:
        #    search.search(command.lower())
        #if "launch" in command:
        #    launch.launch(command.lower().split(maxsplit=1)[-1])
        #if "open" in command:
        #    open.open(command.lower().split(maxsplit=1)[-1])
        #if "send" in command:
        #    send.send(command.lower().split(maxsplit=1)[-1])
        #if "time" in command or "clock" in command:
        #    clock.time("time" + command.lower().split("time")[-1])
        #if "calculate" in command:
        #    calculator.calculator(command.split("calculate ")[-1])
        #if "date" in command or "day" in command:
        #    date.date(command)
        #if "weather" in command:
        #   weather.weather(command)

    except:
        pass


if __name__ == "__main__":
    with sr.Microphone() as mics:
        while True:
            try:
                print("Listening...")
                Listen.adjust_for_ambient_noise(mics)
                mic = Listen.listen(mics, phrase_time_limit=10)
                data = Listen.recognize_sphinx(mic)
                print(data)
                if "hello siri" in str(data).lower():
                    hour = datetime.datetime.now().hour
                    if hour > 5 and hour < 12:
                        Speak.say("Good Morning!!! How can I help you?")
                    elif hour > 11 and hour < 18:
                        Speak.say("Good Afternoon!!! How can I help you?")
                    elif hour > 17 and hour < 20:
                        Speak.say("Good Evening!!! How can I help you?")
                    else:
                        Speak.say("How can I help you?")
                    Speak.runAndWait()
                    command_taker()
                    Speak.say("")
                    Speak.runAndWait()
            except:
                # _ = os.system('cls')
                pass
