#-*- coding: utf-8 -*-
import pygame
import os
import sys
import time
import io
import week1
import week2
import week3
from Functions.L_A import L_A
pygame.init()
pygame.mixer.init()
pygame.mixer.pre_init(44100,-16,2,2048)
vn=pygame.mixer.Sound('Music/visual novel.wav')
romante=pygame.mixer.Sound('Music/Romantic.wav')
buttonsn=pygame.mixer.Sound('Music/Button.wav')
pytcls=pygame.mixer.Sound('Music/pythonclass.wav')
vn.stop()
romante.stop()
buttonsn.stop()
pytcls.stop()
def rrs(file):
    with io.open(file,'r',encoding='utf8') as ri1:
        rir=ri1.readline()[:-1]
    ri1.close()
    print(rir)
    return rir
def relvpointrec(point,filenumber,target):
    if filenumber==1:
        if target==0:
            with io.open('Data/Relation1.txt','r',encoding='utf8') as rpr1:
                rpr=rpr1.readline()[:-1]
                temp1=rpr1.readline()
            rpr1.close()
            with io.open('Data/Relation1.txt','w',encoding='utf8') as rpr2:
                res=str(int(110)+int(point))+str("\n")+str(temp1)
                rpr2.write(res)
            rpr2.close()
        if target==1:
            with io.open('Data/Relation1.txt','r',encoding='utf8') as rpr1:
                temp1=rpr1.readline()
                rpr=rpr1.readline()[:-1]
            rpr1.close()
            with io.open('Data/Relation1.txt','w',encoding='utf8') as rpr2:
                res=str(temp1)+str(int(40)+int(point))+str("\n")
                rpr2.write(res)
            rpr2.close()
    if filenumber==2:
        if target==0:
            with io.open('Data/Relation2.txt','r',encoding='utf8') as rpr1:
                rpr=rpr1.readline()[:-1]
                temp1=rpr1.readline()
            rpr1.close()
            with io.open('Data/Relation2.txt','w',encoding='utf8') as rpr2:
                res=str(int(rpr)+int(point))+str("\n")+str(temp1)
                rpr2.write(res)
            rpr2.close()
        if target==1:
            with io.open('Data/Relation2.txt','r',encoding='utf8') as rpr1:
                temp1=rpr1.readline()
                rpr=rpr1.readline()[:-1]
            rpr1.close()
            with io.open('Data/Relation2.txt','w',encoding='utf8') as rpr2:
                res=str(temp1)+str(int(rpr)+int(point))+str("\n")
                rpr2.write(res)
            rpr2.close()
    if filenumber==3:
        if target==0:
            with io.open('Data/Relation3.txt','r',encoding='utf8') as rpr1:
                rpr=rpr1.readline()[:-1]
                temp1=rpr1.readline()
            rpr1.close()
            with io.open('Data/Relation3.txt','w',encoding='utf8') as rpr2:
                res=str(int(rpr)+int(point))+str("\n")+str(temp1)
                rpr2.write(res)
            rpr2.close()
        if target==1:
            with io.open('Data/Relation3.txt','r',encoding='utf8') as rpr1:
                temp1=rpr1.readline()
                rpr=rpr1.readline()[:-1]
            rpr1.close()
            with io.open('Data/Relation3.txt','w',encoding='utf8') as rpr2:
                res=str(temp1)+str(int(rpr)+int(point))+str("\n")
                rpr2.write(res)
            rpr2.close()
def img_fadin(temparea,imgarea,bgimg,x,y,Display,speed=None):
    if speed==None:
        speed=10
    a=int(255/speed)+int(1)
    for i in range(0,a):
        pygame.event.clear()
        Display.blit(bgimg,(0,0))
        imgarea.blit(Display,(-x,-y))
        imgarea.blit(temparea,(0,0))
        imgarea.set_alpha(i*speed)
        Display.blit(imgarea,(x,y))
        pygame.display.update()
    pygame.event.clear()
    Display.blit(bgimg,(0,0))
    Display.blit(temparea,(x,y))
    pygame.display.update()
def img_fadout(temparea,imgarea,bgimg,x,y,Display,speed=None):
    if speed==None:
        speed= -10
    for i in range(255,-1,speed):
        pygame.event.clear()
        Display.blit(bgimg,(0,0))
        imgarea.blit(Display,(-x,-y))
        imgarea.blit(temparea,(0,0))
        imgarea.set_alpha(i)
        Display.blit(imgarea,(x,y))
        pygame.display.update()
    pygame.event.clear()
    Display.blit(bgimg,(0,0))
    #Display.blit(temparea,(x,y))
    pygame.display.update()
def text_objects(text,fonts,color):
    Fonts=pygame.font.Font('Fonts/NanumGothic.ttf',30)
    textSurface=Fonts.render(text,True,color)
    return textSurface,textSurface.get_rect()
def texting(textfile,Fonts,font_size,x_pos,y_pos,speed,Display,Record=0):
    global text_objects
    c=len(textfile)
    Texts=pygame.font.Font(Fonts,font_size)
    for k in range(c):
        pygame.event.clear()
        TextSurf,TextRect=text_objects(textfile[k],Texts,(0,0,0))
        TextRect.center=(x_pos+font_size/2,y_pos+font_size/2)
        Display.blit(TextSurf,TextRect)
        pygame.display.update()
        pygame.time.delay(speed-10)
        x_pos +=(font_size/2 + 10)
def savtemp(trig,textfile=None):
    if textfile==None:
        textfile='Data/Save.txt'
    with io.open('Data/Save.txt','w',encoding='utf8') as ws1:
        ws1.write(str(trig)+"\n")
    ws1.close()
def rdtemp(textfile=None):
    if textfile==None:
        textfile='Data/Save.txt'
    with io.open('Data/Save.txt','r',encoding='utf8') as rf1:
        rfc=rf1.readline()[:-1]
    rf1.close()
    return rfc
def paused(msg,Fonts,font_size,width,height,Display):
    print("Pausing")
    global button04
    global text_objects
    global unpause
    global quitgame
    pygame.mixer.pause()
    img01=pygame.image.load(os.path.abspath('Images/pause 1.png'))
    img01.set_alpha(64)
    temp01=pygame.image.load(os.path.abspath('Images/ButtonImg/continue.png')).convert_alpha()
    temp02=pygame.image.load(os.path.abspath('Images/ButtonImg/main.png')).convert_alpha()
    temp03=pygame.image.load(os.path.abspath('Images/ButtonImg/quit.png')).convert_alpha()
    Display.blit(img01,(0,0))
    largeText=pygame.font.Font(Fonts,font_size)
    TextSurf,TextRect=text_objects(msg,largeText,(0,0,128))
    TextRect.center=((width/2),(height/2-160))
    Display.blit(TextSurf,TextRect)
    click=pygame.mouse.get_pressed()
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quitgame()
        button04(Display,temp01,80,213,225,294,unpause)
        button04(Display,temp02,528,213,224,294,main)
        button04(Display,temp03,975,213,225,294,quitgame)
        pygame.display.update()
        pygame.time.delay(50)
