#   _       ____  ________   ____
#  | \   | |    |    |      |
#  |  \  | |    |    |      |----
#  |   \_| |____|    |      |____

# Bấm a,b,c,d,e,f để đổi kiểu hover

import pygame,math,random
def Hexagons(poin,size):
    x,y = poin
    a = (x-size/2,y-float((math.sqrt(3)/2)*size))
    e = (x-size/2,y+float((math.sqrt(3)/2)*size))
    b = (x+size/2,y-float((math.sqrt(3)/2)*size))
    d = (x+size/2,y+float((math.sqrt(3)/2)*size))
    f = (x-size,y)
    c = (x+size,y)
    return (a,b,c,d,e,f)
def Gradient_line(color1,color2,color3,size):
    surface = pygame.Surface((3,3))
    pygame.draw.line(surface,color1,(0,0),(2,0))
    pygame.draw.line(surface,color2,(0,1),(2,1))
    pygame.draw.line(surface,color3,(0,2),(2,2))
    return pygame.transform.smoothscale(surface,(size[0],size[1]))
def Gradient_circle(color,size):
    surface = pygame.Surface((4,4))
    pygame.draw.circle(surface,color,(2,2),1) 
    return pygame.transform.smoothscale(surface,(size[0],size[1])) 
def Gradient_circle_2(size):
    surface = pygame.Surface((50,50))
    pygame.draw.circle(surface,(255,125,82),(25,25),25) 
    pygame.draw.circle(surface,(255,168,82),(25,25),24) 
    pygame.draw.circle(surface,(255,212,82),(25,25),23) 
    pygame.draw.circle(surface,(255,255,82),(25,25),22) 
    pygame.draw.circle(surface,(212,255,82),(25,25),21) 
    pygame.draw.circle(surface,(168,255,82),(25,25),20) 
    pygame.draw.circle(surface,(125,255,82),(25,25),19) 
    pygame.draw.circle(surface,(82,255,82),(25,25),18) 
    pygame.draw.circle(surface,(82,255,125),(25,25),17) 
    pygame.draw.circle(surface,(82,255,168),(25,25),16) 
    pygame.draw.circle(surface,(82,255,212),(25,25),15) 
    pygame.draw.circle(surface,(82,255,255),(25,25),14) 
    pygame.draw.circle(surface,(82,212,255),(25,25),13) 
    pygame.draw.circle(surface,(82,168,255),(25,25),12) 
    pygame.draw.circle(surface,(82,125,255),(25,25),11) 
    pygame.draw.circle(surface,(82,82,255),(25,25),10) 
    pygame.draw.circle(surface,(125,82,255),(25,25),9) 
    pygame.draw.circle(surface,(168,82,255),(25,25),8) 
    pygame.draw.circle(surface,(212,82,255),(25,25),7) 
    pygame.draw.circle(surface,(255,82,255),(25,25),6) 
    pygame.draw.circle(surface,(255,82,212),(25,25),5) 
    pygame.draw.circle(surface,(255,82,168),(25,25),4) 
    pygame.draw.circle(surface,(255,82,125),(25,25),3) 
    pygame.draw.circle(surface,(255,82,82),(25,25),2) 
    pygame.draw.circle(surface,(255,100,0),(25,25),1) 
    return pygame.transform.smoothscale(surface,(size[0],size[1]))  
def Gradient_circle_3(size):
    surface = pygame.Surface((10,10))
    pygame.draw.circle(surface,(255,0,0),(5,5),5)
    pygame.draw.circle(surface,(255,255,0),(5,5),4)
    pygame.draw.circle(surface,(0,0,255),(5,5),3)
    pygame.draw.circle(surface,(0,255,0),(5,5),2)
    pygame.draw.circle(surface,(255,0,255),(5,5),1)
    return pygame.transform.smoothscale(surface,(size[0],size[1]))  


pygame.init()
screen = pygame.display.set_mode((1000,680))
play = True
size = 40
size_x = size*3 + 4
size_y = size*(math.sqrt(3)) + 4
gradient = Gradient_line((0,0,0),(0,255,0),(0,0,0),(1000,680))
gradient_y_1 = 0
gradient_y_2 = -1000
list_hover = []
list_hover_1 = []
hover_1 = False
hover_2 = False
hover_3 = False
hover_4 = False
hover_5 = False
hover_6 = False
spaw_color = pygame.USEREVENT
pygame.time.set_timer(spaw_color,200)
q = w = e = 0
list_r = [i for i in range(1,6)]

color = (0,255,255)

