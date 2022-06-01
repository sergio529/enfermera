import pygame
import random

from pygame.locals import*
vel=10
mov=250
mov2=0
x=500
y=550
k=0
    
class Cursor(pygame.Rect):
    def  __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
        
    
        
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=200,y=200):
        self.imagen_normal=imagen1
        self.imagen_seleccion=imagen2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)
        
    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal
        pantalla.blit(self.imagen_actual,self.rect)

    
        
def mov_up(movarriba,vel,x,y):
    reloj=pygame.time.Clock()
    pygame.init()
    scr=pygame.display.set_mode((1080,680))

    fondo=pygame.image.load("fondo.png").convert()
    joyup1=pygame.image.load("joyb1.png").convert_alpha()
    tjoyup1=joyup1.get_rect()
    a=0
    tjoyup1.centerx=x
    tjoyup1.centery=y
    pacientes1=pygame.image.load("pacientesbt.png")
    pacientes2=pygame.image.load("pacientesbt2.png")
    enfermetabt1=pygame.image.load("enfermerabt.png")
    enfermetabt2=pygame.image.load("enfermerabt2.png")
    medicamentosbt1=pygame.image.load("medicamentosbt.png")
    medicamentosbt2=pygame.image.load("medicamentosbt2.png")
    inventariobt1=pygame.image.load("inventariobt.png")
    inventariobt2=pygame.image.load("inventariobt2.png")
    entregarbt1=pygame.image.load("entregarbt.png")
    entregarbt2=pygame.image.load("entregarbt2.png")
    pll1=pygame.image.load("p1.png")
    pll2=pygame.image.load("p2.png")
    pll3=pygame.image.load("p3.png")
    cama=pygame.image.load("cama.png")
    cama1=pygame.image.load("cama1.png")
    cama2=pygame.image.load("cama2.png")
    cama3=pygame.image.load("cama3.png")
    ventana1=pygame.image.load("pop up.png")
    ventana2=pygame.image.load("medicamen.png")
    ventana3=pygame.image.load("ventana33.png")
    salir=pygame.image.load("salir.jpg")
    heart=pygame.image.load("heart.png").convert_alpha()
    heartb=pygame.image.load("heartb.png").convert_alpha()
    theart=heart.get_rect()
    theartb=heartb.get_rect()
    

    bt1=Boton(pacientes1,pacientes2,704,20)
    bt2=Boton(enfermetabt1,enfermetabt2,704,120)
    bt3=Boton(medicamentosbt1,medicamentosbt2,704,220)
    bt4=Boton(inventariobt1,inventariobt2,704,320)
    bt5=Boton(entregarbt1,entregarbt2,704,420)
    pbt1=Boton(pll1,pll1,407,405)
    pbt2=Boton(pll2,pll2,519,405)
    pbt3=Boton(pll3,pll3,631,405)
    cbt0=Boton(cama,cama,90,80)
    cbt1=Boton(cama1,cama1,300,75)
    cbt2=Boton(cama2,cama2,430,80)
    cbt3=Boton(cama3,cama3,600,80)
    cbt4=Boton(cama,cama,30,430)
    cbt5=Boton(cama,cama,140,430)
    salir=Boton(salir,salir,30,407)
    pu1=Boton(ventana1,ventana1,30,30)
    me1=Boton(ventana2,ventana2,30,30)
    enf1=Boton(ventana3,ventana3,30,30)
    joy=Boton(joyup1,joyup1,500,550)

    cursor=Cursor()
    
    while(a<=movarriba):
        reloj.tick(400)
        scr.blit(fondo,(0,0))
        scr.blit(joyup1,(tjoyup1.centerx,tjoyup1.centery))

        tjoyup1.centery=tjoyup1.centery-vel
        a=a+vel
        
        bt1.update(scr,cursor)
        bt2.update(scr,cursor)
        bt3.update(scr,cursor)
        bt4.update(scr,cursor)
        bt5.update(scr,cursor)
        pbt1.update(scr,cursor)
        pbt2.update(scr,cursor)
        pbt3.update(scr,cursor)
        cbt0.update(scr,cursor)
        cbt1.update(scr,cursor)
        cbt2.update(scr,cursor)
        cbt3.update(scr,cursor)
        cbt4.update(scr,cursor)
        cbt5.update(scr,cursor)
        pygame.display.flip()
    return(tjoyup1.centery)

    

