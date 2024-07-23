from vosk import Model, KaldiRecognizer
import os
import pyaudio
import time
import json
import requests
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

model = Model(r"F:\\code_programs\\Python_prog\\codes_Python\w27_pr_2\\Vasya\\vosk-model-small-ru-0.22")
rec = KaldiRecognizer(model, 44100)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=8000
)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = json.loads(rec.Result())
        print(result["text"].split())
        full_text = result["text"].split()
        if "василиса" in full_text:
            if "погода" in full_text:
                response = requests.get("http://0.0.0.0:3000/current-weather").json()
                engine.say(
                    f'Сейчас {response["temperature"]} градусов и {response["condition"]}'
                )
                engine.runAndWait()

            elif "курс" in full_text and "доллара":
                response = requests.get('http://127.0.0.1:5000/currency_valute').json()
                engine.say(
                    f'Курс доллара {response}'
                )
                engine.runAndWait()

stream.stop_stream()
stream.close()
p.terminate()