while play:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    # print(mouse_x,mouse_y)
    #1 Vòng for bắt sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == spaw_color:
            q,w,e = random.choice([255,0]),random.choice([255,0]),random.choice([255,0])
            if q == e == w == 0:
                q,w,e = random.choice([255,0]),random.choice([255,0]),random.choice([255,0])
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((0,0,0))
                list_hover = []
                hover_1 = True
                hover_2 = False
                hover_5 = False
                hover_4 = False
                hover_6 = False
                hover_3 = False
            if event.key == pygame.K_b:
                screen.fill((0,0,0))
                list_hover_1 = []
                hover_2 = True
                hover_3 = False
                hover_1 = False
                hover_6 = False
                hover_5 = False
                hover_4 = False
            if event.key == pygame.K_d:
                list_hover = []
                hover_3 = True
                hover_1 = False
                hover_6 = False
                hover_2 = False       
                hover_4 = False       
                hover_5 = False       
            if event.key == pygame.K_e:
                list_hover = []
                hover_3 = False
                hover_1 = False
                hover_2 = False
                hover_5 = False
                hover_6 = False
                hover_4 = True       
            if event.key == pygame.K_c:
                list_hover = []
                hover_3 = False
                hover_1 = False
                hover_2 = False
                hover_4 = False       
                hover_5 = False       
                hover_6 = True       
            if event.key == pygame.K_f:
                list_hover = []
                hover_3 = False
                hover_1 = False
                hover_2 = False
                hover_4 = False       
                hover_6 = False       
                hover_5 = True       
    #2 Hiệu ứng hightlight animotion
    if hover_3:
        screen.fill((0,0,0))
        for i in list_hover:
            gradient_hover = Gradient_circle((q,w,e),(250,250))
            screen.blit(gradient_hover,gradient_hover.get_rect(center = (i[0],i[1])))
        list_hover = []
    elif hover_6:
        screen.fill((0,0,0))
        for i in list_hover:
            gradient_hover = Gradient_circle(color,(250,250))
            screen.blit(gradient_hover,gradient_hover.get_rect(center = (i[0],i[1])))
        list_hover = []
    elif hover_4:
        screen.fill((0,0,0))
        for i in list_hover:
            gradient_hover = Gradient_circle_2((250,250))
            screen.blit(gradient_hover,gradient_hover.get_rect(center = (i[0],i[1])))
        list_hover = []
    elif hover_5:
        screen.fill((0,0,0))
        for i in list_hover:
            gradient_hover = Gradient_circle_3((250,250))
            screen.blit(gradient_hover,gradient_hover.get_rect(center = (i[0],i[1])))
        list_hover = []
    else:
        gradient_y_1 += 5
        gradient_y_2 += 5
        if gradient_y_1 > 1000:
            gradient_y_1 = -1000
        if gradient_y_2 > 1000:
            gradient_y_2 = -1000
        screen.blit(gradient,(0,gradient_y_1))
        screen.blit(gradient,(0,gradient_y_2))
    #2 Các hình lục giác và hover
    for i in range(10):
        for j in range(11):
            pygame.draw.polygon(screen,(59,59,59),Hexagons((size_x*i,size_y*j-25),size))
            pygame.draw.polygon(screen,(59,59,59),Hexagons((size_x*i+size_x/2,size_y*j+size_y/2-25),size))
            if mouse_x == 0 and mouse_y == 0:
                pass
            elif 0 < (mouse_x - (size_x*i))*(mouse_x - (size_x*i)) + (mouse_y-(size_y*j-25))*(mouse_y-(size_y*j-25)) < size*size-300:
                list_hover.append([size_x*i,size_y*j-25,255,size])
                list_hover_1.append([(size_x*i,size_y*j-25),(size_x*i,size_y*(j+1)-25),(size_x*i,size_y*(j-1)-25),(size_x*i+size_x/2,size_y*j+size_y/2-25),(size_x*i+size_x/2,size_y*(j-1)+size_y/2-25),(size_x*(i-1)+size_x/2,size_y*j+size_y/2-25),(size_x*(i-1)+size_x/2,size_y*(j-1)+size_y/2-25)])
            if 0 < math.pow((mouse_x -(size_x*i+size_x/2)),2) + math.pow((mouse_y - (size_y*j+size_y/2-25)),2) < size*size-300:
                list_hover.append([size_x*i+size_x/2,size_y*j+size_y/2-25,255,size])
                list_hover_1.append([(size_x*i+size_x/2,size_y*j+size_y/2-25),(size_x*i+size_x/2,size_y*(j+1)+size_y/2-25),(size_x*i+size_x/2,size_y*(j-1)+size_y/2-25),(size_x*i,size_y*j-25),(size_x*i,size_y*(j+1)-25),(size_x*(i+1),size_y*j-25),(size_x*(i+1),size_y*(j+1)-25)])
    if hover_1:
        for i in list_hover:
            pygame.draw.polygon(screen,(59,i[2],i[2]),Hexagons((i[0],i[1]),i[3]))
        for i in list_hover:
            i[2] -= 4
        try:
            for i in list_hover:
                if i[2] <= 59:
                    list_hover.remove(i)
        except:
            list_hover = []
    if hover_2:
        for i in list_hover_1:
            for j in range(7):
                pygame.draw.polygon(screen,color,Hexagons(i[j],size))          
        list_hover_1 = []
    pygame.display.flip()
pygame.quit()