def mov_down(movarriba,vel,x,y):
    reloj=pygame.time.Clock()
    pygame.init()
    fondo=pygame.image.load("fondo.png").convert()
    joyup1=pygame.image.load("joyb1.png").convert_alpha()
    tjoyup1=joyup1.get_rect()
    a=0
    tjoyup1.centerx=x
    tjoyup1.centery=y
    scr=pygame.display.set_mode((1080,680))
    pacientes1=pygame.image.load("pacientesbt.png")
    pacientes2=pygame.image.load("pacientesbt2.png")
    enfermetabt1=pygame.image.load("enfermerabt.png")
    enfermetabt2=pygame.image.load("enfermerabt2.png")
    medicamentosbt1=pygame.image.load("medicamentosbt.png")
    medicamentosbt2=pygame.image.load("medicamentosbt2.png")
    inventariobt1=pygame.image.load("inventariobt.png")
    inventariobt2=pygame.image.load("inventariobt2.png")
    entregarbt1=pygame.image.load("entregarbt.png")
    entregarbt2=pygame.image.load("entregarbt2.png")
    pll1=pygame.image.load("p1.png")
    pll2=pygame.image.load("p2.png")
    pll3=pygame.image.load("p3.png")
    cama=pygame.image.load("cama.png")
    cama1=pygame.image.load("cama1.png")
    cama2=pygame.image.load("cama2.png")
    cama3=pygame.image.load("cama3.png")
    ventana1=pygame.image.load("pop up.png")
    ventana2=pygame.image.load("medicamen.png")
    ventana3=pygame.image.load("ventana33.png")
    salir=pygame.image.load("salir.jpg")
    heart=pygame.image.load("heart.png").convert_alpha()
    heartb=pygame.image.load("heartb.png").convert_alpha()
    theart=heart.get_rect()
    theartb=heartb.get_rect()

    bt1=Boton(pacientes1,pacientes2,704,20)
    bt2=Boton(enfermetabt1,enfermetabt2,704,120)
    bt3=Boton(medicamentosbt1,medicamentosbt2,704,220)
    bt4=Boton(inventariobt1,inventariobt2,704,320)
    bt5=Boton(entregarbt1,entregarbt2,704,420)
    pbt1=Boton(pll1,pll1,407,405)
    pbt2=Boton(pll2,pll2,519,405)
    pbt3=Boton(pll3,pll3,631,405)
    cbt0=Boton(cama,cama,90,80)
    cbt1=Boton(cama1,cama1,300,75)
    cbt2=Boton(cama2,cama2,430,80)
    cbt3=Boton(cama3,cama3,600,80)
    cbt4=Boton(cama,cama,30,430)
    cbt5=Boton(cama,cama,140,430)
    salir=Boton(salir,salir,30,407)
    pu1=Boton(ventana1,ventana1,30,30)
    me1=Boton(ventana2,ventana2,30,30)
    enf1=Boton(ventana3,ventana3,30,30)
    joy=Boton(joyup1,joyup1,500,550)

    fondo=pygame.image.load("fondo.png").convert()
    joyup1=pygame.image.load("joyf1.png").convert_alpha()
    tjoyup1=joyup1.get_rect()
    a=0
    tjoyup1.centerx=x
    tjoyup1.centery=y

    cursor=Cursor()
    
    while(a<=movarriba):
        reloj.tick(400)
        scr.blit(fondo,(0,0))
        scr.blit(joyup1,(tjoyup1.centerx,tjoyup1.centery))

        tjoyup1.centery=tjoyup1.centery+vel
        a=a+vel
        
        bt1.update(scr,cursor)
        bt2.update(scr,cursor)
        bt3.update(scr,cursor)
        bt4.update(scr,cursor)
        bt5.update(scr,cursor)
        pbt1.update(scr,cursor)
        pbt2.update(scr,cursor)
        pbt3.update(scr,cursor)
        cbt0.update(scr,cursor)
        cbt1.update(scr,cursor)
        cbt2.update(scr,cursor)
        cbt3.update(scr,cursor)
        cbt4.update(scr,cursor)
        cbt5.update(scr,cursor)
        pygame.display.flip()
    return(tjoyup1.centery)


        

