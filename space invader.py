import math
import random

import pygame
from pygame import mixer

pygame.init()
screen=pygame.display.set_mode((800,500))

background=pygame.image.load('background.png')

mixer.music.load("background.wav")
mixer.music.play(-1)

pygame.display.set_capttion("Space Invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerimg=pygame.image.load('player.png')
playerx=370
playery=380
playerx_change=0
enemy_img=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
num_of_enemies=6

for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load('enemy.png'))
    enemy_x.append(random.randint(0,735))
    enemy_y.append(random.randint(50,150))
    enemy_x_change.append(4)
    enemy_y_change.append(40)

#bulllet
#Ready - You can't see the bullet in the screen
#Fire - The bullet is currently moving

bulletimg=pygame.image.load('bullet.png')
bulletx=0
bullety=480
bulletx_change=0
bullety_change=10
bullet_state="ready" 

#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',64)
def show_score(x,y):
    score_value=font.render("Score:" +str(score_value),True,(255,255,255))
    screen.blit(score_value,(x,y))
def player(x,y):
    screen.blit(playerimg,(x,y))
def game_over_text():
    over_font=pygame.font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_font,(200,250))
def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletimg,(x+16,y+10))
def isCollision(enemyx,enemyy,bulletx,bullety):
    distance=math.sqrt(math.pow(enemyx-bulletx,2)+math.pow(enemyy-bullety,2))
    if distance < 27:
        return True
    else:
        return False
running=True
while running:
    screen.fill((0,0,0))
    #background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound=mixer.Sound("Laser.wav")
                    bulletSound.play()
                    #get the current x coordinate of the spaceship
                    bulletx=playerx
                    fire_bullet(bulletx,bullety)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    playerx+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736

        #enemy movement
    for i in range(num_of_enemies):

        #Game Over
        if enemyy[i]>340:
            for j in range(num_of_enemies):
                enemyY[j]=2000
            game_over_text()
            break
        enemyy[i]+=enemyy_change[i]
        if enemyx[i]<=0:
            enemyx_change[i]=4
            enemyy[i]+=enemyy_change[i]
        elif enemyx[i]>=736:
            enemyx_change[i]=-4
            enemyy[i]+=enemyy_change[i]
        collision=isCollision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            explosionSound=mixer.Sound("explosion.wav")
            explosionSound.play()
            bullety=480
            bullet_state="ready"
            score_value+=1
        enemy(enemyx[i],enemyy[i],i)

    if bullety<=0:
        bullety=380
        bullet_state=ready
    if bullet_state is "fire":
        fire_bullet(bulletx,bullety)
        bullety-=bullety_change
        
    player(playerx,playery)
    show_score(textX,textY)
    pygame.display.update