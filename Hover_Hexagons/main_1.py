#   _       ____  ________   ____
#  | \   | |    |    |      |
#  |  \  | |    |    |      |----
#  |   \_| |____|    |      |____

# Bấm a,b,c để đổi kiểu hover

import pygame,math
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
gradient_hover = Gradient_circle((255,0,0),(300,300))
while play:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    # print(mouse_x,mouse_y)
    #1 Vòng for bắt sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                screen.fill((0,0,0))
                list_hover = []
                hover_1 = True
                hover_2 = False
                hover_3 = False
            if event.key == pygame.K_b:
                screen.fill((0,0,0))
                list_hover_1 = []
                hover_2 = True
                hover_3 = False
                hover_1 = False
            if event.key == pygame.K_c:
                list_hover = []
                hover_3 = True
                hover_1 = False
                hover_2 = False
            
    #2 Hiệu ứng hightlight animotion
    if hover_3:
        screen.fill((0,0,0))
        for i in list_hover:
            
            screen.blit(gradient_hover,gradient_hover.get_rect(center = (i[0],i[1])))
        try:
            for i in list_hover:
                list_hover.remove(i)
        except:
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
                list_hover_1.append([(size_x*i,size_y*j-25),(size_x*i,size_y*(j+1)-25),(size_x*i,size_y*(j-1)-25),(size_x*i+size_x/2,size_y*j+size_y/2-25),(size_x*i+size_x/2,size_y*(j-1)+size_y/2-25),(size_x*(i-1)+size_x/2,size_y*j+size_y/2-25),(size_x*(i-1)+size_x/2,size_y*(j-1)+size_y/2-25),255])
            if 0 < math.pow((mouse_x -(size_x*i+size_x/2)),2) + math.pow((mouse_y - (size_y*j+size_y/2-25)),2) < size*size-300:
                list_hover.append([size_x*i+size_x/2,size_y*j+size_y/2-25,255,size])
                list_hover_1.append([(size_x*i+size_x/2,size_y*j+size_y/2-25),(size_x*i+size_x/2,size_y*(j+1)+size_y/2-25),(size_x*i+size_x/2,size_y*(j-1)+size_y/2-25),(size_x*i,size_y*j-25),(size_x*i,size_y*(j+1)-25),(size_x*(i+1),size_y*j-25),(size_x*(i+1),size_y*(j+1)-25),255])
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
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[0],size))      
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[1],size))      
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[2],size))      
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[3],size))      
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[4],size))      
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[5],size))      
            pygame.draw.polygon(screen,(0,i[7],i[7]),Hexagons(i[6],size))
        try:
            for i in list_hover_1:
                list_hover_1.remove(i)
        except:
            list_hover_1 = []

    pygame.display.flip()
pygame.quit()