def mov_right(movderecha,vel,x,y):
    
    reloj=pygame.time.Clock()
    pygame.init()
    scr=pygame.display.set_mode((1080,680))
   
    fondo=pygame.image.load("fondo.png").convert()
    joyup1=pygame.image.load("joyr1.png").convert_alpha()
    tjoyup1=joyup1.get_rect()
    a=0
    tjoyup1.centerx=x
    tjoyup1.centery=y
    pacientes1=pygame.image.load("pacientesbt.png")
    pacientes2=pygame.image.load("pacientesbt2.png")
    enfermetabt1=pygame.image.load("enfermerabt.png")
    enfermetabt2=pygame.image.load("enfermerabt2.png")
    medicamentosbt1=pygame.image.load("medicamentosbt.png")
    medicamentosbt2=pygame.image.load("medicamentosbt2.png")
    inventariobt1=pygame.image.load("inventariobt.png")
    inventariobt2=pygame.image.load("inventariobt2.png")
    entregarbt1=pygame.image.load("entregarbt.png")
    entregarbt2=pygame.image.load("entregarbt2.png")
    pll1=pygame.image.load("p1.png")
    pll2=pygame.image.load("p2.png")
    pll3=pygame.image.load("p3.png")
    cama=pygame.image.load("cama.png")
    cama1=pygame.image.load("cama1.png")
    cama2=pygame.image.load("cama2.png")
    cama3=pygame.image.load("cama3.png")
    ventana1=pygame.image.load("pop up.png")
    ventana2=pygame.image.load("medicamen.png")
    ventana3=pygame.image.load("ventana33.png")
    salir=pygame.image.load("salir.jpg")
    heart=pygame.image.load("heart.png").convert_alpha()
    heartb=pygame.image.load("heartb.png").convert_alpha()
    theart=heart.get_rect()
    theartb=heartb.get_rect()

    bt1=Boton(pacientes1,pacientes2,704,20)
    bt2=Boton(enfermetabt1,enfermetabt2,704,120)
    bt3=Boton(medicamentosbt1,medicamentosbt2,704,220)
    bt4=Boton(inventariobt1,inventariobt2,704,320)
    bt5=Boton(entregarbt1,entregarbt2,704,420)
    pbt1=Boton(pll1,pll1,407,405)
    pbt2=Boton(pll2,pll2,519,405)
    pbt3=Boton(pll3,pll3,631,405)
    cbt0=Boton(cama,cama,90,80)
    cbt1=Boton(cama1,cama1,300,75)
    cbt2=Boton(cama2,cama2,430,80)
    cbt3=Boton(cama3,cama3,600,80)
    cbt4=Boton(cama,cama,30,430)
    cbt5=Boton(cama,cama,140,430)
    salir=Boton(salir,salir,30,407)
    pu1=Boton(ventana1,ventana1,30,30)
    me1=Boton(ventana2,ventana2,30,30)
    enf1=Boton(ventana3,ventana3,30,30)
    joy=Boton(joyup1,joyup1,500,550)

    cursor=Cursor()
              
    while(a<=movderecha):
        reloj.tick(400)
        scr.blit(fondo,(0,0))
        scr.blit(joyup1,(tjoyup1.centerx,tjoyup1.centery))

        tjoyup1.centerx=tjoyup1.centerx+vel
        a=a+vel
        
        bt1.update(scr,cursor)
        bt2.update(scr,cursor)
        bt3.update(scr,cursor)
        bt4.update(scr,cursor)
        bt5.update(scr,cursor)
        pbt1.update(scr,cursor)
        pbt2.update(scr,cursor)
        pbt3.update(scr,cursor)
        cbt0.update(scr,cursor)
        cbt1.update(scr,cursor)
        cbt2.update(scr,cursor)
        cbt3.update(scr,cursor)
        cbt4.update(scr,cursor)
        cbt5.update(scr,cursor)
        pygame.display.flip()
    return(tjoyup1.centerx)

