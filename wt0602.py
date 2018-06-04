import pygame
from pygame.locals import *
import time,random
"""
실제창에 사용되는 변수값
"""
Navy_Blue =(60,60,255)
black=(0,0,0)
white=(255,255,255)
BGColor=Navy_Blue
padWidth=1280
padHeight=600
"""
실습시뮬에 사용되는 그림 길이값
window=(400,200)
upperbar=(400,30)
exitbut=(30,30)
icon=(60,60)
chrome_on_search=(150,150)
"""
"""
실제 게임이 실행되는 공간
"""
def runGame():
    global gamepad, clock
    global bg
    global windows, icons, bars, buttons
    global chrome_on
    global menu,menu_window,menu_icons,menu_on,menu_wifi
    global kakao_logout, kakao_main, kakao_room, kakao_pro
    global none
    global chat_q1, chat_q2, chat_q3, chat_qg, chat_a1, chat_a2, chat_a3, chat_ag
    global pycharm, pycharm_but
    global pycharm_code
    """
    개발에 필요한 변수들(기본 위치,조건값)
    """
    windowmove1 = False
    windowmove2 = False
    windowmove3 = False
    windowmove4=False
    windowins1=False
    windowins2=False
    windowins3=False
    windowins4=False
    window_type1=1
    window_type2 = 2
    window_type3 = 3
    (init_x,init_y)=pygame.mouse.get_pos()

    icondraw1=False
    icondraw2 = False
    icondraw3 = False
    iconins1=False
    iconins2=False
    iconins3=False

    menudraw1=False
    menudraw2 = False
    menudraw3 = False

    draw_on=False
    draw_wifi=False
    wifi_onoff=True

    wait=2
    a=0
    b=0
    count=False

    pro=0
    chat=0

    drawpro=False
    inspro=False
    inschat=False
    drawchat=False
    insQA=False
    rand=0
    rand2=0
    changeop=False
    changean=False

    i_msg=0
    msg=0
    download=False
    bool=4

    window1_loc=[100,100]
    icon1_loc=[10,10]
    wifi_place=1140

    imp_range = []
    t=0
    min=0
    hour=0
    gamefont = pygame.font.SysFont("comicsansms", 14)
    """
    창 클래스
    """
    class window_model(object):
        def __init__(self, window, bar, buttonx, buttonm,locate,ID):
            self.window = window
            self.bar = bar
            self.buttonx = buttonx
            self.buttonm=buttonm
            self.locate = locate
            self.ID=ID

        def constr(self):
            gamepad.blit(self.window[0], self.locate)
            gamepad.blit(self.bar[0], self.locate)
            gamepad.blit(self.buttonx[0], (self.locate[0] + self.bar[1] - self.buttonx[1], self.locate[1]))
            gamepad.blit(self.buttonm[0],(self.locate[0]+self.bar[1]-self.buttonx[1]-self.buttonm[1],self.locate[1]))

        def chrome_online(self,img):
            gamepad.blit(img[0][0],(self.locate[0]+self.window[1]/2-img[0][1]/2,self.locate[1]+self.bar[2]))
            gamepad.blit(img[1][0],(self.locate[0]+self.window[1]/2-img[1][1]/2,self.locate[1]+self.bar[2]+img[0][2]))
            gamepad.blit(img[2][0],(self.locate[0]+self.window[1]/2-img[2][1]/2,self.locate[1]+self.bar[2]+img[0][2]+img[1][2]+50))

    class icon_model(object):
        def __init__(self, image, wh, locate):
            self.image = image
            self.wh = wh
            self.locate = locate

        def constr(self):
            gamepad.blit(self.image, self.locate)

    class menu_model(object):
        def __init__(self,bar,icons,wh,menu_on,menu_wifi):
            self.bar=bar
            self.menu_icons=icons
            self.wh=wh
            self.menu_on=menu_on
            self.menu_wifi=menu_wifi

        def constr(self,d1,d2,d3,hour,min):
            gamepad.blit(self.bar,(0,padHeight-self.wh[1]))
            gamepad.blit(self.menu_on[0],(0,padHeight-self.wh[1]))
            clock_text = []
            virtual_hour=5+hour
            virtual_min=min
            if virtual_min<10:
                clock_text.append("PM "+str(virtual_hour)+":"+"0"+str(virtual_min))
            else:
                clock_text.append("PM " + str(virtual_hour) + ":" + str(virtual_min))
            clock_text.append("2018-05-18")
            screen_text1 = gamefont.render(clock_text[0], True, white)
            screen_text2 = gamefont.render(clock_text[1], True, white)
            gamepad.blit(screen_text1, (1200,padHeight-self.wh[1]))
            gamepad.blit(screen_text2, (1180, padHeight - self.wh[1]/2))

    class chat_model(object):
        def __init__(self,img,len):
            self.img=img
            self.len=len


    """
    사용 함수들
    1.아이콘으로 창 실행 및 종료 버튼으로 창 닫는 함수
    2.창을 드래그로 이동시키는 함수
    3.우선도 조정 함수
    4.우선도가 자신보다 높은 함수들의 구역에서 발생한 이벤트를 무시하는 함수
    5.우선도가 자신보다 높은 객체만 리스트로 정리
    6.시간 계산
    7.메뉴 구현
    8.와이파이 구현
    """
    def icon_func(icon, Window, draw,ins, mouse_x, mouse_y):
        if icon.locate[0] <= mouse_x <= icon.locate[0] + icon.wh[0] and icon.locate[1] <= mouse_y <= icon.locate[1] + icon.wh[1] and rec_sub(Window,mouse_x,mouse_y):
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw = True
                ins=True
        if Window.locate[0] + Window.bar[1]-Window.buttonx[1]-Window.buttonm[1] <= mouse_x <= Window.locate[0] + Window.bar[1] and Window.locate[1] <= mouse_y <= Window.locate[1] + Window.buttonx[2] and rec_sub(Window,mouse_x,mouse_y) :
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                draw= False
                imp_insert(Window,'rem')

        if draw and ins:
            ins=False
            imp_insert(Window,'ins')
        if draw:
            Window.constr()
        return draw,ins

    def window_move(Window,move,ins,init_x,init_y,mouse_x,mouse_y,type):
        if ins:
            imp_insert(Window, 'ins')
            ins = False

        if move==True:
            (final_x,final_y)=pygame.mouse.get_pos()
            Window.locate = (Window.locate[0]+final_x-init_x, Window.locate[1]+final_y-init_y)
            (init_x,init_y)=pygame.mouse.get_pos()

        if Window.locate[0]<=mouse_x<=Window.locate[0]+Window.bar[1]-Window.buttonx[1]-Window.buttonm[1] and Window.locate[1] <= mouse_y<=Window.locate[1]+Window.buttonx[2]:
            if Window.ID==1:
                if not(Window.locate[0]<=mouse_x<=Window.locate[0]+106+106+106 and Window.locate[1]+8<=mouse_y<=Window.locate[1]+8+28):
                    if event.type == MOUSEBUTTONDOWN and event.button == 1:
                        move = True
                        ins = True
                        (init_x, init_y) = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    move = False
            else:
                if event.type==MOUSEBUTTONDOWN and event.button==1:
                    move=True
                    ins=True
                    (init_x, init_y) = pygame.mouse.get_pos()
                if event.type==MOUSEBUTTONUP and event.button==1:
                    move=False
        if Window.ID==1:
            if Window.locate[0]<=mouse_x<=Window.locate[0]+106 and Window.locate[1]+8<=mouse_y<=Window.locate[1]+8+28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Window.bar[0]=bars[0]
                    ins=True
                    type=1
            if Window.locate[0]+106<=mouse_x<=Window.locate[0]+106+106 and Window.locate[1]+8<=mouse_y<=Window.locate[1]+8+28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Window.bar[0]=bars[1]
                    ins = True
                    type = 2
            if Window.locate[0]+106+106<=mouse_x<=Window.locate[0]+106+106+106 and Window.locate[1]+8<=mouse_y<=Window.locate[1]+8+28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    Window.bar[0]=bars[2]
                    ins = True
                    type = 3

        return init_x,init_y,move,ins,type

    def imp_insert(obj,mode):
        count = 0
        key=False
        """
        원소 찾기
        """
        while count<len(imp_range):
            if imp_range[count].ID == obj.ID:
                key=True
                p=imp_range[count]
                break
            count = count + 1

        if mode=='ins':
            if not key:
                imp_range.append(obj)
            else:
                imp_range.remove(p)
                imp_range.append(obj)
        elif mode=='rem':
            if key:
                imp_range.remove(p)

    def rec_sub(obj, mouse_x, mouse_y):
        i = 0
        s = list_cut(obj)
        for x in s:
            if x.locate[0] <= mouse_x <= x.locate[0] + x.window[1] and x.locate[1] <= mouse_y <= x.locate[1] + x.window[2]:
                if i==1:
                    continue
                i = 1
        if i == 0:
            return True
        else:
            return False

    def list_cut(obj):
        count = 0
        for i in range(len(imp_range)):
            if imp_range[i] == obj:
                return imp_range[(count + 1):]
            count = count + 1
        return imp_range

    def time_cal(time):
        hour=int(time//60)
        minute=int(time%60)
        return hour,minute

    def menu_func(draw, mouse_x, mouse_y):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if 0 <= mouse_x <= 40 and padHeight-40 <= mouse_y <= padHeight:
                draw = True
            elif not (0<= mouse_x<=246 and padHeight-40-162 <= mouse_y <= padHeight-40) :
                draw= False
        if draw:
            gamepad.blit(menu_window,(0,padHeight-40-162))
            if draw and 0<=mouse_x<=246 and padHeight-40-54<=mouse_y<=padHeight-40:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("give up")
            if draw and 0<=mouse_x<=246 and padHeight-40-54-54<=mouse_y<=padHeight-40-54:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("close")
            if draw and 0<=mouse_x<=246 and padHeight-40-54-54-54<=mouse_y<=padHeight-40-54-54:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("exit")
        return draw

    def wifi_func(draw, on_off,mouse_x, mouse_y,wait):
        if on_off and not (wait==1 or wait==3):
            gamepad.blit(menu_wifi[0], (wifi_place, padHeight - 40))
        else:
            gamepad.blit(menu_wifi[1], (wifi_place, padHeight - 40))
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if wifi_place <= mouse_x <= wifi_place+40 and padHeight-40 <= mouse_y <= padHeight:
                draw = True
            elif not (wifi_place+40-256<= mouse_x<=wifi_place+40 and padHeight-40-284 <= mouse_y <= padHeight-40) :
                draw= False
        if draw:
            if wait==1 or wait==3:
                gamepad.blit(menu_wifi[6],(wifi_place+40-256,padHeight-40-284))
            elif on_off:
                gamepad.blit(menu_wifi[2],(wifi_place+40-256,padHeight-40-284))
                gamepad.blit(menu_wifi[4], (wifi_place + 40 - 256/2-65, padHeight - 40-60))
                if wait==2:
                    if wifi_place+40-256/2-25<=mouse_x<=wifi_place+40-256/2+25 and padHeight-40-60<=mouse_y<=padHeight-40-60+34:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            on_off= not on_off
                            wait=3
            else:
                gamepad.blit(menu_wifi[3],(wifi_place+40-256,padHeight-40-284))
                gamepad.blit(menu_wifi[5],(wifi_place + 40 - 256/2-65, padHeight - 40 -60))
                if wait==0:
                    if wifi_place+40-256/2-25<=mouse_x<=wifi_place+40-256/2+25 and padHeight-40-60<=mouse_y<=padHeight-40-60+34:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            on_off= not on_off
                            wait=1
        return draw,on_off,wait

    def kakaomain(Window,mouse_x,mouse_y,draw,ins,list):
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+92<=mouse_y<=Window.locate[1]+92+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=list[0]
                ins=True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+161<=mouse_y<=Window.locate[1]+161+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=list[1]
                ins = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+226<=mouse_y<=Window.locate[1]+226+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=list[2]
                ins = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+291<=mouse_y<=Window.locate[1]+291+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=list[3]
                ins = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+358<=mouse_y<=Window.locate[1]+358+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=list[4]
                ins = True

        if draw!=False :
            if Window.locate[0]-draw.buttonx[1] <= mouse_x <= Window.locate[0] and Window.locate[1] <= mouse_y <= Window.locate[1] + draw.buttonx[2] :
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    #imp_insert(draw,'rem')
                    draw = False

        if (draw != False) and ins:
            imp_insert(Window, 'ins')
            ins=False
        if draw != False:
            gamepad.blit(draw.window[0],(Window.locate[0]-draw.window[1]-2,Window.locate[1]))

        return draw,ins

    def kakaochat(Window,mouse_x,mouse_y,draw,drawed,drawob,ins,list):

        #버튼 부분 전부 rec_sub(Window,mouse_x,mouse_y) 처리

        if drawed!=False:
            if draw:
                draw=False
            numb=drawed.ID
            if numb==11:
                drawob=list[0]
            elif numb==12:
                drawob=list[1]
            elif numb==13:
                drawob=list[2]
            elif numb==14:
                drawob=list[3]
            elif numb==15:
                drawob=list[4]
            if Window.locate[0]-228+94<=mouse_x<=Window.locate[0]-228+94+40 and Window.locate[1]+272<=mouse_y<=Window.locate[1]+272+40:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    draw=True
                    ins=True

        if Window.locate[0]+70<=mouse_x<=Window.locate[0]+70+210 and Window.locate[1]+90<=mouse_y<=Window.locate[1]+90+64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=True
                ins = True
                drawob = list[0]
        if Window.locate[0]+70<=mouse_x<=Window.locate[0]+70+210 and Window.locate[1]+155<=mouse_y<=Window.locate[1]+155+64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=True
                ins = True
                drawob = list[1]
        if Window.locate[0]+70<=mouse_x<=Window.locate[0]+70+210 and Window.locate[1]+225<=mouse_y<=Window.locate[1]+225+64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=True
                ins = True
                drawob = list[2]
        if Window.locate[0]+70<=mouse_x<=Window.locate[0]+70+210 and Window.locate[1]+290<=mouse_y<=Window.locate[1]+290+64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=True
                ins = True
                drawob = list[3]
        if Window.locate[0]+70<=mouse_x<=Window.locate[0]+70+210 and Window.locate[1]+355<=mouse_y<=Window.locate[1]+355+64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=True
                ins = True
                drawob = list[4]

        if Window.locate[0]-drawob.buttonm[1]-2<=mouse_x<=Window.locate[0]-2 and Window.locate[1]+4<=mouse_y<=Window.locate[1]+4+20 and rec_sub(Window,mouse_x,mouse_y):
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw=False

        if draw and ins:
            drawed=False
            ins=False
            imp_insert(Window, 'ins')
        if draw:
            gamepad.blit(drawob.window[0],(Window.locate[0]-drawob.bar[1]-2,Window.locate[1]))

        return draw,drawed,drawob,ins

    def chatclick(Window,drawob,mouse_x,mouse_y,msg,ins):
        #메세지 종류 결정
        if drawob.ID==25:
            return msg,ins
        if drawob.ID==22 or drawob.ID==23 or drawob.ID==24:
            if Window.locate[0]-drawob.bar[1]+18<=Window.locate[0]-drawob.bar[1]+18+240 and Window.locate[1]+388<=mouse_y<=Window.locate[1]+388+28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    msg=1
                    ins=True
            if Window.locate[0]-drawob.bar[1]+18<=Window.locate[0]-drawob.bar[1]+18+240 and Window.locate[1]+424<=mouse_y<=Window.locate[1]+424+28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    msg=2
                    ins=True
            if Window.locate[0]-drawob.bar[1]+18<=Window.locate[0]-drawob.bar[1]+18+240 and Window.locate[1]+460<=mouse_y<=Window.locate[1]+460+28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    msg=3
                    ins=True
        if drawob.ID==21:
            if Window.locate[0]-drawob.bar[1]+95<=mouse_x<= Window.locate[0]-drawob.bar[1]+95+88 and Window.locate[1]+388<=mouse_y<=Window.locate[1]+388+88:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    msg=4
                    ins=True
        if msg!=0 and ins:
            imp_insert(Window,"ins")
        return msg,ins

    def question(Window,msg,messages,chatdraw,ins,p,change):
        if msg==1 and chatdraw and ins:
            p=random.randint(0,2)

        if msg==2 and chatdraw and ins:
            p=random.randint(0,2)

        if msg==3 and chatdraw and ins:
            p=random.randint(0,1)

        if msg==4 and chatdraw and ins:
            p=0

        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 90 <= mouse_y <= \
                Window.locate[1] + 90 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change=True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 155 <= mouse_y <= \
                Window.locate[1] + 155 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 225 <= mouse_y <= \
                Window.locate[1] + 225 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 290 <= mouse_y <= \
                Window.locate[1] + 290 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 355 <= mouse_y <= \
                Window.locate[1] + 355 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+92<=mouse_y<=Window.locate[1]+92+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+161<=mouse_y<=Window.locate[1]+161+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+226<=mouse_y<=Window.locate[1]+226+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+291<=mouse_y<=Window.locate[1]+291+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+358<=mouse_y<=Window.locate[1]+358+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True

        if drawob.ID == 22 or drawob.ID == 23 or drawob.ID == 24:
            if Window.locate[0] - drawob.bar[1] + 18 <= Window.locate[0] - drawob.bar[1] + 18 + 240 and Window.locate[
                1] + 388 <= mouse_y <= Window.locate[1] + 388 + 28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
            if Window.locate[0] - drawob.bar[1] + 18 <= Window.locate[0] - drawob.bar[1] + 18 + 240 and Window.locate[
                1] + 424 <= mouse_y <= Window.locate[1] + 424 + 28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
            if Window.locate[0] - drawob.bar[1] + 18 <= Window.locate[0] - drawob.bar[1] + 18 + 240 and Window.locate[
                1] + 460 <= mouse_y <= Window.locate[1] + 460 + 28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
        if drawob.ID == 21:
            if Window.locate[0] - drawob.bar[1] + 95 <= mouse_x <= Window.locate[0] - drawob.bar[1] + 95 + 88 and \
                    Window.locate[1] + 388 <= mouse_y <= Window.locate[1] + 388 + 88:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
        if msg>0 and not change:
            gamepad.blit(messages[msg-1][p].img, (Window.locate[0] - messages[msg-1][p].len - 3, Window.locate[1] + 64))

        if not chatdraw:
            msg=0

        return msg,p,ins,change

    def answer(Window,msg,chatdraw,bool,ins,download,change,p):
        if msg==1 and chatdraw and ins:
            if bool==0:
                p=random.randint(0,2)
                ins=False
            elif bool==4:
                p = random.randint(0, 2)
                ins = False
        if msg==2 and chatdraw and ins:
            if bool:
                p=0
                ins = False
            else:
                p=0
                ins = False
        if msg==3 and chatdraw and ins:
            p=random.randint(0,6)
            ins = False
            bool=0
        if msg==4 and chatdraw and ins:
            p=random.randint(0,1)
            ins = False
            bool=0

        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 90 <= mouse_y <= \
                Window.locate[1] + 90 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change=True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 155 <= mouse_y <= \
                Window.locate[1] + 155 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 225 <= mouse_y <= \
                Window.locate[1] + 225 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 290 <= mouse_y <= \
                Window.locate[1] + 290 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0] + 70 <= mouse_x <= Window.locate[0] + 70 + 210 and Window.locate[1] + 355 <= mouse_y <= \
                Window.locate[1] + 355 + 64:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+92<=mouse_y<=Window.locate[1]+92+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+161<=mouse_y<=Window.locate[1]+161+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+226<=mouse_y<=Window.locate[1]+226+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+291<=mouse_y<=Window.locate[1]+291+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True
        if Window.locate[0]+19<=mouse_x<=Window.locate[0]+19+50 and Window.locate[1]+358<=mouse_y<=Window.locate[1]+358+50:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                change = True

        if drawob.ID == 22 or drawob.ID == 23 or drawob.ID == 24:
            if Window.locate[0] - drawob.bar[1] + 18 <= Window.locate[0] - drawob.bar[1] + 18 + 240 and Window.locate[
                1] + 388 <= mouse_y <= Window.locate[1] + 388 + 28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
            if Window.locate[0] - drawob.bar[1] + 18 <= Window.locate[0] - drawob.bar[1] + 18 + 240 and Window.locate[
                1] + 424 <= mouse_y <= Window.locate[1] + 424 + 28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
            if Window.locate[0] - drawob.bar[1] + 18 <= Window.locate[0] - drawob.bar[1] + 18 + 240 and Window.locate[
                1] + 460 <= mouse_y <= Window.locate[1] + 460 + 28:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
        if drawob.ID == 21:
            if Window.locate[0] - drawob.bar[1] + 95 <= mouse_x <= Window.locate[0] - drawob.bar[1] + 95 + 88 and \
                    Window.locate[1] + 388 <= mouse_y <= Window.locate[1] + 388 + 88:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    change = False
        if msg>0 and (bool==0 or bool==4) and not change:
            if 3+msg+bool>9:
                bool=0
            gamepad.blit(messages[3+msg+bool][p].img, (Window.locate[0] - 280 - 3, Window.locate[1] + 100))

        if not chatdraw:
            msg=0

        return bool,msg,p,ins,change



    """
    객체 생성
    """
    window1 = window_model([windows[0], 838, 480], [bars[0], 838, 38], [buttons[0], 38, 38],[buttons[1],38,38], window1_loc,1)
    window2 = window_model([pycharm, 886, 484], [none, 886, 38], [none, 16, 16],[none,16,16],[window1_loc[0] + 50, window1_loc[1] + 50],2)
    window3 = window_model([kakao_main, 280, 496], [none, 280, 28], [none, 20, 20],[none,20,20],[window1_loc[0] + 600, window1_loc[1]],3)
    kakao_pro1=window_model([kakao_pro[0],228,340],[none, 228, 24], [none, 20, 20],[none,20,20],[window1_loc[0] + 200-230, window1_loc[1]],11)
    kakao_pro2 = window_model([kakao_pro[1], 228, 340], [none, 228, 24], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 12)
    kakao_pro3 = window_model([kakao_pro[2], 228, 340], [none, 228, 24], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 13)
    kakao_pro4 = window_model([kakao_pro[3], 228, 340], [none, 228, 24], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 14)
    kakao_pro5 = window_model([kakao_pro[4], 228, 340], [none, 228, 24], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 15)
    kakao_chat1=window_model([kakao_room[0],280,500],[none, 280, 28], [none, 20, 20],[none,20,20],[window1_loc[0] + 200-230, window1_loc[1]],21)
    kakao_chat2 = window_model([kakao_room[1], 280, 500], [none, 280, 28], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 22)
    kakao_chat3 = window_model([kakao_room[2], 280, 500], [none, 280, 28], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 23)
    kakao_chat4 = window_model([kakao_room[3], 280, 500], [none, 280, 28], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 24)
    kakao_chat5 = window_model([kakao_room[4], 280, 500], [none, 280, 28], [none, 20, 20], [none, 20, 20],[window1_loc[0] + 200 - 230, window1_loc[1]], 25)
    none1=window_model([none,10,10],[none,10,10],[none,10,10],[none,10,10],[0,0],0)
    list=[kakao_pro1,kakao_pro2,kakao_pro3,kakao_pro4,kakao_pro5]
    list2=[kakao_chat1,kakao_chat2,kakao_chat3,kakao_chat4,kakao_chat5]
    icon1 = icon_model(icons[0], (60, 60), icon1_loc)
    icon2 = icon_model(icons[1], (60, 60), [icon1_loc[0], icon1_loc[1] + 90])
    icon3 = icon_model(icons[2], (60, 60), [icon1_loc[0], icon1_loc[1] + 180])

    menu=menu_model(menu,menu_icons,(40,40),[menu_on[0],0,padHeight-40],[menu_wifi[0],1080,padHeight-40])

    q1_1=chat_model(chat_q1[0],176)
    q1_2 = chat_model(chat_q1[1],226)
    q1_3 = chat_model(chat_q1[2], 120)
    q1=[q1_1,q1_2,q1_3]
    q2_1 = chat_model(chat_q2[0],220 )
    q2_2 = chat_model(chat_q2[1],81 )
    q2_3 = chat_model(chat_q2[2],184 )
    q2=[q2_1,q2_2,q2_3]
    q3_1 = chat_model(chat_q3[0],63 )
    q3_2 = chat_model(chat_q3[1],62 )
    q3=[q3_1,q3_2]
    q_g=[chat_model(chat_qg[0],96)]

    a1_y1=chat_model(chat_a1[0],136)
    a1_y2 = chat_model(chat_a1[1], 123)
    a1_y3 = chat_model(chat_a1[2], 120)
    a1_y=[a1_y1,a1_y2,a1_y3]
    a1_n1 = chat_model(chat_a1[3], 185)
    a1_n2 = chat_model(chat_a1[4], 61)
    a1_n3 = chat_model(chat_a1[5], 81)
    a1_n = [a1_n1, a1_n2, a1_n3]
    a2_y=[chat_model(chat_a2[0],180)]
    a2_n =[ chat_model(chat_a2[1], 60)]
    a3_1=chat_model(chat_a3[0],92)
    a3_2 = chat_model(chat_a3[1], 106)
    a3_3 = chat_model(chat_a3[2], 60)
    a3_4 = chat_model(chat_a3[3], 59)
    a3_5 = chat_model(chat_a3[4], 42)
    a3_6 = chat_model(chat_a3[5], 96)
    a3_7 = chat_model(chat_a3[6], 35)
    a3=[a3_1,a3_2,a3_3,a3_4,a3_5,a3_6,a3_7]
    a_g1=chat_model(chat_ag[0],75)
    a_g2 = chat_model(chat_ag[1], 43)
    ag=[a_g1,a_g2]
    messages=(q1,q2,q3,q_g,a1_y,a2_y,a3,ag,a1_n,a2_n)

    chrome = []
    chrome.append((chrome_on[1], 838, 176))
    chrome.append((chrome_on[0], 138, 138))
    chrome.append((chrome_on[2], 364, 54))

    drawob = none1
    """
    교수님 등장시간
    """
    test_time=random.randrange(6,11)
    f_time = random.randrange(61, 121)
    s_time = random.randrange(121, 181)
    t_time = random.randrange(181, 241)
    wifi_time=random.randrange(91,211)
    test_wifi_time=random.randrange(6,11)

    """
    과제 진행도
    """
    percent=0

    """
    반복문
    """
    ts_now_i = time.time()
    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                gamepad.fill(BGColor)
                crashed=True
            if hour>=3:
                gamepad.fill(BGColor)
                print("Time Over!")
                crashed = True
        gamepad.blit(bg, (0, 0))
        (mouse_x, mouse_y) = pygame.mouse.get_pos()
        ts_now_f = time.time()
        if ts_now_f - ts_now_i>=0.5:
            t=t+0.25
            ts_now_i=ts_now_f
        (hour,min)=time_cal(t)

        """
        아이콘으로 창을 열고 종료버튼으로 창 닫는 함수
        """
        icon1.constr()
        icon2.constr()
        icon3.constr()
        (icondraw1,iconins1)=icon_func(icon1,window1,icondraw1,iconins1,mouse_x,mouse_y)
        (icondraw2,iconins2) = icon_func(icon2, window2, icondraw2,iconins2, mouse_x, mouse_y)
        (icondraw3,iconins3) = icon_func(icon3, window3, icondraw3,iconins3, mouse_x, mouse_y)
        """
        바를 클릭한 상태에서 창을 움직이는 함수
        """
        if icondraw1 and rec_sub(window1,mouse_x, mouse_y):
            (init_x,init_y,windowmove1,windowins1,window_type1)=window_move(window1,windowmove1,windowins1,init_x,init_y,mouse_x,mouse_y,window_type1)
        if icondraw2 and rec_sub(window2, mouse_x, mouse_y):
            (init_x, init_y, windowmove2,windowins2,window_type2) = window_move(window2, windowmove2,windowins2, init_x, init_y, mouse_x, mouse_y,window_type2)
        if icondraw3 and rec_sub(window3, mouse_x, mouse_y):
            (init_x, init_y, windowmove3,windowins3,window_type3) = window_move(window3, windowmove3,windowins3, init_x, init_y, mouse_x, mouse_y,window_type3)

        """
        우선도에 따라 이미지 삽입
        """
        for x in imp_range:
            if x.ID==4:
                continue
            x.constr()
            if x.ID==1 and window_type1==1:
                x.chrome_online(chrome)
            if x.ID==2 :
                pygame.draw.rect(gamepad,(0,125,60),(x.locate[0]+180,x.locate[1]+46,63,int(270*percent/100)))
                if percent>=100:
                    pygame.draw.rect(gamepad, (0, 225, 0),(x.locate[0] + 180, x.locate[1] + 46, 63, int(270 * percent / 100)))
                How_many=gamefont.render((str(percent)+'%'),True,black)
                gamepad.blit(How_many,(x.locate[0]+180+20,x.locate[1]+46+130))
                if 10<=percent<20:
                    gamepad.blit(pycharm_code[0],(x.locate[0]+180+64,x.locate[1]+46))
                elif 20<=percent<30:
                    gamepad.blit(pycharm_code[1],(x.locate[0]+180+64,x.locate[1]+46))
                elif 30<=percent<40:
                    gamepad.blit(pycharm_code[2],(x.locate[0]+180+64,x.locate[1]+46))
                elif 40<=percent<50:
                    gamepad.blit(pycharm_code[3],(x.locate[0]+180+64,x.locate[1]+46))
                elif 50<=percent<60:
                    gamepad.blit(pycharm_code[4],(x.locate[0]+180+64,x.locate[1]+46))
                if 60<=percent<70:
                    gamepad.blit(pycharm_code[5],(x.locate[0]+180+64,x.locate[1]+46))
                elif 70<=percent<80:
                    gamepad.blit(pycharm_code[6],(x.locate[0]+180+64,x.locate[1]+46))
                elif 80<=percent<90:
                    gamepad.blit(pycharm_code[7],(x.locate[0]+180+64,x.locate[1]+46))
                elif 90<=percent<100:
                    gamepad.blit(pycharm_code[8],(x.locate[0]+180+64,x.locate[1]+46))
                elif 100<=percent:
                    gamepad.blit(pycharm_code[9],(x.locate[0]+180+64,x.locate[1]+46))
                    if x.locate[0] + 793 <= mouse_x <= x.locate[0] + 886 and x.locate[1]+337<=mouse_y<=x.locate[1]+484:
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
                            print("submitted")
                            crashed=True

            if x.ID==3 :
                if test_time-10<=t<=test_time:
                    bool=0
                else:
                    bool=4
                (drawpro, inspro) = kakaomain(window3, mouse_x, mouse_y, drawpro, inspro, list)
                (drawchat,drawpro,drawob,inschat)=kakaochat(window3,mouse_x,mouse_y,drawchat,drawpro,drawob,inschat,list2)
                (msg,insQA)=chatclick(window3,drawob,mouse_x,mouse_y,msg,insQA)
                (msg,rand,insQA,changeop)=question(window3,msg,messages,drawchat,insQA,rand,changeop)

                (bool,msg,rand2,insQA,changean)=answer(window3,msg,drawchat,bool,insQA,download,changean,rand2)
        """
        진행도
        """

        if imp_range!=[] and percent<100:
            if imp_range[-1].ID==1 and window_type1==1:
                if not count:
                    b = t
                    count = True
                if t-b>0.5:
                    count=False
                    percent+=1
            elif imp_range[-1].ID==2 and percent<100:
                if not count:
                    b = t
                    count = True
                if t-b>1:
                    count=False
                    percent+=1
        if percent<100:
            window2.window[0]=pycharm_but
        else:
            window2.window[0] = pycharm
        """
        메뉴 이미지 삽입
        """
        menu.constr(menudraw1,menudraw2,menudraw3,hour,min)
        """
        메뉴 전원
        """
        draw_on=menu_func(draw_on,mouse_x,mouse_y)
        """
        메뉴 와이파이
        """
        (draw_wifi,wifi_onoff,wait)=wifi_func(draw_wifi,wifi_onoff,mouse_x,mouse_y,wait)
        if wait==3: #클릭 후 텀을 둬서 반복적으로 클릭되지 못하게 조정
            if not count:
                a=t
                count=True
            if t-a>=1:
                wait=0
                a=0
                count=False
        if wait==1:
            if not count:
                a=t
                count=True
            if t-a>=1:
                wait=2
                a=0
                count=False

        """
        교수님이 올 시간
        """
        if t == test_time or t == f_time or t == s_time or t == t_time:
            if icondraw1 or icondraw2 or icondraw3:
                print("you are F!")
        if t==wifi_time or t==test_wifi_time:
            wifi_onoff=False
            wait=0

        """
        변화 반복
        """
        pygame.display.flip()   #변화를 계속해서 갱신한다. 사진을 이어붙여 영화를 만드는 것과 동일.
        clock.tick(30)#프레임 설정
    pygame.quit()
