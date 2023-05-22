from recordAudio import record
from textToSpeech import textToSpeech
from speechToText import speechToTextWhisper, speechToTextDeepgram
from questionAnswer import questionAnswer
from playsound import playsound

audio = record()
text = speechToTextWhisper(audio)
if text == "Error":
    print("Speech To Text Error")
question = questionAnswer(text)
answer, filename = textToSpeech(question)
playsound(filename)