def mov_left(movderecha,vel,x,y):
    
    reloj=pygame.time.Clock()
    pygame.init()
    scr=pygame.display.set_mode((1080,680))
    
    fondo=pygame.image.load("fondo.png").convert()
    joyup1=pygame.image.load("joyl1.png").convert_alpha()
    tjoyup1=joyup1.get_rect()
    a=0
    tjoyup1.centerx=x
    tjoyup1.centery=y
    pacientes1=pygame.image.load("pacientesbt.png")
    pacientes2=pygame.image.load("pacientesbt2.png")
    enfermetabt1=pygame.image.load("enfermerabt.png")
    enfermetabt2=pygame.image.load("enfermerabt2.png")
    medicamentosbt1=pygame.image.load("medicamentosbt.png")
    medicamentosbt2=pygame.image.load("medicamentosbt2.png")
    inventariobt1=pygame.image.load("inventariobt.png")
    inventariobt2=pygame.image.load("inventariobt2.png")
    entregarbt1=pygame.image.load("entregarbt.png")
    entregarbt2=pygame.image.load("entregarbt2.png")
    pll1=pygame.image.load("p1.png")
    pll2=pygame.image.load("p2.png")
    pll3=pygame.image.load("p3.png")
    cama=pygame.image.load("cama.png")
    cama1=pygame.image.load("cama1.png")
    cama2=pygame.image.load("cama2.png")
    cama3=pygame.image.load("cama3.png")
    ventana1=pygame.image.load("pop up.png")
    ventana2=pygame.image.load("medicamen.png")
    ventana3=pygame.image.load("ventana33.png")
    salir=pygame.image.load("salir.jpg")
    heart=pygame.image.load("heart.png").convert_alpha()
    heartb=pygame.image.load("heartb.png").convert_alpha()
    theart=heart.get_rect()
    theartb=heartb.get_rect()

    bt1=Boton(pacientes1,pacientes2,704,20)
    bt2=Boton(enfermetabt1,enfermetabt2,704,120)
    bt3=Boton(medicamentosbt1,medicamentosbt2,704,220)
    bt4=Boton(inventariobt1,inventariobt2,704,320)
    bt5=Boton(entregarbt1,entregarbt2,704,420)
    pbt1=Boton(pll1,pll1,407,405)
    pbt2=Boton(pll2,pll2,519,405)
    pbt3=Boton(pll3,pll3,631,405)
    cbt0=Boton(cama,cama,90,80)
    cbt1=Boton(cama1,cama1,300,75)
    cbt2=Boton(cama2,cama2,430,80)
    cbt3=Boton(cama3,cama3,600,80)
    cbt4=Boton(cama,cama,30,430)
    cbt5=Boton(cama,cama,140,430)
    salir=Boton(salir,salir,30,407)
    pu1=Boton(ventana1,ventana1,30,30)
    me1=Boton(ventana2,ventana2,30,30)
    enf1=Boton(ventana3,ventana3,30,30)
    joy=Boton(joyup1,joyup1,500,550)

    cursor=Cursor()

    
    while(a<=movderecha):
        reloj.tick(400)
        scr.blit(fondo,(0,0))
        scr.blit(joyup1,(tjoyup1.centerx,tjoyup1.centery))

        tjoyup1.centerx=tjoyup1.centerx-vel
        a=a+vel
        
        bt1.update(scr,cursor)
        bt2.update(scr,cursor)
        bt3.update(scr,cursor)
        bt4.update(scr,cursor)
        bt5.update(scr,cursor)
        pbt1.update(scr,cursor)
        pbt2.update(scr,cursor)
        pbt3.update(scr,cursor)
        cbt0.update(scr,cursor)
        cbt1.update(scr,cursor)
        cbt2.update(scr,cursor)
        cbt3.update(scr,cursor)
        cbt4.update(scr,cursor)
        cbt5.update(scr,cursor)
        pygame.display.flip()
    return(tjoyup1.centerx)



def mov_paciente1():

    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(150,vel,x2,y2)
    x4=mov_right(125,vel,x3,y3)
    y4=y3
    oof=pygame.mixer.Sound("oof.wav")
    oof.play()
    x5=mov_left(125,vel,x4,y4)
    y5=y4
    x6=x5
    y6=mov_up(300,vel,x5,y5)
    x7=x6
    y7=mov_down(450,vel,x6,y6)
    x8=mov_right(225,vel,x7,y7)



def mov_paciente2():

    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(238,vel,x3,y3)
    y4=y3
    x5=mov_left(238,vel,x4,y4)
    y5=y4
    x6=x5
    oof=pygame.mixer.Sound("oof.wav")
    oof.play()
    y6=mov_up(130,vel,x5,y5)
    x7=mov_right(175,vel,x6,y6)
    y7=y6
    x8=x7
    y8=mov_up(180,vel,x7,y7)
    x9=x8
    y9=mov_down(180,vel,x8,y8)
    x10=mov_left(175,vel,x9,y9)
    y10=y9
    x11=x10
    y11=mov_down(260,vel,x10,y10)
    x12=mov_right(225,vel,x11,y11)



