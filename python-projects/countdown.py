import time

#Hide the pygame community message
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

count = []

pygame.init()
pygame.mixer.music.load("Python\\Projects\\sound.mp3")


def counter(num):
    for i in reversed(range(1,num+1)):
        print(i)
        time.sleep(1)
        count.append(1)
         
user = input("\nEnter the number you want to start the countdown with: ")

try:
    user = int(user)
    counter(user)
    
    pygame.mixer.music.play()
    
    while pygame.mixer.music.get_busy():
        time.sleep(1)
        
except:
    print("\nNot a valid integer")