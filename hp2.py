import pygame
import time
pygame.init()
pygame.mixer.music.load("hps1.ogg")
pygame.mixer.music.play(loops=0)
gameexit=False
gamedisplay=pygame.display.set_mode((1100,650))
pygame.display.set_caption("Harry Potter")
clock= pygame.time.Clock()
image=pygame.image.load('hpi.jpg')
hr2=pygame.image.load('ring.png')
hog=pygame.image.load('hog.jpg')
bk=pygame.image.load('diary.jpg')
bk1=pygame.image.load('diary1.jpg')
hr3=pygame.image.load('loc.jpg')
hem=pygame.image.load('herm.jpg')
drc2=pygame.image.load('drc2.jpg')
ron=pygame.image.load('ron.jpg')
ron1=pygame.image.load('ron1.jpg')
hr3=pygame.image.load('loc.jpg')
cup1=pygame.image.load('cup1.jpg')
rh=pygame.image.load('ronher.jpg')
dim=pygame.image.load('loc1.jpg')
dim1=pygame.image.load('dim1.png')
dim2=pygame.image.load('dim2.png')
n1=pygame.image.load('nagine2.jpg')
n=pygame.image.load('nagine.jpg')
n2=pygame.image.load('nagni1.jpg')
h_r=pygame.image.load('r_h.jpg')
lb=pygame.image.load('lb.jpg')
lbk=pygame.image.load('lbk.png')
lbk1=pygame.image.load('lbk1.png')
lbk2=pygame.image.load('lbk2.png')
nk=pygame.image.load('lnkk.png')
wh=pygame.image.load('hhor.jpg')
wv=pygame.image.load('voldemort.jpg')
war2=pygame.image.load('war2.jpg')
war1=pygame.image.load('war.jpg')
hev=pygame.image.load('hpdd1.jpg')
atk1=pygame.image.load('volwar1.jpg')
atk3=pygame.image.load('war3.jpg')
atk4=pygame.image.load('volwar.jpg')
atk5=pygame.image.load('war4.png')
atk6=pygame.image.load('vol2.jpg')
atk2=pygame.image.load('ha.jpg')
atk7=pygame.image.load('hpa.jpg')
drc=pygame.image.load('drc.jpg')
dd=pygame.image.load('dd.jpg')
gamedisplay.blit(image,(80,80))
pygame.display.update()
time.sleep(1)
print("tap space bar to play")
def msge(msg,color,size):
    font=pygame.font.SysFont(None,size)
    screen_text=font.render(msg,True,color)
    gamedisplay.blit(screen_text,[100,500])
def hor1():
    #pygame.mixer.music.play(loops=0, startpos=0.0)
    
    global bk,bk1,drc,gameexit
    game=False
    x=20 
    y=600
    xc=0
    yc=0
    h=1
    flag=0
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
                break
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("destroy the tom riddles diary1")
                    gamedisplay.fill((20,210,200))
                    msge("1 Destroy The Tom Riddles Diary",(200,100,50),40)
                    pygame.display.update()
                    time.sleep(1)
                    flag=1
                if flag==1:
                    if event.key == pygame.K_LEFT:
                        xc = -20
                        yc = 0
                    if event.key == pygame.K_RIGHT:
                        xc = 20
                        yc = 0
                    if event.key == pygame.K_UP:
                        yc = -20
                        xc = 0
                    if event.key ==pygame.K_DOWN:
                        yc = 20
                        xc =0
                    x+=xc
                    y+=yc
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(bk1,(1000,0))
                    gamedisplay.blit(bk1,(800,200))
                    gamedisplay.blit(bk1,(600,500))
                    gamedisplay.blit(bk1,(400,0))
                    gamedisplay.blit(drc,(x,y))
                
                    pygame.draw.rect(gamedisplay,(25,50,60),[1040,40,20,20])
                    pygame.draw.rect(gamedisplay,(255,50,60),[840,240,20,20])
                    pygame.draw.rect(gamedisplay,(25,50,160),[640,540,20,20])
                    pygame.draw.rect(gamedisplay,(25,150,60),[440,40,20,20])
                    pygame.display.update()
                    if x==840 and y==240:
                        msge("Not This",(26,95,156),30)
                        pygame.display.update()
                    if x==640 and y==540:
                        msge("Not This",(26,95,156),30)
                        pygame.display.update()
                    if x==440 and y==40:
                        msge("Not This",(26,95,156),30)
                        pygame.display.update()
                    if x==1040 and y==40:
                        print("killed")
                        gamedisplay.blit(bk,(0,0))
                        pygame.display.update()
                        game=True
                        hor2()
                        break
    