def mov_paciente3():
    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(352,vel,x3,y3)
    y4=y3
    x5=mov_left(352,vel,x4,y4)
    y5=y4
    x6=x5
    y6=mov_up(130,vel,x5,y5)
    x7=mov_right(340,vel,x6,y6)
    y7=y6
    x8=x7
    oof=pygame.mixer.Sound("oof.wav")
    oof.play()
    y8=mov_up(170,vel,x7,y7)
    x9=x8
    y9=mov_down(170,vel,x8,y8)
    x10=mov_left(340,vel,x9,y9)
    y10=y9
    x11=x10
    y11=mov_down(260,vel,x10,y10)
    x12=mov_right(225,vel,x11,y11)

def mov_paciente12():

    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(125,vel,x3,y3)
    y4=y3
    x5=mov_left(125,vel,x4,y4)
    y5=y4
    x6=x5
    y6=mov_up(130,vel,x5,y5)
    x7=mov_right(175,vel,x6,y6)
    y7=y6
    
    x8=x7
    y8=mov_up(180,vel,x7,y7)
    x9=x8
    y9=mov_down(180,vel,x8,y8)
    x10=mov_left(175,vel,x9,y9)
    y10=y9
    x11=x10
    y11=mov_down(260,vel,x10,y10)
    x12=mov_right(225,vel,x11,y11)

def mov_paciente13():
    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(125,vel,x3,y3)
    y4=y3
    x5=mov_left(125,vel,x4,y4)
    y5=y4
    x6=x5
    y6=mov_up(130,vel,x5,y5)
    x7=mov_right(340,vel,x6,y6)
    y7=y6
    oof=pygame.mixer.Sound("oof.wav")
    oof.play()
    x8=x7
    y8=mov_up(170,vel,x7,y7)
    x9=x8
    y9=mov_down(170,vel,x8,y8)
    x10=mov_left(340,vel,x9,y9)
    y10=y9
    x11=x10
    y11=mov_down(260,vel,x10,y10)
    x12=mov_right(225,vel,x11,y11)

def mov_paciente21():

    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(238,vel,x3,y3)
    y4=y3
    oof=pygame.mixer.Sound("oof.wav")
    oof.play()
    x5=mov_left(238,vel,x4,y4)
    y5=y4
    
    x6=x5
    y6=mov_up(300,vel,x5,y5)
    x7=x6
    y7=mov_down(430,vel,x6,y6)
    x8=mov_right(225,vel,x7,y7)

def mov_paciente31():

    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(352,vel,x3,y3)
    y4=y3
    x5=mov_left(352,vel,x4,y4)
    
    y5=y4
    x6=x5
    y6=mov_up(300,vel,x5,y5)
    x7=x6
    y7=mov_down(430,vel,x6,y6)
    x8=mov_right(225,vel,x7,y7)


def mov_paciente32():

    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(352,vel,x3,y3)
    y4=y3
    x5=mov_left(352,vel,x4,y4)
    y5=y4
    x6=x5
    y6=mov_up(130,vel,x5,y5)
    x7=mov_right(175,vel,x6,y6)
    y7=y6
    oof=pygame.mixer.Sound("oof.wav")
    oof.play()
    x8=x7
    y8=mov_up(180,vel,x7,y7)
    x9=x8
    y9=mov_down(180,vel,x8,y8)
    x10=mov_left(175,vel,x9,y9)
    y10=y9
    x11=x10
    y11=mov_down(260,vel,x10,y10)
    x12=mov_right(225,vel,x11,y11)

def mov_paciente23():
    
    x2=mov_left(225,vel,x,y)
    y2=y
    x3=x2
    y3=mov_up(130,vel,x2,y2)
    x4=mov_right(238,vel,x3,y3)
    y4=y3
    x5=mov_left(238,vel,x4,y4)
    y5=y4
    x6=x5
    y6=mov_up(130,vel,x5,y5)
    x7=mov_right(340,vel,x6,y6)
    
    y7=y6
    x8=x7
    y8=mov_up(170,vel,x7,y7)
    x9=x8
    y9=mov_down(170,vel,x8,y8)
    x10=mov_left(340,vel,x9,y9)
    y10=y9
    x11=x10
    y11=mov_down(260,vel,x10,y10)
    x12=mov_right(225,vel,x11,y11)
    
