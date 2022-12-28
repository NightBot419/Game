import pygame
def text(string,size,color):
    a = pygame.font.SysFont("Times News Roman", size)
    return a.render(string,True,color)

pygame.init()
screen = pygame.display.set_mode((868,434))
clock = pygame.time.Clock()
pygame.display.set_caption("SIGN IN")
play = True
r = 0
speed = 2
list_hover = []
list_circle = [-i for i in range(0,540,60)]
# 0
# COLOR
GREEN = (0,255,0)
WHITE = (255,255,255)
# TEXT
# 1
a = "Username"
User_before = text(a,18,(170,170,170))
User_play = False
# 2
b = "Password" 
Pass_before = text(b,18,(170,170,170))
Pass_play = False
# 3
Forgot = text("Forgot Password",19,WHITE)
Sign_up = text("Signup",22,GREEN)
# 4
Sign_in = text("SIGN IN", 30, GREEN)
Sign_in_rect = Sign_in.get_rect(center = (434,112))
# 5
Login = text("Login",27,GREEN)
Login_rect = Login.get_rect(center = (434,317))
# 6
Click_Mouse_User = False
User_y = 167
User_afther = text("Username:",16,WHITE)
Click_Mouse_Pass = False
Pass_y = 222
Pass_afther = text("Password:",16,WHITE)
# 7
index = 0
# VÒNG LẶP CHÍNH
while play:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        # if event.type == Speed:
        #     speed = 2
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 329 < mouse_x < 329+210 and 155 < mouse_y < 195:
                    User_play = True
                    Pass_play = False
                    Click_Mouse_User = True
                elif 329 < mouse_x < 329+210 and 210 < mouse_y < 250:
                    User_play = False
                    Pass_play = True
                    Click_Mouse_Pass = True
                elif 329 < mouse_x < 329+210 and 297.5 < mouse_y < 297.5+40:
                    speed = 5
                    index = 10
                elif 329 < mouse_x < 329+106 and 265 < mouse_y < 265+15:
                    speed = 5
                    index = 10
                elif 486 < mouse_x < 486+51 and 266 < mouse_y < 265+16:
                    speed = 5
                    index = 10
                else:
                    User_play = False
                    Pass_play = False
        if User_play:
            if a == "Username":
                a = ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    a = a[:-1]
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_KP_ENTER or event.key == pygame.K_END or event.key == pygame.K_AC_BACK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_AT or event.key == pygame.K_ASTERISK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_CAPSLOCK or event.key == pygame.K_TAB: 
                    pass
                else:
                    a += event.unicode
                    speed = 5
                    index = 10
            User_play = True
        if Pass_play: 
            if b == "Password":
                b = ""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    b = b[:-1]
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_KP_ENTER or event.key == pygame.K_END or event.key == pygame.K_AC_BACK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_AT or event.key == pygame.K_ASTERISK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_CAPSLOCK or event.key == pygame.K_TAB: 
                    pass
                else:
                    b += "*"
                    speed = 5
                    index = 10

            Pass_play = True
    # HIỆU ỨNG SÓNG        
    for i in list_circle:
        pygame.draw.circle(screen,(0, 245, 255),(434,217),i)
        pygame.draw.circle(screen,(0,0,0),(434,217),i-5)
    for i in range(len(list_circle)):
        list_circle[i] += speed
    for i in range(len(list_circle)):
        if list_circle[i] >= 540:
            list_circle.pop(0)
            list_circle.append(0)
            index -= 1
            break
    if index == 0:
        speed = 2
    # HIỆU ỨNG HOVER CHO CÁC HÌNH VUÔNG
    for i in range(4,868,54):
        for j in range(4,434,54):
            pygame.draw.rect(screen,(59,59,59),(i,j,50,50))
            if i < mouse_x < i+50 and j < mouse_y < j +50:
                list_hover.append([i,j,255])
    for i in list_hover:
        pygame.draw.rect(screen,(59,i[2],59),(i[0],i[1],50,50))
    for i in list_hover:
        if i[2] > 59:
            i[2] -= 4
            pygame.draw.rect(screen,(59,i[2],59),(i[0],i[1],50,50))
    # XÓA BỚT CÁC Ô VUÔNG ĐÃ HOVER
    try:
        for i in range(len(list_hover)):
            if list_hover[i][2] <= 59:
                list_hover.pop(i)
    except:
        pass
    # MÀN HÌNH ĐĂNG NHẬP
    #Text
    pygame.draw.rect(screen,(24,24,24),(309,67,250,300))
    pygame.draw.rect(screen,(50,50,50),(329,297.5,210,40))
    pygame.draw.rect(screen,(50,50,50),(329,150,210,50))
    pygame.draw.rect(screen,(50,50,50),(329,205,210,50))
    screen.blit(Sign_in,Sign_in_rect)
    screen.blit(Login,Login_rect)
    screen.blit(Forgot,(329,265))
    screen.blit(Sign_up,(486,266))
    # Hiệu ứng cho Username
    if Click_Mouse_User:
        if 154 <= User_y <= 167:
            User_y -= 1
        screen.blit(User_afther,(343,User_y))
        User_before = text(a,22,WHITE)
        screen.blit(User_before,(348,170))
    else:
        User_before = text(a,20,(170,170,170))
        screen.blit(User_before,(343,167))
    if  Click_Mouse_User == True and a == "" and User_play == False or User_play == False and Click_Mouse_User == True and a == "Username":
        a = "Username"
        Click_Mouse_User = False
        User_y = 167
    # Hiệu ứng cho Password
    if Click_Mouse_Pass:
        if 209 <= Pass_y <= 222:
            Pass_y -= 1
        screen.blit(Pass_afther,(343,Pass_y))
        Pass_before = text(b,22,WHITE)
        screen.blit(Pass_before,(348,227))
    else:
        Pass_before = text(b,20,(170,170,170))
        screen.blit(Pass_before,(343,221))
    if  Click_Mouse_Pass == True and b == "" and Pass_play == False or Pass_play == False and Click_Mouse_Pass == True and b == "Password":
        b = "Password"
        Click_Mouse_Pass = False
        Pass_y = 222
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
