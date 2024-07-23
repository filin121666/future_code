from vosk import Model, KaldiRecognizer
import os
import pyaudio

model = './vosk-model-small-en-us-0.15'
rec = KaldiRecognizer(Model(model), 8000)
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16, 
    channels=1, 
    rate=8000, 
    input=True, 
    frames_per_buffer=8000
)
stream.start_stream()

while True:
    data = stream.read(4000)
    if len(data) == 0:
        break

    print(rec.Result() if rec.AcceptWaveform(data) else rec.PartialResult())

print(rec.FinalResult())