"""
NOME/NAME: Raphael Araújo
DATA/DATE: 30/10/2019
[PT]
>  Faça um programa em Python que abre e reproduz o áudio de um arquivo MP3.
[EN]
> Make a Python program that opens and plays the audio from an MP3 file.
"""
from pygame import mixer
mixer.init()
mixer.music.load('som.mp3')
mixer.music.play()
input('')