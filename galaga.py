import pgzrun
import random

HIEGHT=600
WIDTH=1200
TITLE="Galaga"


#lists
bullets=[]
enemies=[]
#actors
spaceship=Actor('galaga')
spaceship.x=WIDTH//2
spaceship.y=500
bullet=Actor('bullet')
enemy=Actor('bug')
#Variables
score=0
drawbullet=False
vx=2
vy=2
BLUE=(0,0,225)

def draw():
    screen.clear()
    spaceship.draw()
    for bullet in bullets:
        bullet.draw()
    for enemy in enemies:
        enemy.draw()
    if drawbullet==True:
        bullet.draw()




def update():
    global vx,vy,drawbullet
    if keyboard.left:
        spaceship.x=spaceship.x+5
    if keyboard.right:
        spaceship.x=spaceship.x-5
    if keyboard.up:
        drawbullet=True
        bullet.y=bullet.y-5

'''def update():
    global vx
    global vy
    if keyboard.left:
        spaceship.x=spaceship.x-vx
    if keyboard.right:
        spaceship.x=spaceship.x+vx
    if keyboard.space:
        for bullet in bullets:
            bullet.y-=10
            if bullet.y<0:
                bullets.remove(bullet)'''





'''def on_key_down(key):
    if key==keyboard.space:
        bullets.append(Actor('bullet'))
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-90'''






pgzrun.go()