def unpause():
    global pause
    pygame.mixer.unpause()
    pause=False
def button01(msg,Display,x_pos,y_pos,width,height,o_color,c_color,action=None):
    global text_objects
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_pos+width>mouse[0]>x_pos and y_pos+height>mouse[1]>y_pos:
        pygame.draw.rect(Display,c_color,(x_pos,y_pos,width,height))
        if click[0]==1 and action !=None:
            action()
    else:
        pygame.draw.rect(Display,o_color,(x_pos,y_pos,width,height))
    smallText=pygame.font.Font('Fonts/NanumGothic.ttf',20)
    textSurf,textRect=text_objects(msg,smallText,(255,255,255))
    textRect.center=((x_pos+(width/2)),(y_pos+(height/2)))
    Display.blit(textSurf,textRect)
def button02(msg,Display,x_pos,y_pos,width,height,image,action=None):
    global text_objects
    img=pygame.image.load(os.path.abspath(image)).convert_alpha()
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_pos+width>mouse[0]>x_pos and y_pos+height>mouse[1]>y_pos:
        Display.blit(img,(x_pos,y_pos))
        pygame.display.update()
        if click[0]==1 and action !=None:
            action()
    else:
        Display.blit(img,(x_pos,y_pos))
        pygame.display.update()
    smallText=pygame.font.Font('Fonts/NanumGothic.ttf',20)
    textSurf,textRect=text_objects(msg,smallText,(255,255,255))
    textRect.center=((x_pos+(width/2)),(y_pos+(height/2)))
    Display.blit(textSurf,textRect)