"""
런게임 함수에 필요한 모든 요소를 제공, 런게임 함수 실행
"""
def initGame():
    global gamepad, clock
    global bg
    global windows, icons, bars, buttons
    global chrome_on
    global menu,menu_window,menu_icons,menu_on,menu_wifi
    global kakao_logout,kakao_main,kakao_room,kakao_pro
    global none
    global chat_q1,chat_q2,chat_q3,chat_qg,chat_a1,chat_a2,chat_a3,chat_ag
    global pycharm,pycharm_but
    global pycharm_code
    """
    게임판 준비 및 프레임 설정
    """
    pygame.init() #파이겜 모듈을 전부 넣어줌
    gamepad=pygame.display.set_mode((padWidth,padHeight)) #게임판 크기 설정. 모드 안에 튜플로 넣어야 함
    pygame.display.set_caption('두근두근 실습실')#제목 설정
    clock=pygame.time.Clock()#초당 프레임 설정. 30 또는 60

    bg=pygame.image.load("image/bg.png")
    """
    창 구현에 필요한 요소
    """
    windows=[]
    for i in range(3):
        windows.append(pygame.image.load("image/window_model.png"))
    icons=[]
    icons.append(pygame.image.load("image/icon_chrome.png"))
    icons.append(pygame.image.load("image/icon_idle.png"))
    icons.append(pygame.image.load("image/icon_kakao.png"))
    buttons = []
    buttons.append(pygame.image.load("image/exitbut.png"))
    buttons.append(pygame.image.load("image/minus.png"))
    bars = []
    bars.append(pygame.image.load("image/upperbar_search.png"))
    bars.append(pygame.image.load("image/upperbar_sit.png"))
    bars.append(pygame.image.load("image/upperbar_work.png"))

    """
    메뉴
    """
    menu=pygame.image.load("image/menu_bar.png")
    menu_window = pygame.image.load("image/menu_on.png")

    menu_icons=[]
    menu_icons.append(pygame.image.load("image/menu_chrome.png"))
    menu_icons.append(pygame.image.load("image/menu_idle.png"))
    menu_icons.append(pygame.image.load("image/menu_kakao.png"))

    menu_on=[]
    menu_on.append(pygame.image.load("image/menu_on_icon2.png"))

    menu_wifi=[]
    menu_wifi.append(pygame.image.load("image/menu_wifi_on.png"))
    menu_wifi.append(pygame.image.load("image/menu_wifi_off.png"))
    menu_wifi.append(pygame.image.load("image/wifi_on.png"))
    menu_wifi.append(pygame.image.load("image/wifi_off.png"))
    menu_wifi.append(pygame.image.load("image/wifi_switch_on.png"))
    menu_wifi.append(pygame.image.load("image/wifi_switch_off.png"))
    menu_wifi.append(pygame.image.load("image/wifi_change.png"))
    """
    크롬
    """
    chrome_on=[]
    chrome_on.append(pygame.image.load("image/chrome_on_search.png"))
    chrome_on.append(pygame.image.load("image/chrome_on_google.png"))
    chrome_on.append(pygame.image.load("image/chrome_on_doing.png"))
    """
    카카오톡
    """
    kakao_main=pygame.image.load("image/kakao_main.png")
    kakao_logout=pygame.image.load("image/kakao_logout.png")
    kakao_room=[]
    kakao_room.append(pygame.image.load("image/gf_chat.png"))
    kakao_room.append(pygame.image.load("image/f1_chat.png"))
    kakao_room.append(pygame.image.load("image/f2_chat.png"))
    kakao_room.append(pygame.image.load("image/f3_chat.png"))
    kakao_room.append(pygame.image.load("image/pf_chat.png"))
    kakao_pro=[]
    kakao_pro.append(pygame.image.load("image/gf_prof.png"))
    kakao_pro.append(pygame.image.load("image/f1_prof.png"))
    kakao_pro.append(pygame.image.load("image/f2_prof.png"))
    kakao_pro.append(pygame.image.load("image/f3_prof.png"))
    kakao_pro.append(pygame.image.load("image/pf_prof.png"))
    """
    카톡바
    """
    none=pygame.image.load("image/none.png")

    """
    카톡챗
    """
    chat_q1=[]
    chat_q1.append(pygame.image.load("image/q2_1.png"))
    chat_q1.append(pygame.image.load("image/q2_2.png"))
    chat_q1.append(pygame.image.load("image/q2_3.png"))

    chat_q2=[]
    chat_q2.append(pygame.image.load("image/q3_1.png"))
    chat_q2.append(pygame.image.load("image/q3_2.png"))
    chat_q2.append(pygame.image.load("image/q3_3.png"))

    chat_q3=[]
    chat_q3.append(pygame.image.load("image/q1_1.png"))
    chat_q3.append(pygame.image.load("image/q1_2.png"))

    chat_qg=[]
    chat_qg.append(pygame.image.load("image/q_g.png"))

    chat_ag=[]
    chat_ag.append(pygame.image.load("image/a_g1.png"))
    chat_ag.append(pygame.image.load("image/a_g2.png"))

    chat_a1=[]
    chat_a1.append(pygame.image.load("image/a2_y1.png"))
    chat_a1.append(pygame.image.load("image/a2_y2.png"))
    chat_a1.append(pygame.image.load("image/a2_y3.png"))
    chat_a1.append(pygame.image.load("image/a2_n1.png"))
    chat_a1.append(pygame.image.load("image/a2_n2.png"))
    chat_a1.append(pygame.image.load("image/a2_n3.png"))

    chat_a2=[]
    chat_a2.append(pygame.image.load("image/a3_y.png"))
    chat_a2.append(pygame.image.load("image/a3_n.png"))

    chat_a3=[]
    chat_a3.append(pygame.image.load("image/a1_1.png"))
    chat_a3.append(pygame.image.load("image/a1_2.png"))
    chat_a3.append(pygame.image.load("image/a1_3.png"))
    chat_a3.append(pygame.image.load("image/a1_4.png"))
    chat_a3.append(pygame.image.load("image/a1_5.png"))
    chat_a3.append(pygame.image.load("image/a1_6.png"))
    chat_a3.append(pygame.image.load("image/a1_7.png"))

    """
    파이참
    """
    pycharm=pygame.image.load("image/pycharm.png")
    pycharm_but=pygame.image.load("image/pycharm2.png")

    pycharm_code=[]
    pycharm_code.append(pygame.image.load("image/day2_1.png"))
    pycharm_code.append(pygame.image.load("image/day2_2.png"))
    pycharm_code.append(pygame.image.load("image/day2_3.png"))
    pycharm_code.append(pygame.image.load("image/day2_4.png"))
    pycharm_code.append(pygame.image.load("image/day2_5.png"))
    pycharm_code.append(pygame.image.load("image/day2_6.png"))
    pycharm_code.append(pygame.image.load("image/day2_7.png"))
    pycharm_code.append(pygame.image.load("image/day2_8.png"))
    pycharm_code.append(pygame.image.load("image/day2_9.png"))
    pycharm_code.append(pygame.image.load("image/day2_10.png"))
    """
    런게임 실행
    """
    runGame()
"""
인잇게임을 실행
"""
if __name__=='__main__':
    initGame()