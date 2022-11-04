from turtle import Turtle

# import pygame
# import os
from cross_game_myself.settings.game_settings import FONT, PATH_TO_ASSETS


class PauseLabel(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        # self.pause_sound = pygame.mixer.Sound(os.path.join(PATH_TO_ASSETS, 'sound', 'lose2.wav'))

    def update_pause(self):
        self.clear()
        self.color('green')
        self.write(arg=f'Player set pause', align='center', font=FONT)
        # pygame.mixer.Sound.play(self.pause_sound)
        
    