def txt(t):#funcion que permite ESCRIBIR EN LA VENTANA
    let=pygame.font.SysFont("ItalicT",20)
    imgtxt=let.render(t,True,(255,201,14),(250,250,250))
    return(imgtxt)

def txt2(t):#funcion que permite ESCRIBIR EN LA VENTANA
    let=pygame.font.SysFont("comic sans",30,)
    imgtxt=let.render(t,True,(0,0,0),(250,250,250))
    return(imgtxt)
       
  
def lain():
        pygame.init()
        scr=pygame.display.set_mode((1080,680))
       
        #carga fondo
        fondo=pygame.image.load("fondo.png").convert()
        joyup1=pygame.image.load("joyl1.png").convert_alpha()
        reloj=pygame.time.Clock()

        #Carga de imágenes 
        pacientes1=pygame.image.load("pacientesbt.png")
        pacientes2=pygame.image.load("pacientesbt2.png")
        enfermetabt1=pygame.image.load("enfermerabt.png")
        enfermetabt2=pygame.image.load("enfermerabt2.png")
        medicamentosbt1=pygame.image.load("medicamentosbt.png")
        medicamentosbt2=pygame.image.load("medicamentosbt2.png")
        inventariobt1=pygame.image.load("inventariobt.png")
        inventariobt2=pygame.image.load("inventariobt2.png")
        entregarbt1=pygame.image.load("entregarbt.png")
        entregarbt2=pygame.image.load("entregarbt2.png")
        pll1=pygame.image.load("p1.png")
        pll2=pygame.image.load("p2.png")
        pll3=pygame.image.load("p3.png")
        cama=pygame.image.load("cama.png")
        cama1=pygame.image.load("cama1.png")
        cama2=pygame.image.load("cama2.png")
        cama3=pygame.image.load("cama3.png")
        ventana1=pygame.image.load("pop up.png")
        ventana2=pygame.image.load("medicamen.png")
        ventana3=pygame.image.load("ventana33.png")
        enfermera1=pygame.image.load("b2.png")
        enfermera2=pygame.image.load("joyf1.png")
        salir=pygame.image.load("salir.jpg")
        chck=pygame.image.load("check.png")
        heart=pygame.image.load("heart.png").convert_alpha()
        heartb=pygame.image.load("heartb.png").convert_alpha()
        theart=heart.get_rect()
        theartb=heartb.get_rect()
        oof=pygame.mixer.Sound("oof.wav")
        perder=pygame.image.load("perder.png")
        skull=pygame.image.load("skull.png")
        time=pygame.image.load("reloj.png")
        
       
        
        
        

        tjoyup1=joyup1.get_rect()
        a=0
        tjoyup1.centerx=x
        tjoyup1.centery=y





        #definición botnoes
        bt1=Boton(pacientes1,pacientes2,704,20)
        bt2=Boton(enfermetabt1,enfermetabt2,704,120)
        bt3=Boton(medicamentosbt1,medicamentosbt2,704,220)
        bt4=Boton(inventariobt1,inventariobt2,704,320)
        bt5=Boton(entregarbt1,entregarbt2,704,420)
        pbt1=Boton(pll1,pll1,407,405)
        pbt2=Boton(pll2,pll2,519,405)
        pbt3=Boton(pll3,pll3,631,405)
        cbt0=Boton(cama,cama,90,80)
        cbt1=Boton(cama1,cama1,300,75)
        cbt2=Boton(cama2,cama2,430,80)
        cbt3=Boton(cama3,cama3,600,80)
        cbt4=Boton(cama,cama,30,430)
        cbt5=Boton(cama,cama,140,430)
        salir=Boton(salir,salir,30,407)
        enfermera1=Boton(enfermera1,enfermera1,280,107)
        enfermera2=Boton(enfermera2,enfermera2,80,107)
        pu1=Boton(ventana1,ventana1,30,30)
        me1=Boton(ventana2,ventana2,30,30)
        enf1=Boton(ventana3,ventana3,30,30)
        joy=Boton(joyup1,joyup1,500,550)
        chkbt1=Boton(chck,chck,495,500)
        chkbt2=Boton(chck,chck,407,365)
        chkbt3=Boton(chck,chck,520,365)
        chkbt4=Boton(chck,chck,632,365)
        chkbt5=Boton(chck,chck,308,35)
        chkbt6=Boton(chck,chck,440,35)
        chkbt7=Boton(chck,chck,610,35)
        skbt1=Boton(skull,skull,308,35)
        skbt2=Boton(skull,skull,440,35)
        skbt3=Boton(skull,skull,610,35)
        tmbt1=Boton(time,time,308,35)
        tmbt2=Boton(time,time,440,35)
        tmbt3=Boton(time,time,610,35)
        
        
        
        
        
        cursor=Cursor()



        #Variables cualquiera
        vent1=0
        vent2=0
        vent3=0
   
        joyc=0
        pildora=0
        paciente=0
        k=1
        pa=3
        pb=3
        pc=3
        punt=0
        s=0
        h=0
        hk1=0
        hk2=0
        hk3=0
        
        
    
    
        
        
        while(k<=4):
            
            if(1==1):
                    s=s+1
                    if(s==60):
                       h=h+1
                       s=0
                       hk1=hk1+1
                       hk2=hk2+1
                       hk3=hk3+1
                    if(h==24):
                        h=0
                       
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if cursor.colliderect(salir.rect):
                        vent1=0
                        vent2=0
                        vent3=0
                        joyc=0
                        paciente=0
                    if cursor.colliderect(bt2.rect):
                        vent3=1

                    if cursor.colliderect(bt5.rect):
                        
                         pygame.quit()
                            
                    if cursor.colliderect(bt1.rect):
                        vent1=1
                        joyc=0
                        pildora=0
                    if cursor.colliderect(bt3.rect):
                        vent2=1
                        joyc=0
                        pildora=0
                    
                        
                    if cursor.colliderect(joy.rect):
                        
                        joyc=1

                    if cursor.colliderect(bt4.rect):
                        pa=3
                        pb=3
                        pc=3
                        
                        
                        
                    if cursor.colliderect(pbt1.rect) :
                        pildora=1
                    if cursor.colliderect(pbt2.rect) :
                        pildora=2
                    if cursor.colliderect(pbt3.rect) :
                        pildora=3
                        
                    
                    if cursor.colliderect(cbt1.rect):
                        paciente=1
                    if cursor.colliderect(cbt2.rect):
                        paciente=2
                    if cursor.colliderect(cbt3.rect):
    
                        paciente=3
                        
                        
                    
                         
        
            if (vent1==0 and vent2==0 and vent3==0):            
                reloj.tick(20)
                cursor.update()
                bt1.update(scr,cursor)
                bt2.update(scr,cursor)
                bt3.update(scr,cursor)
                bt4.update(scr,cursor)
                bt5.update(scr,cursor)
                pbt1.update(scr,cursor)
                pbt2.update(scr,cursor)
                pbt3.update(scr,cursor)
                cbt0.update(scr,cursor)
                cbt1.update(scr,cursor)
                cbt2.update(scr,cursor)
                cbt3.update(scr,cursor)
                cbt4.update(scr,cursor)
                cbt5.update(scr,cursor)
            if(vent1==1):
                reloj.tick(20)
                cursor.update()
                pu1.update(scr,cursor)
                salir.update(scr,cursor)
            if(vent2==1):
                reloj.tick(20)
                cursor.update()
                me1.update(scr,cursor)
                salir.update(scr,cursor)
            if(vent3==1):
                reloj.tick(20)
                cursor.update()
                enf1.update(scr,cursor)
                salir.update(scr,cursor)
                enfermera1.update(scr,cursor)
                enfermera2.update(scr,cursor)
            if(joyc==1):
                chkbt1.update(scr,cursor)
            if(pildora==1):
                chkbt2.update(scr,cursor)
            if(pildora==2):
                chkbt3.update(scr,cursor)
            if (pildora==3):
                chkbt4.update(scr,cursor)
                
            if(paciente==1):
               chkbt5.update(scr,cursor)
            if(paciente==2):
               chkbt6.update(scr,cursor)
            if(paciente==3):
               chkbt7.update(scr,cursor)
            if(paciente==1 and pildora==1 and joyc==1):
                mov_paciente1()
                paciente=0
                pildora=0
                joyc=0
                pa=pa-1
                punt=punt+1
                k=k+1
               
            if(paciente==2 and pildora==2 and joyc==1):
                mov_paciente2()
                paciente=0
                pildora=0
                joyc=0
                pb=pb-1
                punt=punt+1
                k=k+1
                
            if(paciente==3 and pildora==3 and joyc==1):
                mov_paciente3()
                paciente=0
                pildora=0
                joyc=0
                punt=punt+1
                pc=pc-1
                k=k+1
            if(paciente==2 and pildora==1 and joyc==1 and hk2>=5):
                mov_paciente12()
                paciente=0
                pildora=0
                punt=punt+1
                joyc=0
                hk2=0
                pa=pa-1
                
        
                
            if(paciente==3 and pildora==1 and joyc==1):
                mov_paciente13()
                paciente=0
                pildora=0
                joyc=0
                k=k+1
                pa=pa-1
                punt=punt+1
                

            if(paciente==1 and pildora==2 and joyc==1):
                mov_paciente21()
                paciente=0
                pildora=0
                joyc=0
                pb=pb-1
                k=k+1
                punt=punt+1
            if(paciente==1 and pildora==3 and joyc==1 and hk1>=3 ):
                mov_paciente31()
                paciente=0
                pildora=0
                joyc=0
                hk1=0
                pc=pc-1
                punt=punt+1

            
                
            if(paciente==2 and pildora==3 and joyc==1 ):
                mov_paciente32()
                paciente=0
                pildora=0
                joyc=0
                k=k+1
                pc=pc-1
                punt=punt+1
            if(paciente==3 and pildora==2 and joyc==1 and hk3>=11):
                mov_paciente23()
                paciente=0
                pildora=0
                joyc=0
                hk3=0
                pb=pb-1
                punt=punt+1
                
          
                
            if(hk1==5):
                tmbt1.update(scr,cursor)
            if(hk1>=6):
                skbt1.update(scr,cursor)
                if(hk1==7):
                    k=5
            if(hk2==3):
                tmbt2.update(scr,cursor)
            if(hk2>=4):
                skbt2.update(scr,cursor)
                if(hk1==5):
                    k=5
            if(hk3==11):
                tmbt3.update(scr,cursor)
            if(hk3>=12):
                skbt3.update(scr,cursor)
                if(hk3==12):
                    k=5
            
            



            #vidas
            if(k==0 or k==1):
              scr.blit(heart,(theart.centerx-5,theart.centery+625))
              scr.blit(heart,(theart.centerx+20,theart.centery+625))
              scr.blit(heart,(theart.centerx+45,theart.centery+625))
            if(k==2):
              scr.blit(heartb,(theartb.centerx+4,theartb.centery+631))
              scr.blit(heart,(theart.centerx+20,theart.centery+625))
              scr.blit(heart,(theart.centerx+45,theart.centery+625))
          
            if(k==3):
              scr.blit(heartb,(theartb.centerx+4,theartb.centery+631))
              scr.blit(heartb,(theartb.centerx+29,theartb.centery+631))
              scr.blit(heart,(theart.centerx++45,theart.centery+625))
          
            if(k>=4):
             
              scr.blit(heartb,(theartb.centerx++4,theartb.centery+631))
              scr.blit(heartb,(theartb.centerx+29,theartb.centery+631))
              scr.blit(heartb,(theartb.centerx+54,theartb.centery+631))
              scr.blit(perder,(440,220))
             

            
            
                
            h1=str(h)
            s1=str(s)
            t5="Hora:"+h1+":"+s1
            
            
            imgtiem=txt2(t5)
            t=str(pa)
            t2=str(pb)
            t3=str(pc)
            t4="PUNTUACIÒN: "+ str(punt)
            img1=txt(t)
            img2=txt(t2)
            img3=txt(t3)
            img4=txt(t4)
            scr.blit(img1,(420,365))
            scr.blit(img2,(540,365))
            scr.blit(img3,(650,365))
            scr.blit(img4,(750,600))
            scr.blit(imgtiem,(10,320))
            
           
          
            
            pygame.display.flip()
            

        
            scr.blit(fondo,(0,0))
            scr.blit(joyup1,(tjoyup1.centerx,tjoyup1.centery))
            print(k)
        
    
            
                
                        
        
"""x2=mov_left(mov,vel,x,y)
                        y2=y
                        x3=x2
                        y3=mov_up(mov,vel,x2,y2)
                        mov2=372
                        x4=mov_right(mov2,vel,x3,y3)
                        y4=y3
                        x5=x4
                        mov3=200
                        y5=mov_up(mov3,vel,x4,y4)"""
lain()
    
        
        
        
    
    
