# Colocar música mp3
#Precisa colocar a música na pasta(colar), nome do arquivo. instalar pygame
import pygame
pygame.mixer.init()
pygame.mixer.music.load('projeto 05.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()