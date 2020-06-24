import pygame as pg
import time,random,sys
pg.init()

blackcol=(227,20,20)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_red=(255,0,0)
bright_green=(0,255,0)
bright_blue=(0,0,255)
color=(33,31,30)
display_width=800
display_height=600
pause=True

gamedisplay=pg.display.set_mode((display_width,display_height))
pg.display.set_caption("Vineeth vilayattu")
clock=pg.time.Clock()
carimg=pg.image.load('car.png')
grass=pg.image.load('gr.jpeg')
strip=pg.image.load('wh.jpeg')
yellow=pg.image.load('yelllow.png')
car_width=75
intro_background=pg.image.load('bc.jpeg')
instruction_background=pg.image.load('bc1.jpeg')


def introduction():
    introduction=True
    while introduction:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
                sys.exit()
        gamedisplay.blit(instruction_background,(0,0))
        largetext=pg.font.Font('freesansbold.ttf',80)
        smalltext=pg.font.Font('freesansbold.ttf',20)
        mediumtext=pg.font.Font('freesansbold.ttf',40)
        textSurf,textRect=text_objects('This is a car game in which you need dodge the coming cars',smalltext)
        textRect.center=((350),(200))
        TextSurf,TextRect=text_objects('INSTRUCTION',mediumtext)
        TextRect.center=((400),(250))
        gamedisplay.blit(TextSurf,TextRect)
        gamedisplay.blit(textSurf,textRect)
        stextSurf,stextRect=text_objects('ARROW LEFT : LEFT TURN',smalltext)
        stextRect.center=((150),(400))
        htextSurf,htextRect=text_objects('ARROW RIGHT : RIGHT TURN',smalltext)
        htextRect.center=((150),(450))
        atextSurf,atextRect=text_objects('A : ACCELERATOR',smalltext)
        atextRect.center=((150),(500))
        rtextSurf,rtextRect=text_objects('B : BRAKE',smalltext)
        rtextRect.center=((150),(550))
        ptextSurf,ptextRect=text_objects('P : PAUSE',smalltext)
        ptextRect.center=((150),(350))
        s1textSurf,s1textRect=text_objects('CONTROLS',smalltext)
        s1textRect.center=((150),(280))
        gamedisplay.blit(stextSurf,stextRect)
        gamedisplay.blit(s1textSurf,s1textRect)
        gamedisplay.blit(htextSurf,htextRect)
        gamedisplay.blit(atextSurf,atextRect)
        gamedisplay.blit(rtextSurf,rtextRect)
        gamedisplay.blit(ptextSurf,ptextRect)
        button('BACK',600,450,100,50,blue,bright_blue,'menu')
        pg.display.update()
        clock.tick(30)
def intro_loop():
    intro=True
    while intro:
        for event in pg.event.get():
            if event.type==pg.QUIT:
                pg.quit()
                quit()
                sys.exit()
        gamedisplay.blit(intro_background,(0,0))
        largetext=pg.font.Font('freesansbold.ttf',50)
        Textsurf,Textrect=text_objects('Vineeth vilayattu',largetext)
        Textrect.center=(400,100)
        gamedisplay.blit(Textsurf,Textrect)
        button('START',150,520,100,50,green,bright_green,'play')
        button('QUIT',550,520,100,50,red,bright_red,'quit')
        button('INSTRUCTION',300,520,200,50,blue,bright_blue,'intro')
        pg.display.update()
        clock.tick(50)

def paused():
    global pause
    pause=True
    while pause:
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                pg.quit()
                quit()
                sys.exit()
        print(pause)
        gamedisplay.blit(instruction_background,(0,0))
        smalltext=pg.font.Font('freesansbold.ttf',115)
        textsurf,textrect=text_objects('PAUSED',smalltext)
        textrect.center=((display_width/2),(display_height/2))
        gamedisplay.blit(textsurf,textrect)
        button('CONTINUE',150,450,150,50,green,bright_green,'unpause')
        button('RESTART',350,450,150,50,blue,bright_blue,'play')
        button('MAIN MENU',550,450,200,50,red,bright_red,'menu')
        pg.display.update()
        clock.tick(30)
    