def hor2():
    global hr2,bk1,flag,drc,gameexit
    game=False
    x=1020
    y=520
    xc=0
    yc=0
    h=1
    flag=0
    msge('press space bar to play',(200,5,255),40)
    pygame.display.update()
    time.sleep(1)
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("destroy the 2")
                    gamedisplay.fill((250,250,200))
                    msge("2 Destroy Marvolo Gaunts Ring",(20,190,50),40)
                    pygame.display.update()
                    time.sleep(1)
                    flag=1
                if flag==1:
                    if event.key == pygame.K_LEFT:
                        xc = -40
                        yc = 0
                    if event.key == pygame.K_RIGHT:
                        xc = 40
                        yc = 0
                    if event.key == pygame.K_UP:
                        yc = -40
                        xc = 0
                    if event.key ==pygame.K_DOWN:
                        yc = 40
                        xc =0
                    x+=xc
                    y+=yc
                
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(hr2,(0,0))
                    gamedisplay.blit(dd,(x,y))
                    pygame.draw.rect(gamedisplay,(25,50,160),[20,40,20,20])
                    pygame.display.update()
                    if x==20 and y==40:
                        print("killed")
                        msge("Destroyed",(20,20,232),30)
                        pygame.display.update()
                        time.sleep(0.5)
                        game=True
                        hor3()
                        break
def hor3():
    global hr2,bk1,flag,drc,gameexit
    game=False
    x=400
    y=500
    xc=0
    yc=0
    h=1
    flag=0
    gamedisplay.fill((250,250,200))
    msge('press space bar to play',(200,5,255),40)
    time.sleep(1)
    pygame.display.update()
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("destroy the 3")
                    gamedisplay.fill((250,250,200))
                    msge("3 Destroy Salazar Slytherins Locket",(200,100,50),40)
                    pygame.display.update()
                    time.sleep(1)
                    flag=1
                if flag==1:
                    if event.key == pygame.K_LEFT:
                        xc = -20
                        yc = 0
                    if event.key == pygame.K_RIGHT:
                        xc = 20
                        yc = 0
                    if event.key == pygame.K_UP:
                        yc = -20
                        xc = 0
                    if event.key ==pygame.K_DOWN:
                        yc = 20
                        xc =0
                    x+=xc
                    y+=yc
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(hr3,(0,0))
                    gamedisplay.blit(ron,(x,y))
                    gamedisplay.blit(hem,(900,400))
                    gamedisplay.blit(drc2,(50,400))
                    pygame.draw.rect(gamedisplay,(25,250,60),[100,100,20,20])
                    pygame.display.update()
                    if x==100 and y==100 :
                        print("killed")
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(ron1,(0,0))
                        pygame.display.update()
                        msge("Destroyed",(20,20,232),40)
                        pygame.display.update()
                        time.sleep(2)
                        game=True
                        hor4()
                        break
def hor4():
    global hr2,bk1,flag,drc,gameexit
    game=False
    x=400
    y=500
    xc=0
    yc=0
    h=1
    flag=0
    gamedisplay.fill((250,250,200))
    msge('press space bar to play',(200,5,255),40)
    pygame.display.update()
    time.sleep(1)
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("destroy the 4")
                    gamedisplay.fill((250,250,200))
                    msge("4 Destroy The Helga Hufflepuffs Cup",(200,100,50),40)
                    pygame.display.update()
                    time.sleep(1)
                    flag=1
                if flag==1:
                    if event.key == pygame.K_LEFT:
                        xc = -20
                        yc = 0
                    if event.key == pygame.K_RIGHT:
                        xc = 20
                        yc = 0
                    if event.key == pygame.K_UP:
                        yc = -20
                        xc = 0
                    if event.key ==pygame.K_DOWN:
                        yc = 20
                        xc =0
                    x+=xc
                    y+=yc
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(cup1,(0,0))
                    gamedisplay.blit(ron,(1000,400))
                    gamedisplay.blit(hem,(x,y))
                    pygame.draw.rect(gamedisplay,(205,50,60),[140,80,20,20])
                    pygame.display.update()
                    if x==140 and y==80:
                        print("killed")
                        gamedisplay.fill((255,255,255))
                        gamedisplay.blit(rh,(0,0))
                        msge("Destroyed",(20,20,232),30)
                        pygame.display.update()
                        time.sleep(1)
                        game=True
                        hor5()
                        break
