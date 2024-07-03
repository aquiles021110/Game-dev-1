import pgzrun
from random import randint
WIDTH=1000
HEIGHT=1000
score=0
end=False
bee=Actor('bumblebee')
bee.pos=500,500
flower=Actor('flower')
flower.pos=200,200
def draw():
    #screen.clear()
    screen.blit('grass',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text('Score:'+str(score),color='black', topleft=(0,0))
    if end:
        screen.fill('pink')
        screen.draw.text('Times up! \n Score: '+str(score),color='green',topleft=(500,400),fontsize=40)
def timer():
    global end
    end=True
clock.schedule(timer,20.0)
def update():
    global score
    if keyboard.left or keyboard.a:
        bee.x-=3
    if keyboard.right or keyboard.d:
        bee.x+=3
    if keyboard.up or keyboard.w:
        bee.y-=3
    if keyboard.down or keyboard.s:
        bee.y+=3
    collision=bee.colliderect(flower)
    if collision:
        score+=1
        flower.x=randint(0,500)
        flower.y=randint(0,500)
pgzrun.go()