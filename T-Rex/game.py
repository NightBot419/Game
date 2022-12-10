import pygame,random
def draw(x):
    return pygame.image.load(x).convert()
def move_tree(list_tree):
    for tree in list_tree:
        tree[1].centerx -= 5
    return list_tree
def draw_tree(list_tree):
    for tree_rect in list_tree:
        screen.blit(tree,tree_rect)
def score_display():
    score_a = font.render(f'Score: {int(score)}',True,(0,0,0))
    score_rect = score_a.get_rect(center = (900,50))
    screen.blit(score_a,score_rect)
    hight_score_a = font.render(f'Hight Score: {int(hight_score)}',True,(0,0,0))
    hight_score_rect = hight_score_a.get_rect(center = (800,50))
    screen.blit(hight_score_a,hight_score_rect)
pygame.init()
screen = pygame.display.set_mode((1000,500))
clock = pygame.time.Clock()
play = True
font = pygame.font.Font('Program/!000001.ttf',10)
rex_1 = pygame.transform.scale(draw("Program/rex1.0.jpg"),(50,50))
rex_2 = pygame.transform.scale(draw("Program/rex1.1.jpg"),(50,50))
rex_3 = pygame.transform.scale(draw("Program/rex1.2.jpg"),(50,50))
rex_4 = pygame.transform.scale(draw("Program/rex1.3.jpg"),(50,50))
rex_5 = pygame.transform.scale(draw("Program/rex1.4.jpg"),(50,50))
rex_6 = pygame.transform.scale(draw("Program/rex1.5.jpg"),(50,50))
tree_1 = pygame.transform.scale(draw("Program/tree1.jpg"),(50,50))
tree_2 = pygame.transform.scale(draw("Program/tree2.jpg"),(50,50))
tree_3 = pygame.transform.scale(draw("Program/tree3.jpg"),(50,50))
tree_4 = pygame.transform.scale(draw("Program/tree4.jpg"),(50,50))
tree_5 = pygame.transform.scale(draw("Program/tree5.jpg"),(50,50))
bird = pygame.transform.scale(draw("Program/bird.jpg"),(50,50))
gameover = pygame.transform.scale(draw("Program/gameover.jpg"),(200,100))
gameover_rect = gameover.get_rect(center = (500,200))
list_rex = [rex_1,rex_2,rex_4]
rex_index = score = 0
hight_score = 0
game = jump_1 = True
rex = list_rex[rex_index]
list_tree = [[tree_1,tree_2,tree_3,tree_4,tree_5],[bird]]
tree = list_tree[0]
rex_rect = rex.get_rect(center = (100,275))
rex_move = pygame.USEREVENT
pygame.time.set_timer(rex_move,100)
jump = down = False
spaw_tree = pygame.USEREVENT + 1
pygame.time.set_timer(spaw_tree,1200)
list_tree_move = []
while play:
    screen.fill((255,255,255))
    pygame.draw.line(screen,(0,0,0),(0,295),(1000,295))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == rex_move:
            if rex_index < 2:
                rex_index += 1
            else:
                rex_index = 0
            rex , rex_rect = list_rex[rex_index], list_rex[rex_index].get_rect(center = (100,rex_rect.centery))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                if game:
                    jump = True
                    jump_1 = True
                    down = False
                    rex , rex_rect = rex_1, rex_1.get_rect(center = (100,rex_rect.centery))
                else:
                    score = 0
                    list_tree_move.clear()
                    game = True
        if event.type == spaw_tree:
            a = random.choice(list_tree)
            if a == list_tree[0]:
                tree = random.choice(list_tree[0])
                list_tree_move.append([tree,tree.get_rect(center = (1200,275))])
            else:
                x = random.choice([270,230])
                list_tree_move.append([bird,bird.get_rect(center = (1200,x))])
    if game:
        if down:
            rex = rex_6
            rex_rect = rex.get_rect(center = (100,280))
            screen.blit(rex,rex_rect)
            list_tree_move = move_tree(list_tree_move)
            for i in list_tree_move:
                screen.blit(i[0],i[1])
            if len(list_tree_move) > 3:
                list_tree_move.pop(0)
            for tree_rect in list_tree_move:
                if rex_rect.colliderect(tree_rect[1]):
                    game = False
            score += 0.1
            score_display()
        else:
            list_tree_move = move_tree(list_tree_move)
            for i in list_tree_move:
                screen.blit(i[0],i[1])
            if len(list_tree_move) > 3:
                list_tree_move.pop(0)
            if jump:   
                rex , rex_rect = rex_3, rex_3.get_rect(center = (100,rex_rect.centery))
                if jump_1:
                    rex_rect.centery -= 5
                else:
                    rex_rect.centery += 7.5
                screen.blit(rex,rex_rect)
                if rex_rect.centery <= 125:
                    jump_1 = False
                if rex_rect.centery >= 275:
                    jump_1 = True
                    jump = False
            else:
                screen.blit(rex,rex_rect)
            for tree_rect in list_tree_move:
                if rex_rect.colliderect(tree_rect[1]):
                    game = False 
            score += 0.1
            score_display()
    else:
        for i in list_tree_move:
            screen.blit(i[0],i[1])
        rex = rex_5
        rex_rect = rex.get_rect(center = (rex_rect.centerx,rex_rect.centery))
        screen.blit(rex,rex_rect)
        if score > hight_score:
            hight_score = score
        score_display()
        screen.blit(gameover,gameover_rect)
    pygame.display.update()
    clock.tick(90)
pygame.quit()