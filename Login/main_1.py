import pygame
def text(string,size,color):
    a = pygame.font.SysFont("Times News Roman", size)
    return a.render(string,True,color)
class ScreenFader:
    def __init__(self, screen, fade_color=(0, 0, 0), fade_speed=5):
        self.screen = screen
        self.fade_color = fade_color
        self.fade_speed = fade_speed
        self.fade_alpha = 0
        self.fading_in = False
        self.fading_out = False

    def start_fade_in(self):
        self.fading_in = True
        self.fading_out = False

    def start_fade_out(self):
        self.fading_in = False
        self.fading_out = True

    def update(self):
        if self.fading_in:
            self.fade_alpha = min(255, self.fade_alpha + self.fade_speed)
        elif self.fading_out:
            self.fade_alpha = max(0, self.fade_alpha - self.fade_speed)

    def draw(self):
        if self.fade_alpha > 0:
            fade_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
            fade_surface.fill(self.fade_color)
            fade_surface.set_alpha(self.fade_alpha)
            self.screen.blit(fade_surface, (0, 0))
def True_False(x):
    if x:
        return True
    else:
        return False
def gradientRect( window, a, b,c, size ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 3, 3 ) )
    pygame.draw.line( colour_rect, a,  ( 0,0 ), ( 2,0 ) )         
    pygame.draw.line( colour_rect, b, ( 0,1 ), ( 2,1 ) )
    pygame.draw.line( colour_rect, c, ( 0,2 ), ( 2,2 ) )
    return pygame.transform.smoothscale( colour_rect, ( size[0],size[1] ) )


