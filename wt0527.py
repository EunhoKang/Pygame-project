import pygame
from pygame.locals import *
import time
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
    """
    개발에 필요한 변수들(기본 위치,조건값)
    """
    windowmove1 = False
    windowmove2 = False
    windowmove3 = False
    windowins1=False
    windowins2=False
    windowins3=False
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
    count=False

    window1_loc=(100,100)
    icon1_loc=(10,10)
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
            virtual_hour=1+hour
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
    """
    사용 함수들
    1.아이콘으로 창 실행 및 종료 버튼으로 창 닫는 함수
    2.창을 드래그로 이동시키는 함수
    3.우선도 조정 함수
    4.우선도가 자신보다 높은 함수들의 구역에서 발생한 이벤트를 무시하는 함수
    5.우선도가 자신보다 높은 객체만 리스트로 정리
    6.시간 계산
    """
    def icon_func(icon, window, draw,ins, mouse_x, mouse_y):
        if icon.locate[0] <= mouse_x <= icon.locate[0] + icon.wh[0] and icon.locate[1] <= mouse_y <= icon.locate[1] + icon.wh[1]:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                draw = True
                ins=True
        if window.locate[0] + window.bar[1]-window.buttonx[1] <= mouse_x <= window.locate[0] + window.bar[1] and window.locate[1] <= mouse_y <= window.locate[1] + window.buttonx[2] :
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                draw= False
                imp_insert(window,'rem')
        if window.locate[0] + window.bar[1]-window.buttonx[1]-window.buttonm[1] <= mouse_x <= window.locate[0] + window.bar[1]-window.buttonx[1] and window.locate[1] <= mouse_y <= window.locate[1] + window.buttonx[2] :
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                draw= False
                imp_insert(window,'rem')
        if draw and ins:
            ins=False
            imp_insert(window,'ins')
        if draw:
            window.constr()
        return draw,ins

    def window_move(window,move,ins,init_x,init_y,mouse_x,mouse_y):
        if move==True:
            if ins:
                imp_insert(window, 'ins')
                ins = False
            (final_x,final_y)=pygame.mouse.get_pos()
            window.locate = (window.locate[0]+final_x-init_x, window.locate[1]+final_y-init_y)
            (init_x,init_y)=pygame.mouse.get_pos()

        if window.locate[0]<=mouse_x<=window.locate[0]+window.bar[1]-window.buttonx[1]-window.buttonm[1] and window.locate[1] <= mouse_y<=window.locate[1]+window.buttonx[2]:
            if event.type==MOUSEBUTTONDOWN and event.button==1:
                move=True
                ins=True
                (init_x, init_y) = pygame.mouse.get_pos()
            if event.type==MOUSEBUTTONUP and event.button==1:
                move=False
        return init_x,init_y,move,ins

    def imp_insert(obj,mode):
        count = 0
        key=False
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
                    print("exit")
            if draw and 0<=mouse_x<=246 and padHeight-40-54-54<=mouse_y<=padHeight-40-54:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("close")
            if draw and 0<=mouse_x<=246 and padHeight-40-54-54-54<=mouse_y<=padHeight-40-54-54:
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    print("give up")
        return draw

    def wifi_func(draw, on_off,mouse_x, mouse_y,wait):
        if on_off:
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

    """
    객체 생성
    """
    window1 = window_model((windows[0], 838, 480), (bars[0], 838, 38), (buttons[0], 38, 38),(buttons[1],38,38), window1_loc,1)
    window2 = window_model((windows[1], 838, 480), (bars[1], 838, 38), (buttons[0], 38, 38),(buttons[1],38,38),
                           (window1_loc[0] + 50, window1_loc[1] + 50),2)
    window3 = window_model((windows[2], 838, 480), (bars[2], 838, 38), (buttons[0], 38, 38),(buttons[1],38,38),
                           (window1_loc[0] + 100, window1_loc[1] + 100),3)
    icon1 = icon_model(icons[0], (60, 60), icon1_loc)
    icon2 = icon_model(icons[1], (60, 60), (icon1_loc[0], icon1_loc[1] + 70))
    icon3 = icon_model(icons[2], (60, 60), (icon1_loc[0], icon1_loc[1] + 140))
    menu=menu_model(menu,menu_icons,(40,40),(menu_on[0],0,padHeight-40),(menu_wifi[0],1080,padHeight-40))

    chrome = []
    chrome.append((chrome_on[1], 838, 176))
    chrome.append((chrome_on[0], 138, 138))
    chrome.append((chrome_on[2], 364, 54))


    """
    반복문
    """
    crashed=False
    ts_now_i = time.time()
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                crashed=True
            if hour>=3:
                crashed=True
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
            (init_x,init_y,windowmove1,windowins1)=window_move(window1,windowmove1,windowins1,init_x,init_y,mouse_x,mouse_y)
        if icondraw2 and rec_sub(window2, mouse_x, mouse_y):
            (init_x, init_y, windowmove2,windowins2) = window_move(window2, windowmove2,windowins2, init_x, init_y, mouse_x, mouse_y)
        if icondraw3 and rec_sub(window3, mouse_x, mouse_y):
            (init_x, init_y, windowmove3,windowins3) = window_move(window3, windowmove3,windowins3, init_x, init_y, mouse_x, mouse_y)
        """
        우선도에 따라 이미지 삽입
        """
        for x in imp_range:
            x.constr()
            if x.ID==1:
                x.chrome_online(chrome)
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
    """
    게임판 준비 및 프레임 설정
    """
    pygame.init() #파이겜 모듈을 전부 넣어줌
    gamepad=pygame.display.set_mode((padWidth,padHeight)) #게임판 크기 설정. 모드 안에 튜플로 넣어야 함
    pygame.display.set_caption('PyGame Test')#제목 설정
    clock=pygame.time.Clock()#초당 프레임 설정. 30 또는 60

    bg=pygame.image.load("image/bg.png")
    """
    창 구현에 필요한 요소
    """
    windows=[]
    for i in range(3):
        windows.append(pygame.image.load("image/window_model.png"))
    icons=[]
    for i in range(3):
        icons.append(pygame.image.load("image/icon.png"))
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
    menu_icons.append(pygame.image.load("image/menu_icon1.png"))
    menu_icons.append(pygame.image.load("image/menu_icon2.png"))
    menu_icons.append(pygame.image.load("image/menu_icon3.png"))

    menu_on=[]
    menu_on.append(pygame.image.load("image/menu_on_icon1.png"))

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
    런게임 실행
    """
    runGame()
"""
인잇게임을 실행
"""
if __name__=='__main__':
    initGame()