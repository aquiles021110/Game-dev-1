import pgzrun
import random
WIDTH=500
HEIGHT=500
def draw():
    r=0
    g=255
    b=random.randint(0,255)
    width=WIDTH
    height=HEIGHT-200
    screen.fill('White')
    thing=Rect((0,0),(width,height))
    thing.center=250,250
    screen.draw.filled_rect(thing,'red')
    screen.draw.filled_circle((250,250),25,'green')
    screen.draw.line((10,250),(200,260),'blue')
'''for i in range(20):
        thing=Rect((0,0),(width,height))
        thing.center=(250,250)
        screen.draw.rect(thing,(r,g,b))
        height+=10
        width-=10
        r+=10
        g-=10'''

pgzrun.go()
