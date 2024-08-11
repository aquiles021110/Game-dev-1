import pgzrun,random
WIDTH=800
HEIGHT=600
end=False
done=False
Totallvl=10
speed=10
objects=['purple_star','red_star','yellow_star','yellow_star2','blu_star']
items=[]
animations=[]
currentlvl=1
def draw():
    global items
    screen.clear()
    screen.blit('space',(0,0))
    if end:
        screen.draw.text('You lost :(',center=(400,50),fontsize=40,color='red')
    elif done:
        screen.draw.text('You WIN :)',center=(400,50),fontsize=40,color='blue')
    else:
        for i in items:
            i.draw()
def update():
    global items,currentlvl
    if len(items)==0:
        items=item_maker(currentlvl)
def item_maker(num_items):
    items_to_create=items_to_create1(num_items)
    picture_apply=picture_apply1(items_to_create)
    layout_items(picture_apply)
    animate_items(picture_apply)
    return picture_apply
def items_to_create1(num_items):
    items_to_create=['satelite']
    for i in range(num_items):
        rand_item=random.choice(objects)
        items_to_create.append(rand_item)
    return items_to_create
def picture_apply1(items_to_create):
    picture_apply=[]
    for i in items_to_create:
        img=Actor(i)
        picture_apply.append(img)
    return picture_apply
def layout_items(layout_itm):
    num_gaps=len(layout_itm)+1
    gap_size=WIDTH/num_gaps
    random.shuffle(layout_itm)
    for index,item in enumerate(layout_itm):
        xpos=index*gap_size
        item.x=xpos
def animate_items(animating_itm):
    global animations
    for i in animating_itm:
        duration=speed-currentlvl
        i.anchor=('center','bottom')
        animation=animate(i,duration=duration,on_finished=game_over,y=HEIGHT)
        animations.append(animation)
def game_over():
    global end
    end=True
def game_complete():
    global done,Totallvl,animations,items,currentlvl
    stop_animations(animations)
    if currentlvl==Totallvl:
        done=True
    else:
        done=False
        currentlvl+=1
        items=[]
        animations=[]
def stop_animations(animations_to_stop):
    for i in animations_to_stop:
        if i.running:
            i.stop()
def on_mouse_down(pos):
    global game_over,game_complete,items
    for i in items:
        if i.collidepoint(pos):
            if 'satelite'in i.image:
                game_complete()
            else:
                game_over()
pgzrun.go()