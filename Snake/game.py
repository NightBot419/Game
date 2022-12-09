import pygame,random

def direction_snake(changeto,direction):
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
    return direction
def snakepos_snake(direction,snakepos):
    if direction == 'RIGHT':
        snakepos[0] += 9
    if direction == 'LEFT':
        snakepos[0] -= 9
    if direction == 'UP':
        snakepos[1] -= 9
    if direction == 'DOWN':
        snakepos[1] += 9
    return snakepos
def score_display(game_active):
    if game_active:
        score_a = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_a.get_rect(center = (200,550))
        pygame.draw.rect(screen,(0,0,0),(0,500,400,100))
        screen.blit(score_a,score_rect)
    else:
        score_a = game_font.render(f'Score:{int(score)}',True,(255,255,255))
        score_rect = score_a.get_rect(center = (200,100))
        screen.blit(score_a,score_rect)
        hight_score_a = game_font.render(f'Hight Score:{int(hight_score)}',True,(255,255,255))
        hight_score_rect = hight_score_a.get_rect(center = (200,400))
        screen.blit(hight_score_a,hight_score_rect)

pygame.init()

screen = pygame.display.set_mode((400,600))
clock = pygame.time.Clock()
play = True

snakepos = [200,200]
snakebody = [[200,209],[200,218],[200,227]]
foodx = random.randrange(1,48)
foody = random.randrange(1,48)
foodpos = [foodx * 8, foody * 8]
foodflat = True
direction = 'RIGHT'
changeto = direction
score = 0
with open("Program/data.txt","r") as file:
    hight_score = file.read()
game_font = pygame.font.Font('Program/!000001.ttf',40)
a = pygame.draw.rect(screen,(0,0,0),(snakepos[0],snakepos[1],8,8))
b = pygame.draw.rect(screen,(0,0,0),(foodpos[0],foodpos[1],8,8))
game_active = True
while play:
    screen.fill((225,225,208))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            if event.key == pygame.K_SPACE:
                game_active = True
                direction = 'RIGHT'
                changeto = direction
                score = 0
                snakepos = [200,200]
                snakebody = [[200,209],[200,218],[200,227]]
                foodflat = False
    if game_active:
        direction = direction_snake(changeto,direction)
        snakepos = snakepos_snake(direction,snakepos)
        snakebody.insert(0,list(snakepos))
        if a.colliderect(b):
            score += 1
            foodflat = False
        else:
            snakebody.pop()
        if foodflat == False:
            foodx,foody = random.randrange(1,48),random.randrange(1,60)
            foodpos = [foodx * 8, foody * 8]
        foodflat = True
        list_snake = []
        for pos in snakebody:
            a = pygame.draw.rect(screen,(0,0,0),(pos[0],pos[1],8,8))
            list_snake.append(a)
        a = pygame.draw.rect(screen,(0,0,0),(snakebody[0][0],snakebody[0][1],8,8))
        for i in range(1,len(list_snake)):
            if a.colliderect(list_snake[i]):
                game_active = False
        b = pygame.draw.rect(screen,(0,0,0),(foodpos[0],foodpos[1],8,8))
        if 390 < snakepos[0] or snakepos[0] < 10 or 490 < snakepos[1] or snakepos[1] < 10:
            game_active = False
        if score > int(hight_score):
            hight_score = score
            with open("Program/data.txt","w") as file:
                file.write(str(hight_score)) 
        score_display(game_active)
    else:
        play_agin = game_font.render(f'Play agin',True,(255,0,0))
        play_agin_rect = play_agin.get_rect(center = (200,225))
        screen.blit(play_agin,play_agin_rect)
        play_agin = game_font.render(f'Press SPACE',True,(255,0,0))
        play_agin_rect = play_agin.get_rect(center = (200,275))
        screen.blit(play_agin,play_agin_rect)
        score_display(game_active)
    pygame.display.update()
    clock.tick(20)
pygame.quit()
            
