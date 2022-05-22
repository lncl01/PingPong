from pygame import *
from random import randint
import time as sec
mixer.init()
font.init()

font = font.SysFont('Courier New', 75)

#score--------------------------------------------------------------------------

score1 = 0

score2 = 0

#speed--------------------------------------------------------------------------

speed_x = 10

speed_y = 10

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
    def __init__(self, player_img, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_img), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 580:
            self.rect.y += self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 580:
            self.rect.y += self.speed 

#sprites------------------------------------------------------------------------

block1 = Player('blockupdate.png', 15, 0, 50, 30, 125)
block2 = Player('blockupdate.png', 15, 1250, 50, 30, 125)

ball = GameSprite('ball.png', 10, 690, 360, 50, 50)

scoretable = GameSprite('score.png', 0, 575, 0, 200, 200)

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

        block2.update2()
        block2.reset()

        scoretable.reset()

        ball.reset()

        ball.rect.x += speed_x 
        ball.rect.y += speed_y

        score = font.render(str(score1) + ":" + str(score2), True,(0,0,0))
        window.blit(score, (605, 110))

        if ball.rect.x > w_width:
            score1 += 1

        if ball.rect.x < 0:
            score2 += 1

        if score1 == 5:
            win1 = font.render('PLAYER 1 WON', True,(255,255,255))
            window.blit(win1, (400, 340))
            end_time = int(sec.time())
            finish = True
        
        if score2 == 5:
            win2 = font.render('PLAYER 2 WON', True,(255,255,255))
            window.blit(win2, (400, 340))
            end_time = int(sec.time())
            finish = True

        if ball.rect.y > w_height - 50 or ball.rect.y < 0:
            speed_y *= -1
    
        if sprite.collide_rect(block2, ball):
            speed_x *= -1

        if sprite.collide_rect(block1, ball):
            speed_x *= -1

        if ball.rect.x > w_width or ball.rect.x < 0:
            ball = GameSprite('ball.png', 10, 690, 360, 50, 50)
    
    if finish == True:
        start_time = int(sec.time())
        if start_time - end_time >= 3:
            finish = False
            score1 = 0
            score2 = 0

            block1 = Player('blockupdate.png', 15, 0, 50, 30, 125)
            block2 = Player('blockupdate.png', 15, 1250, 50, 30, 125)

            ball = GameSprite('ball.png', 10, 690, 360, 50, 50)

            scoretable = GameSprite('score.png', 0, 575, 0, 200, 200)

    display.update() 