def hor5():
    global hr2,bk1,flag,drc,gameexit
    game=False
    x=400
    y=500
    xc=0
    yc=0
    h=1
    flag=0
    gamedisplay.fill((250,250,200))
    msge('press space bar to play',(200,5,255),40)
    pygame.display.update()
    time.sleep(1)
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("5")
                    gamedisplay.fill((250,250,200))
                    msge("5 Destroy The Rowena Ravenclaws Diadem",(200,100,50),40)
                    pygame.display.update()
                    time.sleep(1)
                if event.key == pygame.K_LEFT:
                    xc = -20
                    yc = 0
                if event.key == pygame.K_RIGHT:
                    xc = 20
                    yc = 0
                if event.key == pygame.K_UP:
                    yc = -20
                    xc = 0
                if event.key ==pygame.K_DOWN:
                    yc = 20
                    xc =0
                x+=xc
                y+=yc
                gamedisplay.fill((250,250,200))
                gamedisplay.blit(dim,(0,0))
                gamedisplay.blit(drc2,(x,y))
                pygame.draw.rect(gamedisplay,(255,50,60),[160,40,20,20])
                pygame.display.update()
                if x==160 and y==40:
                    print("killed")
                    gamedisplay.blit(dim2,(0,0))
                    pygame.display.update()
                    time.sleep(0.5)
                    gamedisplay.fill((255,255,255))
                    gamedisplay.blit(dim1,(0,0))
                    pygame.display.update()
                    time.sleep(0.5)
                    msge("Destroyed",(20,20,232),30)
                    pygame.display.update()
                    time.sleep(0.5)
                    game=True
                    hor6()
                    break
def hor6():
    global gameexit
    game = False
    gamedisplay.fill((255,255,255))
    msge('press space bar to play',(200,5,255),40)
    time.sleep(0.5)
    pygame.display.update()
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("destroy the 6")
                    gamedisplay.fill((255,255,255))
                    msge("you are the horkruks: Harry",(200,100,50),40)
                    pygame.display.update()
                    time.sleep(1)
                    flag=1
                if flag==1:
                    gamedisplay.fill((250,250,200))
                    msge("you should die harry press 's'",(23,56,21),40)
                    gamedisplay.blit(wv,(400,100))
                    pygame.display.update()
                    if event.key == pygame.K_s:
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(wv,(400,100))
                        gamedisplay.blit(wh,(50,100))
                        pygame.display.update()
                        time.sleep(1)
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(war2,(0,50))
                       
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(war2,(0,50))
                        pygame.display.update()
                        time.sleep(1)
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(hev,(0,50))
                        msge("part of your soul is with voldemort you will be back soon",(200,32,61),40)
                        pygame.display.update()
                        time.sleep(2)
                        game=True
                        hor7()
                        break
def hor7():
    global hr2,bk1,flag,drc,gameexit
    game=False
    x=400
    y=500
    xc=0
    yc=0
    h=1
    flag=0
    gamedisplay.fill((250,250,200))
    msge('press space bar to play',(200,5,255),40)
    pygame.display.update()
    time.sleep(1)
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("destroy the 7")
                    gamedisplay.fill((250,250,200))
                    msge("7 Destroy Nagine",(200,100,50),40)
                    pygame.display.update()
                    time.sleep(1)
                    flag=1
                if flag==1:
                    if event.key == pygame.K_LEFT:
                        xc = -20
                        yc = 0
                    if event.key == pygame.K_RIGHT:
                        xc = 20
                        yc = 0
                    if event.key == pygame.K_UP:
                        yc = -20
                        xc = 0
                    if event.key ==pygame.K_DOWN:
                        yc = 20
                        xc =0
                    x+=xc
                    y+=yc
                
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(n1,(0,0))
                    gamedisplay.blit(h_r,(x,y))
                    pygame.draw.rect(gamedisplay,(255,50,60),[300,300,20,20])
                    pygame.display.update()
                    if x==300 and y==300:
                        gamedisplay.fill((255,255,255))
                        gamedisplay.blit(n2,(0,0))
                        pygame.display.update()
                        time.sleep(1)
                        gamedisplay.fill((255,255,255))
                        gamedisplay.blit(n,(0,0))
                        pygame.display.update()
                        if lonb()==1:
                            print("killed")
                            msge("Destroyed",(20,20,232),30)
                            pygame.display.update()
                            time.sleep(1)
                            game=True
                            war()
                            break
