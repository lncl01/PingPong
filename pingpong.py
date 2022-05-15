from pygame import *
from random import randint
import time as sec
mixer.init()
font.init()

font = font.SysFont('Courier New', 50)

#window-------------------------------------------------------------------------

w_width = 1280
w_height = 720

window = display.set_mode((w_width, w_height))
display.set_caption('PingPong')

clock = time.Clock()
FPS = 60

#background---------------------------------------------------------------------

background = transform.scale(image.load("space.png"), (w_width, w_height))

#background_music---------------------------------------------------------------

mixer.music.load('calme.mp3')
mixer.music.play()
mixer.music.set_volume(0.03)

#class--------------------------------------------------------------------------

class GameSprite(sprite.Sprite):
    def __init__(self, player_img, player_speed, player_x, player_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (125, 125))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 580:
            self.rect.y += self.speed 

#sprites------------------------------------------------------------------------

block1 = Player('block.png', 5, 0, 50)

#game---------------------------------------------------------------------------

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:

        window.blit(background, (0, 0))

        block1.update1()
        block1.reset()
    
    display.update() 