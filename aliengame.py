import pgzrun
TITLE='Alien game'
WIDTH=500
HEIGHT=400
message=''
alien=Actor('alien')
HEIGHT=alien.height+50
alien.pos=20,60
def draw():
    screen.clear()
    screen.fill('black')
    alien.draw()
def update():
    alien.left+=4
    if alien.left>WIDTH:
        alien.right=0
def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print('Hit!')
        sounds.eep.play()
    else:
        print('Miss!')
pgzrun.go()

















'''alien.pos=500,500
def draw():
    screen.clear()
    screen.fill('light grey')
    alien.draw()
    screen.draw.text(message,(800,30),fontsize=100,color='blue')
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message='Hit!'
        alien.x=random.randint(10,990)
        alien.y=random.randint(10,990)
    else:
        message='Miss! :(' 
pgzrun.go()
'''