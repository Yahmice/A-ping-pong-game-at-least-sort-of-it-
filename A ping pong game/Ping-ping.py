from pygame import *
from time import time as timer
import random

WIDTH = 700
HEIGHT = 500


BALL_SPEED_UP = 1.05
BALL_MAX_SPEED = 40
BALL_X_SPEED = 3
BALL_Y_SPEED = 3    

score = 0
#классы 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, size_x, size_y,player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed




#окно приложения
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption('Ping-Pong')

#фон
background = transform.scale(image.load('bg.png'), (WIDTH,HEIGHT))

#спрайты
player_l = Player('paddle.png', 40, 150, 10, 200, 10)
player_r = Player('paddle.png', 40, 150, 650, 10, 10) 
ball = GameSprite('ball.png', 40, 40, 350, 230, 4)








FPS = 75
running = True
finish = False
clock = time.Clock()
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', True, (180,0,0))
lose2 = font.render('PLAYER 2 LOSE!', True, (180,0,0))
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    if finish != True:
        ball.rect.x += BALL_X_SPEED
        ball.rect.y += BALL_Y_SPEED

        if ball.rect.y > HEIGHT - 50 or ball.rect.y < 0:
            BALL_Y_SPEED *=-1

        if ball.rect.x <0:
            finish = True
            window.blit(lose1, (200,200))


        
        if ball.rect.x > WIDTH:
            finish = True
            window.blit(lose2, (200,200))

        
        window.blit(background, (0,0))
        player_l.update_l()
        player_r.update_r()

        player_l.reset()
        player_r.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)


        