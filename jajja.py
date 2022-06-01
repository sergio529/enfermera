import pygame,sys
from pygame.locals import*

pygame.init()
ventana=pygame.display.set_mode((400,300))
pygame.display.set_caption("trece")



aux=1
while True:
    
    tiempo=pygame.time.get_ticks()/10000
    if(2==int(tiempo)):
              tiempo=0
    print(tiempo)
    tiempo=pygame.time.get_ticks()/1000
    
        
    for event in pygame.event.get():
        if event.type==QUIT:
          pygame.quit()
          sys.exit()
   
    
    pygame.display.update
