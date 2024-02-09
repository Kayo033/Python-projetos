#Faça um programa em python que leia um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('queen.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