pygame.init()
screen = pygame.display.set_mode((868,434))
screen_fader = ScreenFader(screen,(255,255,255),0.3)
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
list_set_alpha = []
index = 0
play_1 = False
play_2 = False
gradient_y = -868/2
#        ____   _       ____               _     ____       _      _     _    0  _
#\    / |    | | \   | |          |       / \   |    |     | \    / |   / \   | | \   |
# \  /  |    | |  \  | |   __     |      /---\  |____|     |  \  /  |  /---\  | |  \  |
#  \/   |____| |   \_| |____|     |____ /     \ |          |   \/   | /     \ | |   \_|
while play:
    # XÉT MỆNH ĐỀ
    User_click = True_False(a == "Username" and b != "Password*" or a == "" and b != "Password*" or a == "Username*" and b == "Password" or a == "" or a == "Username" or a == "Username*")
    Pass_click = True_False(b == "Password" and a != "Username*" or b == "" and a != "Username*" or b == "" or b == "Password" or b == "Password*")
    Animotion_User = True_False(Click_Mouse_User == True and a == "" and User_play == False or User_play == False and Click_Mouse_User == True and a == "Username")
    Animotion_Pass = True_False(Click_Mouse_Pass == True and b == "" and Pass_play == False or Pass_play == False and Click_Mouse_Pass == True and b == "Password")
    mouse_x,mouse_y = pygame.mouse.get_pos()
    #        ____   _       ____       ____  ____   ____      _      _     _    0  _
    #\    / |    | | \   | |          |     |    | |         | \    / |   / \   | | \   |
    # \  /  |    | |  \  | |   __     |---- |    | |         |  \  /  |  /---\  | |  \  |
    #  \/   |____| |   \_| |____|     |     |____| |         |   \/   | /     \ | |   \_|
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # CLICK VÀO USERNAME
                if 329 < mouse_x < 329+210 and 155 < mouse_y < 195:
                    User_play = True
                    Pass_play = False
                    Click_Mouse_User = True
                # CLICK VÀO PASSWORD
                elif 329 < mouse_x < 329+210 and 210 < mouse_y < 250:
                    User_play = False
                    Pass_play = True
                    Click_Mouse_Pass = True
                # CLICK VÀO Ô LOGIN
                elif 329 < mouse_x < 329+210 and 297.5 < mouse_y < 297.5+40:
                    if User_click:
                        User_play = True
                        Pass_play = False
                        Click_Mouse_User = True
                        a = "Username*"
                    elif Pass_click:
                        User_play = False
                        Pass_play = True
                        Click_Mouse_Pass = True
                        b = "Password*"
                    else:
                        speed = 5
                        index = 30
                        screen_fader.start_fade_in()
                else:
                    User_play = False
                    Pass_play = False
        if User_play:
            if a == "Username":
                a = ""
            if event.type == pygame.KEYDOWN:
                if a == "Username*":
                    a = ""
                if event.key == pygame.K_BACKSPACE:
                    a = a[:-1]
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_KP_ENTER or event.key == pygame.K_END or event.key == pygame.K_AC_BACK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_AT or event.key == pygame.K_ASTERISK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_CAPSLOCK or event.key == pygame.K_TAB:
                    pass
                else:
                    a += event.unicode
                    speed = 5
                    index = 9
            User_play = True
        if Pass_play: 
            if b == "Password":
                b = ""
            if event.type == pygame.KEYDOWN:
                if b == "Password*":
                    b = ""
                if event.key == pygame.K_BACKSPACE:
                    b = b[:-1]
                elif event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT or event.key == pygame.K_KP_ENTER or event.key == pygame.K_END or event.key == pygame.K_AC_BACK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_AT or event.key == pygame.K_ASTERISK or event.key == pygame.K_AMPERSAND or event.key == pygame.K_CAPSLOCK or event.key == pygame.K_TAB:
                    pass
                else:
                    b += "*"
                    speed = 5
                    index = 9
            Pass_play = True
    # TRƯỚC KHI BẤM LOGIN
        # HIỆU ỨNG SÓNG 
    gradient = gradientRect(screen,(0,0,0),(0,255,0),(0,0,0),(868,434))
    gradient_y += speed
    if gradient_y>868/2:
        gradient_y=-868/2
    screen.blit(gradient,(0,gradient_y))
        # TỐC ĐỘ SÓNG HIỆU ỨNG KHI CLICK LOGIN, NHẬP TK MK 
    if speed == 10 and index == 0 and a != "Username*" and a != "Username" or speed == 10 and index == 0 and b != "Password*" and b != "Password":
        play = False
        play_1 = True
    if index == 0:
        speed = 2
        screen_fader.start_fade_out()
    elif index == 20:
        speed = 7
    elif index == 10:
        speed = 10
    # HIỆU ỨNG HOVER CHO CÁC HÌNH VUÔNG
    for i in range(2,834,54):
        for j in range(2,417,54):
            pygame.draw.rect(screen,(59,59,59),(i,j,52,52))
            if i < mouse_x < i+52 and j < mouse_y < j +52:
                list_hover.append([i,j,255])
    for i in list_hover:
        pygame.draw.rect(screen,(59,i[2],59),(i[0],i[1],52,52))
    for i in list_hover:
        if i[2] > 59:
            i[2] -= 4
            pygame.draw.rect(screen,(59,i[2],59),(i[0],i[1],52,52))
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
        if a == "Username*":
            User_before = text(a,22,(255,0,0))
        else:
            User_before = text(a,22,WHITE)
        screen.blit(User_before,(348,170))
    else:
        User_before = text(a,20,(170,170,170))
        screen.blit(User_before,(343,167))
    if  Animotion_User:
        a = "Username"
        Click_Mouse_User = False
        User_y = 167
    # Hiệu ứng cho Password
    if Click_Mouse_Pass:
        if 209 <= Pass_y <= 222:
            Pass_y -= 1
        screen.blit(Pass_afther,(343,Pass_y))
        if b == "Password*":
            Pass_before = text(b,22,(255,0,0))
        else:
            Pass_before = text(b,22,WHITE)
        screen.blit(Pass_before,(348,227))
    else:
        Pass_before = text(b,20,(170,170,170))
        screen.blit(Pass_before,(343,221))
    if  Animotion_Pass:
        b = "Password"
        Click_Mouse_Pass = False
        Pass_y = 222
    # clock.tick(60)
    screen_fader.update()
    screen_fader.draw()
    pygame.display.flip()
#  SAU KHI BẤM LOGIN
while play_1:
    mouse_x,mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play_1 = False
    screen.fill((255,255,255))
    pygame.display.flip()

pygame.quit()