def lonb():
    global gameexit
    msge("long bottom can do it press 'l' to take his help",(100,20,35),40)
    pygame.display.update()
    time.sleep(1)
    global hr2,bk1,flag,drc
    game=False
    x=400
    y=500
    xc=0
    yc=0
    h=1
    flag=0
    while not game:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
                game=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_l:
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(n1,(0,0))
                    gamedisplay.blit(lb,(x,y))    
                    pygame.display.update()
                    h=0
                if h==0:
                    if event.key == pygame.K_LEFT:
                        xc = -20
                        yc = 0
                    if event.key == pygame.K_RIGHT:
                        xc = 20
                        yc = 0
                    if event.key == pygame.K_UP:
                        yc = -20
                        xc = 0
                    if event.key ==pygame.K_DOWN:
                        yc = 20
                        xc =0
                    x+=xc
                    y+=yc
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(n1,(0,0))
                    gamedisplay.blit(lb,(x,y))
                    pygame.draw.rect(gamedisplay,(255,50,60),[300,300,20,20])
                    pygame.display.update()
                    if x==300 and y==300:
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(lbk,(0,0))
                        pygame.display.update()
                        time.sleep(0.5)
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(lbk1,(x,y))    
                        pygame.display.update()
                        time.sleep(0.5)
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(lbk2,(x,y))    
                        pygame.display.update()
                        time.sleep(0.5)
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(nk,(x,y))    
                        pygame.display.update()
                        return 1

def war():
    gameexit= False
    gamedisplay.fill((250,250,200))
    msge("Its time to kill Voldemort",(255,30,26),50)
    pygame.display.update()
    time.sleep(1)
    gamedisplay.fill((250,250,200))
    gamedisplay.blit(war1,(10,10))
    pygame.display.update()
    time.sleep(0.5)
    msge("press 'g' to start war",(23,201,59),40)
    pygame.display.update()
    time.sleep(1)
    while not gameexit:
        for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_g:
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(hog,(100,25))
                    pygame.display.update()
                    time.sleep(1)
                    f=1
                if f == 1:
                    gamedisplay.fill((250,250,200))
                    gamedisplay.blit(wv,(50,100))
                    gamedisplay.blit(wh,(400,100))
                    msge("press 's' to spell stupify",(20,53,201),30)
                    pygame.display.update()
                    if event.key == pygame.K_s:
                      gamedisplay.fill((250,250,200))
                      gamedisplay.blit(wv,(50,100))
                      gamedisplay.blit(wh,(400,100))
                      pygame.display.update()
                      gamedisplay.fill((250,250,200))
                      gamedisplay.blit(wv,(50,100))
                      gamedisplay.blit(atk7,(400,100))
                      pygame.display.update()
                      time.sleep(1)      
                      gamedisplay.fill((250,250,200))
                      gamedisplay.blit(wv,(50,100))
                      gamedisplay.blit(wh,(400,100))
                      pygame.display.update()
                      gamedisplay.fill((250,250,200))
                      gamedisplay.blit(atk1,(50,100))
                      gamedisplay.blit(wh,(400,100))
                      pygame.display.update()
                      time.sleep(1)
                      gamedisplay.fill((250,250,200))
                      gamedisplay.blit(wv,(50,100))
                      gamedisplay.blit(wh,(400,100))
                      msge("press 'k' to spell ",(20,53,201),30)
                      pygame.display.update()
                      time.sleep(1)              
                    if event.key == pygame.K_k:
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(wv,(50,100))
                        gamedisplay.blit(wh,(400,100))
                        pygame.display.update()
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(wv,(50,100))
                        gamedisplay.blit(atk2,(400,100))
                        pygame.display.update()
                        time.sleep(1)
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(wv,(50,100))
                        gamedisplay.blit(wh,(400,100))
                        pygame.display.update()
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(atk6,(50,100))
                        gamedisplay.blit(wh,(400,100))
                        pygame.display.update()          
                        msge("press 'a' to spell avarakdavra",(201,36,53),40)
                        pygame.display.update()
                        time.sleep(1)
                    if event.key == pygame.K_a:
                        gamedisplay.fill((250,250,200))
                        gamedisplay.blit(atk5,(10,15))
                        pygame.display.update()
                        time.sleep(1)
                        gameexit=True

msge("Destroy All the horkruks to kill voldemort",[100,200,0],60)
pygame.display.update()
while not gameexit:
    gamedisplay.fill((250,250,200))
    hor1()
    msge("press 'q' to quit, Enter space to restart",(203,253,12),50)
    pygame.display.update()
    for event in pygame.event.get():
            if event.type is pygame.QUIT:
                gameexit=True
            if event.type is pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    gameexit=True
pygame.display.update() 
pygame.quit()
quit()