def button03(Display,bgimg,x_pos,y_pos,width,height,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_pos+width>mouse[0]>x_pos and y_pos+height>mouse[1]>y_pos:
        pygame.display.update()
        if click[0]==1 and action !=None:
            action()
    else:
        Display.blit(bgimg,(0,0))
def button04(Display,imgfile,x_pos,y_pos,width,height,action=None):
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_pos+width>mouse[0]>x_pos and y_pos+height>mouse[1]>y_pos:
        Display.blit(imgfile,(x_pos,y_pos))
        pygame.display.update()
        if click[0]==1 and action !=None:
            action()
    else:
        Display.blit(imgfile,(x_pos,y_pos))
        pygame.display.update()
def buttonA(Display,x_pos,y_pos,action=None):
    tA=pygame.image.load(os.path.abspath('Images/ButtonImg/A.png')).convert_alpha()
    width=136
    height=136
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_pos+width>mouse[0]>x_pos and y_pos+height>mouse[1]>y_pos:
        Display.blit(tA,(x_pos,y_pos))
        pygame.display.update()
        if click[0]==1 and action !=None:
            action()
    else:
        Display.blit(tA,(x_pos,y_pos))
        pygame.display.update()
def buttonB(Display,x_pos,y_pos,action=None):
    tB=pygame.image.load(os.path.abspath('Images/ButtonImg/B.png')).convert_alpha()
    width=136
    height=136
    mouse=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x_pos+width>mouse[0]>x_pos and y_pos+height>mouse[1]>y_pos:
        Display.blit(tB,(x_pos,y_pos))
        pygame.display.update()
        if click[0]==1 and action !=None:
            action()
    else:
        Display.blit(tB,(x_pos,y_pos))
        pygame.display.update()
def crs():
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    pytcls.play()
    def img_fadoutA(temparea,imgarea,bgimg,x,y,Display,speed=None):
        if speed==None:
            speed= -10
        for i in range(255,-1,speed):
            pygame.event.clear()
            Display.blit(bgimg,(0,0))
            imgarea.blit(Display,(-x,-y))
            imgarea.blit(temparea,(0,-2700))
            imgarea.set_alpha(i)
            Display.blit(imgarea,(x,y))
            pygame.display.update()
        pygame.event.clear()
        Display.blit(bgimg,(0,0))
        #Display.blit(temparea,(x,y))
        pygame.display.update()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("크레딧")
    temp1=pygame.image.load(os.path.abspath('Images/BackgroundImg/blackscreen.png')).convert()
    crd=pygame.image.load(os.path.abspath('Images/Credit.png')).convert()
    bwaeqw=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameDisplay.blit(temp1,(0,0))
    for i in range(3000):
        gameDisplay.blit(crd,(0,300-i))
        pygame.display.update()
        pygame.event.clear()
        pygame.time.delay(10)
    img_fadoutA(crd,bwaeqw,temp1,0,0,gameDisplay,-2)
    main()
def quitgame():
    pygame.display.quit()
    pygame.quit()
    sys.exit()
def reseter():
    with io.open('Data/Unlocked.txt','w',encoding='utf8') as nl1:
        nl1.write("1\n0\n0\n0\n")
    nl1.close()
    with io.open('Data/Relation1.txt','w',encoding='utf8') as qwra1:
        qwra1.write("110\n40\n")
    qwra1.close()
    with io.open('Data/Relation2.txt','w',encoding='utf8') as qwra2:
        qwra2.write("110\n40\n")
    qwra2.close()
    with io.open('Data/Relation3.txt','w',encoding='utf8') as qwra3:
        qwra3.write("110\n40\n")
    qwra3.close()
    with io.open('Data/PF.txt','w',encoding='utf8') as qwb1:
        qwb1.write("0\n")
    qwb1.close()
    load_screen()
def load_screen():
    global quitgame
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Load Screen")
    img01=pygame.image.load(os.path.abspath('Images/Sources/loadback.png')).convert()
    img02=pygame.image.load(os.path.abspath('Images/BackgroundImg/mainscreen.png')).convert()
    temp01=pygame.image.load(os.path.abspath('Images/Sources/load 4.png')).convert_alpha()
    temp02=pygame.image.load(os.path.abspath('Images/Sources/load 5.png')).convert_alpha()
    temp03=pygame.image.load(os.path.abspath('Images/Sources/load 6.png')).convert_alpha()
    temp04=pygame.image.load(os.path.abspath('Images/Sources/load 1.png')).convert_alpha()
    temp05=pygame.image.load(os.path.abspath('Images/Sources/load 2.png')).convert_alpha()
    temp06=pygame.image.load(os.path.abspath('Images/Sources/load 3.png')).convert_alpha()
    temp07=pygame.image.load(os.path.abspath('Images/Sources/reset.png')).convert_alpha()
    temp08=pygame.image.load(os.path.abspath('Images/Sources/return.png')).convert_alpha()
    temp09=pygame.image.load(os.path.abspath('Images/Sources/quit.png')).convert_alpha()
    img01.set_alpha(128)
    gameDisplay.blit(img02,(0,0))
    gameDisplay.blit(img01,(0,0))
    pygame.display.update()
    gameExit=False
    with io.open('Data/Unlocked.txt','r',encoding='utf8') as nl1:
        a=nl1.readlines()[0][:-1]
    with io.open('Data/Unlocked.txt','r',encoding='utf8') as nl2:
        b=nl2.readlines()[1][:-1]
    with io.open('Data/Unlocked.txt','r',encoding='utf8') as nl3:
        c=nl3.readlines()[2][:-1]
    with io.open('Data/Unlocked.txt','r',encoding='utf8') as nl4:
        d=nl4.readlines()[3][:-1]
    nl1.close()
    nl2.close()
    nl3.close()
    nl4.close()
    trigger=0
    if a=='1' and b=='0' and c=='0':
        #1st open
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quitgame()
            button04(gameDisplay,temp01,100,280,246,200,phase0)
            button04(gameDisplay,temp05,490,280,246,200)
            button04(gameDisplay,temp06,900,280,246,200)
            button04(gameDisplay,temp07,140,600,300,72,reseter)
            button04(gameDisplay,temp08,840,600,300,72,main)
            button04(gameDisplay,temp09,503,620,275,66,quitgame)
            pygame.display.update()
            pygame.time.delay(10)
    if a=='1' and b=='1' and c=='0':
        #1st and 2nd open
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quitgame()
            button04(gameDisplay,temp01,100,280,246,200,phase0)
            button04(gameDisplay,temp02,490,280,246,200,phase1)
            button04(gameDisplay,temp06,900,280,246,200)
            button04(gameDisplay,temp07,140,600,300,72,reseter)
            button04(gameDisplay,temp08,840,600,300,72,main)
            button04(gameDisplay,temp09,503,620,275,66,quitgame)
            pygame.display.update()
            pygame.time.delay(10)
    if a=='1' and b=='1' and c=='1' and d=='1':
        #1st and 2nd and 3_1 open
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quitgame()
            button04(gameDisplay,temp01,100,280,246,200,phase0)
            button04(gameDisplay,temp02,490,280,246,200,phase1)
            button04(gameDisplay,temp03,900,280,246,200,phase2_1)
            button04(gameDisplay,temp07,140,600,300,72,reseter)
            button04(gameDisplay,temp08,840,600,300,72,main)
            button04(gameDisplay,temp09,503,620,275,66,quitgame)
            pygame.display.update()
            pygame.time.delay(10)
    if a=='1' and b=='1' and c=='1':
        #1st and 2nd and 3rd open
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quitgame()
            button04(gameDisplay,temp01,100,280,246,200,phase0)
            button04(gameDisplay,temp02,490,280,246,200,phase1)
            button04(gameDisplay,temp03,900,280,246,200,phase2)
            button04(gameDisplay,temp07,140,600,300,72,reseter)
            button04(gameDisplay,temp08,840,600,300,72,main)
            button04(gameDisplay,temp09,503,620,275,66,quitgame)
            pygame.display.update()
            pygame.time.delay(10)
    else:
        print("Error: Can't read \"Unlocked.txt\" file correctly")
        main()
    if gameExit==True:
        quitgame()
def main():
    global button01
    global button02
    global button03
    global quitgame
    global executing_text
    global load_screen
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    romante.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Title screen")
    background01=pygame.image.load(os.path.abspath('Images/BackgroundImg/mainscreen.png')).convert()
    gameDisplay.blit(background01,(0,0))
    pygame.display.update()
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
        pygame.display.update()
        button03(gameDisplay,background01,31,153,273,64,phase0)
        button03(gameDisplay,background01,31,271,273,64,load_screen)
        button03(gameDisplay,background01,31,387,273,64,crs)
        button03(gameDisplay,background01,31,503,273,64,quitgame)
        pygame.display.update()
        pygame.time.delay(50)
    if gameExit==True:
        quitgame()
def phase0():
    global button01
    global quitgame
    global pause
    global loading_text
    global choice01
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    pytcls.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("1 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/03.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp6=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 2.png')).convert_alpha()
    temp7=pygame.image.load(os.path.abspath('Images/GFImg/good 1.png')).convert_alpha()
    temp8=pygame.image.load(os.path.abspath('Images/GFImg/good 2.png')).convert_alpha()
    temp9=pygame.image.load(os.path.abspath('Images/GFImg/confident 1.png')).convert_alpha()
    temp10=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g1.png')).convert_alpha()
    temp11=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g2.png')).convert_alpha()
    temp12=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_c1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    playertext1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    proftext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    gfname1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    playername1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    profname1=pygame.Surface((temp6.get_width(),temp6.get_height())).convert()
    gfg1=pygame.Surface((temp7.get_width(),temp7.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',360,display_width,display_height,gameDisplay)
                if trigger==22:
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==21:
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==20:
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==19:
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==18:
                    gameDisplay.blit(temp11,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==17:
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp5,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==16:
                    gameDisplay.blit(temp12,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp12,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==15:
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp5,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==14:
                    gameDisplay.blit(temp11,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==13:
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==12:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    gameDisplay.blit(playertext1,(192,500))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==11:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==7:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:14],'Fonts/NanumGothic.ttf',40,215,555,50,gameDisplay)
                    texting(u_1_01[14:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==22:
                    choice01()
                if trigger==21:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[21]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==20:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[20]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==19:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[19]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==18:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[18]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==17:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[17]
                    t_1_01.close()
                    gameDisplay.blit(temp11,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==16:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[16]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp5,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==15:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[15]
                    t_1_01.close()
                    gameDisplay.blit(temp12,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp12,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==14:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[14]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp5,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==13:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[13]
                    t_1_01.close()
                    gameDisplay.blit(temp11,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==12:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[12]
                    t_1_01.close()
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp4,(0,0))
                    gfname1.set_alpha(196)
                    img_fadin(temp7,gfg1,background2,500,0,gameDisplay)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==11:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[11]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    gameDisplay.blit(playertext1,(192,500))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==10:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[10]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==9:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[9]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==8:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[8]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==7:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[7]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==6:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[6]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==5:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[5]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==4:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[4]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==3:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[3]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==2:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[2]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:14],'Fonts/NanumGothic.ttf',40,215,555,50,gameDisplay)
                    texting(u_1_01[14:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==1:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[1]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
                if trigger==0:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/01.txt','r',encoding='utf8') as t_1_01:
                        u_1_01=t_1_01.readlines()[0]
                    t_1_01.close()
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(u_1_01[:-1],'Fonts/NanumGothic.ttf',40,215,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def choice01():
    print("Phase 1C")
    global buttonA
    global buttonB
    global quitgame
    global pause
    global loading_text
    global phase01_1
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("1 주차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/03.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/GFImg/good 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameDisplay.blit(temp3,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp1,(0,0))
    playertext1.set_alpha(196)
    gameDisplay.blit(temp3,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    with io.open('Scripts/Phase0/c01.txt','r',encoding='utf8') as se1:
        sen1=se1.readline()[:-1]
        sen2=se1.readline()[:-1]
        sen3=se1.readline()[:-1]
    se1.close()
    texting(sen1,'Fonts/NanumGothic.ttf',40,205,530,50,gameDisplay)
    texting(sen2,'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    texting(sen3,'Fonts/NanumGothic.ttf',40,205,630,50,gameDisplay)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                gameDisplay.blit(temp3,(0,0))
                playertext1.blit(temp1,(0,0))
                playertext1.set_alpha(196)
                gameDisplay.blit(temp3,(0,0))
                gameDisplay.blit(playertext1,(192,500))
                texting(sen1,'Fonts/NanumGothic.ttf',40,205,530,0,gameDisplay)
                texting(sen2,'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                texting(sen3,'Fonts/NanumGothic.ttf',40,205,630,0,gameDisplay)
            buttonA(gameDisplay,120,125,phase01_1)
            buttonB(gameDisplay,1024,125,phase01_2)
        pygame.display.update()
        pygame.time.delay(50)
    if gameExit==True:
        quitgame()
def phase01_1():
    print("Phase 1-A")
    global button01
    global quitgame
    global pause
    global loading_text
    global relvpointrec
    relvpointrec(-10,1,0)
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("1 주차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/03.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/good 1.png')).convert_alpha()
    temp6=pygame.image.load(os.path.abspath('Images/GFImg/good 2.png')).convert_alpha()
    temp7=pygame.image.load(os.path.abspath('Images/GFImg/lower 1.png')).convert_alpha()
    temp8=pygame.image.load(os.path.abspath('Images/GFImg/angry 1.png')).convert_alpha()
    temp9=pygame.image.load(os.path.abspath('Images/GFImg/angry 2.png')).convert_alpha()
    temp10=pygame.image.load(os.path.abspath('Images/GFImg/huffy 1.png')).convert_alpha()
    temp11=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g1.png')).convert_alpha()
    temp12=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g2.png')).convert_alpha()
    temp13=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_l1.png')).convert_alpha()
    temp14=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_a1.png')).convert_alpha()
    temp15=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_a2.png')).convert_alpha()
    temp16=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_h1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    playertext1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    gfname1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gameDisplay.blit(temp11,(0,0))
    pygame.display.update()
    trigger=0
    trigger +=1
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[0]
    se1.close()
    gameDisplay.blit(temp11,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp2,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(temp11,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp11,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp12,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp12,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp16,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp16,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp16,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp16,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp15,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp15,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp14,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp14,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp13,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp13,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp11,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==8:
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    pygame.mouse.set_pos([100,50])
                    week1.initGame()
                    pygame.event.clear()
                    pygame.display.quit()
                    a=rrs('Data/PF.txt')
                    phase1()
                if trigger==7:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[7]
                    se1.close()
                    gameDisplay.blit(temp11,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[6]
                    se1.close()
                    gameDisplay.blit(temp12,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp12,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[5]
                    se1.close()
                    gameDisplay.blit(temp16,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp16,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[4]
                    se1.close()
                    gameDisplay.blit(temp16,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp16,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[3]
                    se1.close()
                    gameDisplay.blit(temp15,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp15,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[2]
                    se1.close()
                    gameDisplay.blit(temp14,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp14,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[1]
                    se1.close()
                    gameDisplay.blit(temp13,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp13,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[0]
                    se1.close()
                    gameDisplay.blit(temp11,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp11,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase01_2():
    print("Phase 1-B")
    global button01
    global quitgame
    global pause
    global loading_text
    global relvpointrec
    relvpointrec(10,1,0)
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("1 주차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/03.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/good 1.png')).convert_alpha()
    temp6=pygame.image.load(os.path.abspath('Images/GFImg/good 2.png')).convert_alpha()
    temp7=pygame.image.load(os.path.abspath('Images/GFImg/confident 1.png')).convert_alpha()
    temp8=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g1.png')).convert_alpha()
    temp9=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_g2.png')).convert_alpha()
    temp10=pygame.image.load(os.path.abspath('Images/BackgroundImg/03_c1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    playertext1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    gfname1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    trigger +=1
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase0/03.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[0]
    se1.close()
    gameDisplay.blit(temp9,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp2,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(temp9,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp8,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp8,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(temp9,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp9,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==3:
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    pygame.mouse.set_pos([100,50])
                    week1.initGame()
                    pygame.event.clear()
                    pygame.display.quit()
                    a=rrs('Data/PF.txt')
                    phase1()
                if trigger==2:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[2]
                    se1.close()
                    gameDisplay.blit(temp10,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp10,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[1]
                    se1.close()
                    gameDisplay.blit(temp8,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp3,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(temp8,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    trigger +=1
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase0/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[0]
                    se1.close()
                    gameDisplay.blit(temp9,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp2,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(temp9,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase1():
    global button01
    global quitgame
    global pause
    global loading_text
    with io.open('Data/Unlocked.txt','w',encoding='utf8') as mah1:
        mah1.write("1\n1\n0\n0\n")
    mah1.close()
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    pytcls.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 2.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    proftext1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playername1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    profname1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==8:
                    choice02()
                if trigger==7:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def choice02():
    print("Phase 2C")
    global buttonA
    global buttonB
    global quitgame
    global pause
    global loading_text
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp1,(0,0))
    playertext1.set_alpha(196)
    gameDisplay.blit(playertext1,(192,500))
    with io.open('Scripts/Phase1/c02.txt','r',encoding='utf8') as se1:
        sen1=se1.readline()[:-1]
        sen2=se1.readline()[:-1]
        sen3=se1.readline()[:-1]
        sen4=se1.readline()[:-1]
    se1.close()
    texting(sen1,'Fonts/NanumGothic.ttf',40,205,515,50,gameDisplay)
    texting(sen2,'Fonts/NanumGothic.ttf',40,205,560,50,gameDisplay)
    texting(sen3,'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
    texting(sen4,'Fonts/NanumGothic.ttf',40,205,650,50,gameDisplay)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                gameDisplay.blit(background1,(0,0))
                playertext1.blit(temp1,(0,0))
                playertext1.set_alpha(196)
                gameDisplay.blit(playertext1,(192,500))
                texting(sen1,'Fonts/NanumGothic.ttf',40,205,515,0,gameDisplay)
                texting(sen2,'Fonts/NanumGothic.ttf',40,205,560,0,gameDisplay)
                texting(sen3,'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                texting(sen4,'Fonts/NanumGothic.ttf',40,205,650,0,gameDisplay)
        buttonA(gameDisplay,120,125,phase1_A)
        buttonB(gameDisplay,1024,125,phase1_B)
        pygame.display.update()
        pygame.time.delay(50)
    if gameExit==True:
        quitgame()
def phase1_A():
    global button01
    global quitgame
    global pause
    global loading_text
    print("Phase 1_A")
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 2.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    proftext1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playername1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    profname1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    proftext1.blit(gameDisplay,(-192,-500))
    proftext1.blit(temp2,(0,0))
    proftext1.set_alpha(196)
    profname1.blit(gameDisplay,(-200,-450))
    profname1.blit(temp4,(0,0))
    profname1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(proftext1,(192,500))
    gameDisplay.blit(profname1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==7:
                    relvpointrec(-40,2,1)
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    pygame.mouse.set_pos([100,50])
                    week2.initGame()
                    pygame.event.clear()
                    pygame.display.quit()
                    a=rrs('Data/PF.txt')
                    if a=='0':
                        choice03()
                    else:
                        phase1_3()
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp3,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp2,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase1_B():
    global button01
    global quitgame
    global pause
    global loading_text
    print("Phase 1_B")
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    playername1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase1/03.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp1,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp2,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==2:
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    pygame.mouse.set_pos([100,50])
                    week2.initGame()
                    pygame.event.clear()
                    pygame.display.quit()
                    a=rrs('Data/PF.txt')
                    if a=='0':
                        choice03()
                    else:
                        phase1_3()
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def choice03():
    print("Phase 3C")
    global buttonA
    global buttonB
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    pytcls.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp1,(0,0))
    playertext1.set_alpha(196)
    gameDisplay.blit(playertext1,(192,500))
    with io.open('Scripts/Phase1/c03.txt','r',encoding='utf8') as se1:
        sen1=se1.readline()[:-1]
        sen2=se1.readline()[:-1]
        sen3=se1.readline()[:-1]
    se1.close()
    texting(sen1,'Fonts/NanumGothic.ttf',40,205,530,50,gameDisplay)
    texting(sen2,'Fonts/NanumGothic.ttf',40,205,575,50,gameDisplay)
    texting(sen3,'Fonts/NanumGothic.ttf',40,205,620,50,gameDisplay)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                gameDisplay.blit(background1,(0,0))
                playertext1.blit(temp1,(0,0))
                playertext1.set_alpha(196)
                gameDisplay.blit(playertext1,(192,500))
                texting(sen1,'Fonts/NanumGothic.ttf',40,205,530,0,gameDisplay)
                texting(sen2,'Fonts/NanumGothic.ttf',40,205,575,0,gameDisplay)
                texting(sen3,'Fonts/NanumGothic.ttf',40,205,620,0,gameDisplay)
        buttonA(gameDisplay,120,125,phase1_1)
        buttonB(gameDisplay,1024,125,phase1_2)
        pygame.display.update()
        pygame.time.delay(50)
    if gameExit==True:
        quitgame()
def phase1_1():
    global quitgame
    global pause
    global loading_text
    print("Phase 1_1")
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp3,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==15:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==14:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==13:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==12:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==11:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==10:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==9:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==15:
                    savtemp(0)
                    relvpointrec(-50,2,0)
                    phase2()
                if trigger==14:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==13:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase1_2():
    global button01
    global quitgame
    global pause
    global loading_text
    print("Phase 1_2")
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04.png')).convert()
    backgrounda1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_a1.png')).convert()
    backgrounda2=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_a2.png')).convert()
    backgroundt1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_t1.png')).convert()
    backgroundt2=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_t2.png')).convert()
    backgroundh1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_h1.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/angry 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp3,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==17:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==16:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==15:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==14:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==13:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundt2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:28],'Fonts/NanumGothic.ttf',40,215,545,0,gameDisplay)
                    texting(sen1[29:-1],'Fonts/NanumGothic.ttf',40,215,615,0,gameDisplay)
                if trigger==12:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,215,545,0,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,215,615,0,gameDisplay)
                if trigger==11:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:20],'Fonts/NanumGothic.ttf',40,215,545,0,gameDisplay)
                    texting(sen1[21:-1],'Fonts/NanumGothic.ttf',40,215,615,0,gameDisplay)
                if trigger==10:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==9:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,215,545,0,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,215,615,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==17:
                    savtemp(0)
                    relvpointrec(-30,2,0)
                    phase2()
                if trigger==16:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==15:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==14:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==13:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundt2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:28],'Fonts/NanumGothic.ttf',40,215,545,50,gameDisplay)
                    texting(sen1[29:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==11:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,215,545,50,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==10:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:20],'Fonts/NanumGothic.ttf',40,215,545,50,gameDisplay)
                    texting(sen1[21:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==9:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,215,545,50,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    img_fadin(temp5,gfg1,background1,329,0,gameDisplay)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase1_3():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    romante.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("2 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/05.png')).convert()
    background3=pygame.image.load(os.path.abspath('Images/BackgroundImg/blackscreen.png')).convert()
    backgroundg1=pygame.image.load(os.path.abspath('Images/BackgroundImg/05_g1.png')).convert()
    backgroundg2=pygame.image.load(os.path.abspath('Images/BackgroundImg/05_g2.png')).convert()
    backgroundg3=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_g2.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp6=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 2.png')).convert_alpha()
    temp7=pygame.image.load(os.path.abspath('Images/GFImg/good 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    proftext1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    profname1=pygame.Surface((temp6.get_width(),temp6.get_height())).convert()
    gfg1=pygame.Surface((temp7.get_width(),temp7.get_height())).convert()
    blk1=pygame.Surface((background3.get_width(),background3.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    proftext1.blit(gameDisplay,(-192,-500))
    proftext1.blit(temp5,(0,0))
    proftext1.set_alpha(196)
    profname1.blit(gameDisplay,(-200,-450))
    profname1.blit(temp6,(0,0))
    profname1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(proftext1,(192,500))
    gameDisplay.blit(profname1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==14:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg3,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg3,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==13:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==12:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg3,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg3,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==11:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==10:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:8],'Fonts/NanumGothic.ttf',40,215,545,0,gameDisplay)
                    texting(sen1[9:-1],'Fonts/NanumGothic.ttf',40,215,615,0,gameDisplay)
                if trigger==9:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==14:
                    savtemp(1)
                    relvpointrec(30,2,0)
                    relvpointrec(30,2,1)
                    with io.open('Data/Unlocked.txt','w',encoding='utf8') as mye1:
                        mye1.write("1\n1\n1\n1\n")
                    mye1.close()
                    phase2_1()
                if trigger==13:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg3,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg3,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    img_fadout(backgroundg1,blk1,background3,0,0,gameDisplay)
                    img_fadin(backgroundg3,blk1,background3,0,0,gameDisplay)
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg3,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:8],'Fonts/NanumGothic.ttf',40,215,545,50,gameDisplay)
                    texting(sen1[9:-1],'Fonts/NanumGothic.ttf',40,215,615,50,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    img_fadin(temp7,gfg1,background2,329,0,gameDisplay)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase1/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase2():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    pytcls.play()
    with io.open('Data/Unlocked.txt','w',encoding='utf8') as bnye1:
        bnye1.write("1\n1\n1\n0\n")
    bnye1.close()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 2.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/Sources/prof. 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    playername1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    proftext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    profname1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    pfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    proftext1.blit(gameDisplay,(-192,-500))
    proftext1.blit(temp3,(0,0))
    proftext1.set_alpha(196)
    profname1.blit(gameDisplay,(-200,-450))
    profname1.blit(temp4,(0,0))
    profname1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(proftext1,(192,500))
    gameDisplay.blit(profname1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,560,0,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,205,610,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==10:
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    pygame.mouse.set_pos([100,50])
                    week3.initGame()
                    pygame.event.clear()
                    pygame.display.quit()
                    a=rrs('Data/PF.txt')
                    if a=='0':
                        choice04()
                    else:
                        phase2_2()
                if trigger==9:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,560,50,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,205,610,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase2_1():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    pytcls.play()
    print("Phase 2")
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 2.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/Sources/prof. 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    playername1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    proftext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    profname1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    pfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/01.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    proftext1.blit(gameDisplay,(-192,-500))
    proftext1.blit(temp3,(0,0))
    proftext1.set_alpha(196)
    profname1.blit(gameDisplay,(-200,-450))
    profname1.blit(temp4,(0,0))
    profname1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(proftext1,(192,500))
    gameDisplay.blit(profname1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:18],'Fonts/NanumGothic.ttf',40,205,560,0,gameDisplay)
                    texting(sen1[19:-1],'Fonts/NanumGothic.ttf',40,205,610,0,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,560,0,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,205,610,0,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==10:
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    pygame.mouse.set_pos([100,50])
                    week3.initGame()
                    pygame.event.clear()
                    pygame.display.quit()
                    a=rrs('Data/PF.txt')
                    if a=='0':
                        choice04_1()
                    else:
                        phase2_2()
                if trigger==9:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:18],'Fonts/NanumGothic.ttf',40,205,560,50,gameDisplay)
                    texting(sen1[19:-1],'Fonts/NanumGothic.ttf',40,205,610,50,gameDisplay)
                if trigger==8:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp1,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp2,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,560,50,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,205,610,50,gameDisplay)
                if trigger==4:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/02.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp3,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp4,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def choice04():
    print("Phase 4C")
    global buttonA
    global buttonB
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp1,(0,0))
    playertext1.set_alpha(196)
    gameDisplay.blit(playertext1,(192,500))
    with io.open('Scripts/Phase2/c04.txt','r',encoding='utf8') as se1:
        sen1=se1.readline()[:-1]
        sen2=se1.readline()[:-1]
    se1.close()
    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,530,50,gameDisplay)
    texting(sen1[17:],'Fonts/NanumGothic.ttf',40,205,575,50,gameDisplay)
    texting(sen2,'Fonts/NanumGothic.ttf',40,205,620,50,gameDisplay)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                gameDisplay.blit(background1,(0,0))
                playertext1.blit(temp1,(0,0))
                playertext1.set_alpha(196)
                gameDisplay.blit(playertext1,(192,500))
                texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,530,0,gameDisplay)
                texting(sen1[17:],'Fonts/NanumGothic.ttf',40,205,575,0,gameDisplay)
                texting(sen2,'Fonts/NanumGothic.ttf',40,205,620,0,gameDisplay)
        buttonA(gameDisplay,120,125,phase2_A)
        buttonB(gameDisplay,1024,125,phase2_B)
        pygame.display.update()
        pygame.time.delay(50)
    if gameExit==True:
        quitgame()
def choice04_1():
    print("Phase 4C")
    global buttonA
    global buttonB
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    playertext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp1,(0,0))
    playertext1.set_alpha(196)
    gameDisplay.blit(playertext1,(192,500))
    with io.open('Scripts/Phase2/c04.txt','r',encoding='utf8') as se1:
        sen1=se1.readline()[:-1]
        sen2=se1.readline()[:-1]
    se1.close()
    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,530,50,gameDisplay)
    texting(sen1[17:],'Fonts/NanumGothic.ttf',40,205,575,50,gameDisplay)
    texting(sen2,'Fonts/NanumGothic.ttf',40,205,620,50,gameDisplay)
    pygame.display.update()
    gameExit=False
    while not gameExit:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                gameDisplay.blit(background1,(0,0))
                playertext1.blit(temp1,(0,0))
                playertext1.set_alpha(196)
                gameDisplay.blit(playertext1,(192,500))
                texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,530,0,gameDisplay)
                texting(sen1[17:],'Fonts/NanumGothic.ttf',40,205,575,0,gameDisplay)
                texting(sen2,'Fonts/NanumGothic.ttf',40,205,620,0,gameDisplay)
        buttonA(gameDisplay,120,125,phase2_C)
        buttonB(gameDisplay,1024,125,phase2_D)
        pygame.display.update()
        pygame.time.delay(50)
    if gameExit==True:
        quitgame()
def phase2_A():
    global button01
    global quitgame
    global pause
    global loading_text
    print("Phase 2")
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/08.png')).convert()
    background3=pygame.image.load(os.path.abspath('Images/BackgroundImg/07.png')).convert()
    backgroundl1=pygame.image.load(os.path.abspath('Images/BackgroundImg/07_l1.png')).convert()
    backgroundl2=pygame.image.load(os.path.abspath('Images/BackgroundImg/07_l2.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/lower 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp3,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==34:
                    gameDisplay.blit(background3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==33:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==32:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:17],'Fonts/NanumGothic.ttf',40,205,535,0,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==31:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:12],'Fonts/NanumGothic.ttf',40,205,535,0,gameDisplay)
                    texting(sen1[13:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==30:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==29:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:17],'Fonts/NanumGothic.ttf',40,205,535,0,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==28:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==27:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==26:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==25:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==24:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==23:
                    gameDisplay.blit(background3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==22:
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==21:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==20:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==19:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==18:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==17:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==16:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==15:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==14:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==13:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==12:
                    #################################
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:8],'Fonts/NanumGothic.ttf',40,205,530,0,gameDisplay)
                    texting(sen1[9:20],'Fonts/NanumGothic.ttf',40,205,580,0,gameDisplay)
                    texting(sen1[21:-1],'Fonts/NanumGothic.ttf',40,205,630,0,gameDisplay)
                if trigger==2:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==34:
                    relvpointrec(-70,3,0)
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    crs()
                if trigger==33:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==32:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==31:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:17],'Fonts/NanumGothic.ttf',40,205,535,50,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==30:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:12],'Fonts/NanumGothic.ttf',40,205,535,50,gameDisplay)
                    texting(sen1[13:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==29:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==28:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:17],'Fonts/NanumGothic.ttf',40,205,535,50,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==27:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==26:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==25:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==24:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==23:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==22:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==21:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==20:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==19:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==18:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==17:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==16:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==15:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==14:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==13:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:8],'Fonts/NanumGothic.ttf',40,205,530,50,gameDisplay)
                    texting(sen1[9:20],'Fonts/NanumGothic.ttf',40,205,580,50,gameDisplay)
                    texting(sen1[21:-1],'Fonts/NanumGothic.ttf',40,205,630,50,gameDisplay)
                if trigger==1:
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/05.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase2_B():
    global button01
    global quitgame
    global pause
    global loading_text
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/08.png')).convert()
    background3=pygame.image.load(os.path.abspath('Images/BackgroundImg/07.png')).convert()
    backgrounda1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_a1.png')).convert()
    backgrounda2=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_a2.png')).convert()
    backgroundl1=pygame.image.load(os.path.abspath('Images/BackgroundImg/07_l1.png')).convert()
    backgroundl2=pygame.image.load(os.path.abspath('Images/BackgroundImg/07_l2.png')).convert()
    backgroundl3=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_l1.png')).convert()
    backgroundl4=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_l2.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/lower 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp3,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==38:
                    gameDisplay.blit(background3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==37:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==36:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==35:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==34:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==33:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==32:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==31:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:17],'Fonts/NanumGothic.ttf',40,205,555,50,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==30:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==29:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==28:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==27:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==26:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==25:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==24:
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==23:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==22:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==21:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==20:
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==19:
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==18:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==17:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==16:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==15:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==14:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==13:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(backgroundl3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==38:
                    relvpointrec(-50,3,0)
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    crs()
                if trigger==37:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==36:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==35:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==34:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==33:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==32:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==31:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==30:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:17],'Fonts/NanumGothic.ttf',40,205,555,50,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==29:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==28:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==27:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==26:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==25:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==24:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==23:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==22:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==21:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==20:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==19:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==18:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==17:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==16:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==15:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==14:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==13:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl3,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl3,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl4,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl4,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/06.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase2_C():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    romante.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02_o.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06.png')).convert()
    backgroundg1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_g1.png')).convert()
    backgroundg2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_g1.png')).convert()
    backgroundl1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_l1.png')).convert()
    backgroundl2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_l2.png')).convert()
    backgroundt1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_t2.png')).convert()
    backgroundc1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_c1.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/lower 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp3,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==28:
                    gameDisplay.blit(backgroundc1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundc1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==27:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==26:
                    gameDisplay.blit(backgroundg2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==25:
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==24:
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==23:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==22:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:19],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[20:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==21:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==20:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==19:
                    gameDisplay.blit(backgroundt1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==18:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==17:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==16:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==15:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==14:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==13:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==12:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==11:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==5:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==1:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==28:
                    relvpointrec(-50,3,0)
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    crs()
                if trigger==27:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundc1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundc1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==26:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==25:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==24:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==23:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==22:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==21:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:19],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[20:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==20:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==19:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==18:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==17:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==16:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==15:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==14:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==13:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==11:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==10:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==4:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/03.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase2_D():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    romante.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06.png')).convert()
    backgrounda1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_a1.png')).convert()
    backgrounda2=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_a2.png')).convert()
    backgroundh1=pygame.image.load(os.path.abspath('Images/BackgroundImg/04_h1.png')).convert()
    backgroundg1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_g1.png')).convert()
    backgroundg2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_g1.png')).convert()
    backgroundl1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_l1.png')).convert()
    backgroundl2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_l2.png')).convert()
    backgroundt1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_t2.png')).convert()
    backgroundc1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_c1.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/GFImg/lower 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    gfg1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    playertext1.blit(gameDisplay,(-192,-500))
    playertext1.blit(temp3,(0,0))
    playertext1.set_alpha(196)
    playername1.blit(gameDisplay,(-200,-450))
    playername1.blit(temp4,(0,0))
    playername1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(playertext1,(192,500))
    gameDisplay.blit(playername1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==28:
                    gameDisplay.blit(backgroundc1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundc1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==27:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==26:
                    gameDisplay.blit(backgroundg2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==25:
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==24:
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==23:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==22:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:19],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[20:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==21:
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==20:
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==19:
                    gameDisplay.blit(backgroundt1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==18:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==17:
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==16:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==15:
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:21],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[22:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==14:
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==13:
                    gameDisplay.blit(backgroundh1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:28],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[29:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==12:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==11:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:20],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[21:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==7:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==5:
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    gameDisplay.blit(backgroundh1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==28:
                    relvpointrec(-30,3,0)
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    crs()
                if trigger==27:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundc1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundc1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==26:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==25:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==24:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==23:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==22:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==21:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:19],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[20:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==20:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==19:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==18:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==17:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==16:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background2,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background2,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==15:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==14:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:21],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[22:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==13:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==12:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:28],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[29:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==11:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==10:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:20],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[21:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==9:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==8:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==7:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==6:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgrounda1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:16],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[17:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==4:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundh1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundh1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgrounda2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgrounda2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    with io.open('Scripts/Phase2/04.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:24],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[25:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
    if gameExit==True:
        quitgame()
def phase2_2():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    romante.play()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("3 주 차")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/02.png')).convert()
    background2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06.png')).convert()
    backgroundg1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_g1.png')).convert()
    backgroundg2=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_g1.png')).convert()
    backgroundl1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_l2.png')).convert()
    backgroundt1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_t1.png')).convert()
    backgroundc1=pygame.image.load(os.path.abspath('Images/BackgroundImg/06_c1.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/gf 1.png')).convert_alpha()
    temp2=pygame.image.load(os.path.abspath('Images/TextScreen/gf name 2.png')).convert_alpha()
    temp3=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    temp4=pygame.image.load(os.path.abspath('Images/TextScreen/player name 1.png')).convert_alpha()
    temp5=pygame.image.load(os.path.abspath('Images/TextScreen/prof. 1.png')).convert_alpha()
    temp6=pygame.image.load(os.path.abspath('Images/TextScreen/prof. name 1.png')).convert_alpha()
    temp7=pygame.image.load(os.path.abspath('Images/GFImg/lower 1.png')).convert_alpha()
    gftext1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gfname1=pygame.Surface((temp2.get_width(),temp2.get_height())).convert()
    playertext1=pygame.Surface((temp3.get_width(),temp3.get_height())).convert()
    playername1=pygame.Surface((temp4.get_width(),temp4.get_height())).convert()
    proftext1=pygame.Surface((temp5.get_width(),temp5.get_height())).convert()
    profname1=pygame.Surface((temp6.get_width(),temp6.get_height())).convert()
    gfg1=pygame.Surface((temp7.get_width(),temp7.get_height())).convert()
    gameDisplay.blit(background1,(0,0))
    pygame.display.update()
    trigger=0
    print("Sentence "+str(trigger))
    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
        sen1=se1.readlines()[trigger]
    se1.close()
    trigger +=1
    gameDisplay.blit(background1,(0,0))
    proftext1.blit(gameDisplay,(-192,-500))
    proftext1.blit(temp5,(0,0))
    proftext1.set_alpha(196)
    profname1.blit(gameDisplay,(-200,-450))
    profname1.blit(temp6,(0,0))
    profname1.set_alpha(196)
    gameDisplay.blit(background1,(0,0))
    gameDisplay.blit(proftext1,(192,500))
    gameDisplay.blit(profname1,(200,450))
    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    gameExit=False
    while not gameExit:
        click=pygame.mouse.get_pressed()
        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    gameExit=True
            if event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE:
                pause=True
                paused("PAUSED",'Fonts/NanumGothic.ttf',120,display_width,display_height,gameDisplay)
                if trigger==11:
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==10:
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:5],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[6:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==9:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:26],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[27:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==8:
                    gameDisplay.blit(backgroundc1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundc1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:15],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[16:-1],'Fonts/NanumGothic.ttf',40,205,605,0,gameDisplay)
                if trigger==7:
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==6:
                    gameDisplay.blit(backgroundl1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:5],'Fonts/NanumGothic.ttf',40,205,545,0,gameDisplay)
                    texting(sen1[6:17],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,625,0,gameDisplay)
                if trigger==5:
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==4:
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==3:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==2:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==1:
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,0,gameDisplay)
                if trigger==0:
                    print("Sentence "+str(trigger))
                    gameDisplay.blit(background1,(0,0))
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE or click[0]==1:
                if trigger==11:
                    relvpointrec(50,3,0)
                    relvpointrec(30,3,1)
                    vn.stop()
                    romante.stop()
                    buttonsn.stop()
                    pytcls.stop()
                    crs()
                if trigger==10:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==9:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg2,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundg2,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:5],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[6:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==8:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:26],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[27:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==7:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundc1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundc1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:15],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[16:-1],'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
                if trigger==6:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundg1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundg1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==5:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundl1,(0,0))
                    gftext1.blit(gameDisplay,(-192,-500))
                    gftext1.blit(temp1,(0,0))
                    gftext1.set_alpha(196)
                    gfname1.blit(gameDisplay,(-200,-450))
                    gfname1.blit(temp2,(0,0))
                    gfname1.set_alpha(196)
                    gameDisplay.blit(backgroundl1,(0,0))
                    gameDisplay.blit(gftext1,(192,500))
                    gameDisplay.blit(gfname1,(200,450))
                    texting(sen1[:5],'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
                    texting(sen1[6:17],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                    texting(sen1[18:-1],'Fonts/NanumGothic.ttf',40,205,625,50,gameDisplay)
                if trigger==4:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(backgroundt1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(backgroundt1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==3:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    playertext1.blit(gameDisplay,(-192,-500))
                    playertext1.blit(temp3,(0,0))
                    playertext1.set_alpha(196)
                    playername1.blit(gameDisplay,(-200,-450))
                    playername1.blit(temp4,(0,0))
                    playername1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(playertext1,(192,500))
                    gameDisplay.blit(playername1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==2:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==1:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
                if trigger==0:
                    with io.open('Scripts/Phase2/07.txt','r',encoding='utf8') as se1:
                        sen1=se1.readlines()[trigger]
                    se1.close()
                    trigger +=1
                    gameDisplay.blit(background1,(0,0))
                    proftext1.blit(gameDisplay,(-192,-500))
                    proftext1.blit(temp5,(0,0))
                    proftext1.set_alpha(196)
                    profname1.blit(gameDisplay,(-200,-450))
                    profname1.blit(temp6,(0,0))
                    profname1.set_alpha(196)
                    gameDisplay.blit(background1,(0,0))
                    gameDisplay.blit(proftext1,(192,500))
                    gameDisplay.blit(profname1,(200,450))
                    texting(sen1[:-1],'Fonts/NanumGothic.ttf',40,205,585,50,gameDisplay)
    if gameExit==True:
        quitgame()
"""def reslt():
    global button01
    global quitgame
    global pause
    global loading_text
    vn.stop()
    romante.stop()
    buttonsn.stop()
    pytcls.stop()
    romante.play()
    with io.open('Data/Relation3.txt','r',encoding='utf8') as rpr1:
        rp1=rpr1.readline()[:-1]
        rp2=rpr1.readline()[:-1]
    rpr1.close()
    display_width=1280
    display_height=720
    gameDisplay=pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("")
    background1=pygame.image.load(os.path.abspath('Images/BackgroundImg/blackscreen.png')).convert()
    temp1=pygame.image.load(os.path.abspath('Images/TextScreen/player 1.png')).convert_alpha()
    text1=pygame.Surface((temp1.get_width(),temp1.get_height())).convert()
    gameExit=False
    while not gameExit:
        gameDisplay.blit(background1,(0,0))
        pygame.display.update()
        gameDisplay.blit(background1,(0,0))
        text1.blit(gameDisplay,(-192,-500))
        text1.blit(temp1,(0,0))
        text1.set_alpha(196)
        gameDisplay.blit(background1,(0,0))
        gameDisplay.blit(text1,(192,500))
        texting("여친의 호감도는 "+rp1+",",'Fonts/NanumGothic.ttf',40,205,545,50,gameDisplay)
        texting("교수님의 호감도는 "+rp2+"입니다",'Fonts/NanumGothic.ttf',40,205,605,50,gameDisplay)
        gameExit==True
    if gameExit==True:
        quitgame()"""
main()
