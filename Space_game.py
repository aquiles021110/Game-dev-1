import pgzrun
import random
from time import time
WIDTH=800
HEIGHT=700
starttime=0
totaltime=0
satelitelists=[]
lines=[]
nextsatelite=0
totalsatelites=10
def objects():
    global starttime
    for i in range(totalsatelites):
        satelite=Actor('satelite')
        satelite.pos=random.randint(0,800),random.randint(0,700)
        satelitelists.append(satelite)
    starttime=time()
def draw():
    global totaltime
    screen.blit('space',(0,0))
    num=1
    for i in satelitelists:
        i.draw()
        screen.draw.text(str(num),(i.pos[0],i.pos[1]+20))
        num+=1
    for i in lines:
        screen.draw.line(i[0],i[1],'green')
    if nextsatelite<totalsatelites:
        totaltime=time()-starttime
        totaltime=round(totaltime,2)
        screen.draw.text(str(totaltime),(0,0),fontsize=25)
    else:
         screen.draw.text(str(totaltime),(0,0),fontsize=25)
def update():
    pass
def on_mouse_down(pos):
    global totalsatelites,nextsatelite,satelitelists,lines
    if nextsatelite<totalsatelites:
        if satelitelists[nextsatelite].collidepoint(pos):
            if nextsatelite:
                lines.append((satelitelists[nextsatelite-1].pos,satelitelists[nextsatelite].pos))
            nextsatelite+=1 
        else:
            lines=[]
            nextsatelite=0
objects()
pgzrun.go()
