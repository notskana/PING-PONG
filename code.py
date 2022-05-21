#==================PING PONG=================#
from pygame import *

#===================WINDOW===================#
win = display.set_mode((800, 400))
display.set_caption("АЗОВ ТОП")
purple = (255, 255, 255)
win.fill(purple) 

#===================IMAGES===================#
ball = "ball.jpg"
wall1 = "wall.jpg"
wall2 = "wall.jpg"

#====================FPS=====================#
clock = time.Clock()
FPS = 60

#===================CLASS====================#
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y , player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_e] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys[K_d] and self.rect.y < 390:
            self.rect.y += self.speed

#==================OBJECTS===================#
tennis_ball = GameSprite(ball, 375, 175, 50, 50, 4)
racket1 = Player(wall1, 20, 140, 50, 150, 4)
racket2 = Player(wall2, 730, 140, 50, 150, 4)

#===================FONTS====================#
font.init()
font = font.Font(None, 35)
lose1 = font.render('PLAYER 1 LOSE!', False, (180, 0, 0))
lose2 = font.render('PLAYER 2 LOSE!', False, (180, 0, 0))

#===================GAME=====================#
game = True
finish = False
speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        win.fill(purple)
        racket1.update_l()
        racket2.update_r()
        tennis_ball.rect.x += speed_x
        tennis_ball.rect.y += speed_y

        #=============COLLISION==============#
        if sprite.collide_rect(racket1, tennis_ball) or sprite.collide_rect(racket2, tennis_ball):
            speed_x *= -1
            speed_y *= 1

        if tennis_ball.rect.y > 350 or tennis_ball.rect.y < 0:
            speed_y *= -1

        #==============WinLose===============#
        if tennis_ball.rect.x < 0:
            finish = True
            win.blit(lose1, (200, 200))
            
        if tennis_ball.rect.x > 800:
            finish = True
            win.blit(lose2, (200, 200))
        
        #===============RESET================#
        racket1.reset()
        racket2.reset()
        tennis_ball.reset()
    
    display.update()
    clock.tick(FPS)