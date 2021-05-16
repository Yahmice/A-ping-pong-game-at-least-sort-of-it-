from pygame import *
from time import time as timer

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
        window.blit(self.image, (self.rect.x, self.rect.y))\


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y = -self.speed
        if keys[K_s] and self.rect.y <= 5:
            self.rect.y = +self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y = -self.speed
        if keys[K_DOWN] and self.rect.y <= 5:
            self.rect.y = +self.speed

#окно приложения
window = display.set_mode((700,500))
display.set_caption('Ping-Pong')

#фон
background = transform.scale(image.load('bg.png'), (700,500))

#спрайты
player_l = Player('paddle.png', 40, 100, 100, 430, 1)
player_r = Player('paddle.png', 40, 100, 100, 430, 1) 









FPS = 75
running = True
finish = False
clock = time.Clock()

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
    if finish != True:
        window.blit(background, (0,0))
        player_l.update_l()
        player_r.update_r()

        player_l.reset()
        player_r.reset()
    display.update()
    clock.tick(FPS)


        