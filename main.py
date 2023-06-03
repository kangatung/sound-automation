import speech_recognition as sr #voice to text
from gtts import gTTS #text to voice
from pygame import mixer as audio #play audio
from myProgram import youtube


def playAudio(myFile):
    audio.init()
    audio.music.load(myFile)
    # Memutar audio
    audio.music.play()
    # Tunggu hingga audio selesai diputar
    while audio.music.get_busy():
        continue
    # Menghentikan pemutaran audio
    audio.music.stop()

def audioToText():
    record = sr.Recognizer()
    with sr.Microphone() as source:
        getAudio = record.listen(source)

    global myAudio, judul
    try:
        myAudio = record.recognize_google(getAudio, language="id-ID")
        myAudio = myAudio.lower()
        print(f'audio: {myAudio}')
        try:
            judul = myAudio[myAudio.index('lagu')+ 5:]
        except:
            judul = 'jaran goyang'
    except:
        myAudio = 'jaran goyang'
        judul = myAudio
        playAudio('myAudio/noneText.mp3')

while True:
    playAudio('myAudio/start.mp3')
    audioToText()
    if 'mati' in myAudio:
        playAudio('myAudio/break.mp3')
        break
    elif 'tub' in myAudio:
        playAudio('myAudio/youtube.mp3')
        audioToText()
        youtube(judul)
    else:
        pass