def unpaused():
    global pause
    pause=False


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pg.mouse.get_pos()
    click=pg.mouse.get_pressed()
    if  x+w>mouse[0]>x and action!=None:
        pg.draw.rect(gamedisplay,ac,(x,y,w,h))
        if click[0]==1 and action!=None:
            if action=='play':
                game_loop()
            elif action=='quit':
                pg.quit()
                quit()
                sys.exit()
            elif action=='intro':
                introduction()
            elif action=='menu':
                intro_loop()
            elif action=='pause':
                paused()
            elif action=='unpause':
                unpaused()
        else:
            pg.draw.rect(gamedisplay,ic,(x,y,w,h))
        smalltext=pg.font.Font('freesansbold.ttf',20)
        textsurf,textrect=text_objects(msg,smalltext)
        textrect.center=((x+(w/2)),(y+(h/2)))
        gamedisplay.blit(textsurf,textrect)

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pg.image.load('car1.png')
    elif obs==1:
        obs_pic=pg.image.load('car2.png')
    elif obs==2:
        obs_pic=pg.image.load('car3.png')
    gamedisplay.blit(obs_pic,(obs_startx,obs_starty))


def score_system(passed,score):
    font=pg.font.SysFont(None,25)
    text=font.render('Passed :'+str(passed),True,black)
    score=font.render('Score :'+str(score),True,blackcol)
    gamedisplay.blit(text,(0,50))
    gamedisplay.blit(score,(0,30))

def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()
def message_display(text):
    largetext=pg.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(display_height/2))
    gamedisplay.blit(textsurf,textrect)
    pg.display.update()
    time.sleep(3)
    game_loop()
def crash():
    message_display("CRASHED")
def background():
    gamedisplay.blit(grass,(0,0))
    gamedisplay.blit(grass,(700,0))
    gamedisplay.blit(strip,(110,0))
    gamedisplay.blit(strip,(680,0))
    gamedisplay.blit(yellow,(395,500))
    gamedisplay.blit(yellow,(395,400))
    gamedisplay.blit(yellow,(395,300))
    gamedisplay.blit(yellow,(395,200))
    gamedisplay.blit(yellow,(395,100))
    gamedisplay.blit(yellow,(395,0))
def car(x,y):
    gamedisplay.blit(carimg,(x,y))

def game_loop():
    global pause
    x=(250)
    y=(440)
    x_change=0
    obstacle_speed=9
    obs=1
    y_change=0
    obs_startx=random.randrange(200,(display_width-200))
    obs_starty=-750
    obs_width=75
    obs_height=75
    passed=0
    level=0
    score=0
    bumped=False
    while not bumped:
        for event in pg.event.get():
            if event.type== pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x_change=-5
                if event.key == pg.K_RIGHT:
                    x_change=5
                if event.key == pg.K_a:
                    obstacle_speed+=2
                if event.key==pg.K_b:
                    obstacle_speed-=2
                
            if event.type == pg.KEYUP:
                if event.key==pg.K_RIGHT or event.key == pg.K_LEFT:
                    x_change=0
        x+=x_change
        gamedisplay.fill(color)
        background()
        obs_starty-=obstacle_speed/4
        obstacle(obs_startx,obs_starty,obs)
        obs_starty+=obstacle_speed
        car(x,y)
        score_system(passed,score)
        if x<75 or x>563:
            crash()
            #bumped=True
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(76,513)
            obs=random.randrange(0,3)
            passed=passed+1
            score=passed*10
            if int(passed)%10==0:
                level+=1
                obstacle_speed+=2
                largetext=pg.font.Font("freesansbold.ttf",80)
                textsurf,textrect=text_objects('LEVEL'+str(level),largetext)
                textrect.center=((display_width/2),(display_height/2))
                gamedisplay.blit(textsurf,textrect)
                pg.display.update()
                time.sleep(3)
        if y<=obs_starty+146:
            if x>obs_startx and x < obs_startx+75:
                #print(1,x,obs_startx,obs_startx+75)
                crash()
            if x+75 > obs_startx and x+75 < obs_startx+obs_width:
                #print(2,x,obs_startx,obs_startx+110)
                crash()
        button('Pause',650,0,150,50,blue,bright_blue,'pause')
        pg.display.update()
        clock.tick(60)
intro_loop()
game_loop()