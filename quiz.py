import pgzrun
TITLE='The random Quiz'
WIDTH=1000
HEIGHT=1000
scroll_box=Rect(0,0,1000,150)
question_box=Rect(20,175,750,150)
timer_box=Rect(800,175,180,150)
awnser_box_a=Rect(20,350,350,175)
awnser_box_b=Rect(400,350,350,175)
awnser_box_c=Rect(20,550,350,175)
awnser_box_d=Rect(400,550,350,175)
skip_box=Rect(800,350,180,380)
score=0
total_time=10
question_file='questions.txt'
game_over=False
quest=[]
total_questions=0
current_question=0
boxes=[awnser_box_a,awnser_box_b,awnser_box_c,awnser_box_d]
scroller_msg=''
def draw():
    global scroller_msg
    screen.clear()
    screen.fill('Black')
    screen.draw.filled_rect(scroll_box,'black')
    screen.draw.filled_rect(question_box,'thistle')
    screen.draw.filled_rect(timer_box,'darkolivegreen')
    screen.draw.filled_rect(awnser_box_a,'firebrick')
    screen.draw.filled_rect(awnser_box_b,'royalblue')
    screen.draw.filled_rect(awnser_box_c,'gold')
    screen.draw.filled_rect(awnser_box_d,'limegreen')
    screen.draw.filled_rect(skip_box,'slategrey')
    scroller_msg=f'Welcome to the quiz! You are on Q:{current_question}/{total_questions}'
    screen.draw.textbox(scroller_msg,scroll_box,color='oldlace')
    screen.draw.textbox(str(total_time),timer_box,color='goldenrod')
    screen.draw.textbox('Skip',skip_box,color='darkorchid',angle=-90)
    screen.draw.textbox(readqs[0],question_box,color='black')
    index=1
    for i in boxes:
        screen.draw.textbox(readqs[index].strip(),i,color='black')
        index+=1
def scrolling():
    scroll_box.x-=2
    if scroll_box.right<0:
        scroll_box.left=WIDTH
def update():
    scrolling()
def text():
    global total_questions,quest
    with open('questions.txt','r')as f:
        for i in f:
            quest.append(i)
            total_questions+=1
def read():
    global current_question,quest
    current_question+=1
    return quest.pop(0).split('|')
def on_mouse_down(pos):
    index=1
    for i in boxes:
        if i.collidepoint(pos):
            if index is int(readqs[5]):
                corrrectawnser() 
            else:
                done()
        index+=1
    if skip_box.collidepoint(pos):
        skip()
def corrrectawnser():
    global quest,total_time,score,readqs
    score+=1
    if quest:
        readqs=read()
        total_time=10
    else:
        done()
def done():
    global game_over,score,nextqs,total_time
    msg=f'Game over, you got:{score} questions correct!'
    nextqs=[msg,'~','~','~','~',5]
    total_time=0
    game_over=True
def timer():
    global total_time
    if total_time:
        total_time-=1
    else:
        done()
def skip():
    global readqs,timer
    if quest and not game_over:
        readqs=read()
        timer=10
    else:
        done()
text()
readqs=read()
clock.schedule_interval(timer,1)
pgzrun.go()
