import pyttsx3
import random
import time
from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer

falas = ["Olha a cobra! É mentira!", "Olha a chuva! Já passou!", "A ponte quebrou! Nova ponte!", "O caminho da roça"]
algoritmo = [
    "Entrem de braços dados",
    "Se cumprimentem",
    "Olha a chuva: os participantes mudam de direção (meia volta) e colocam a mão na cabeça.",
    "Já passou: agora voltem.",
    "Balance: todos balançam os braços no ritmo da música.",
    "Olha o túnel: fiquem um de frente para o outro e dão as mãos formando um túnel.",
    "Olha a cobra: todos pulam, gritam e mudam de direção.",
    "Caracol: todos formam uma grande roda."
]






while (True):

    mixer.init()
    mixer.music.load('musica.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()



    engine = pyttsx3.init()
    engine.setProperty('volume', 1000)
    time.sleep(10)
    mixer.music.load('chico1.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    time.sleep(3)
    mixer.music.load('musica.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    time.sleep(15)
    mixer.music.load('chico2.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    time.sleep(3)
    mixer.music.load('musica.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    time.sleep(15)
    mixer.music.load('chico3.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    time.sleep(3)
    mixer.music.load('musica.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    time.sleep(10)
    mixer.init()
    mixer.music.load('chico4.mp3')
    mixer.music.set_volume(1.0)
    mixer.music.play()
    print("finalizado")

