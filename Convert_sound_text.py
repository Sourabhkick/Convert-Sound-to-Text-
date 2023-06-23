
from rom os import path
from pydub import AudioSegment

# files
src = "speech.mp3"
dst = "speech.wav"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")


import speech_recognition as sr
filename = r"C:\Users\Lazard\Downloads\barackobamafederalplaza.wav"
r = sr.Recognizer()
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
