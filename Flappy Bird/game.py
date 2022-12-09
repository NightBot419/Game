import pygame, random

def draw(x):
	return pygame.transform.scale2x(pygame.image.load(x).convert())
def draw_alpha(x):
	return pygame.transform.scale2x(pygame.image.load(x).convert_alpha())
def score_display(game_active):
	if game_active:
		score_a = game_font.render(str(int(score)),True,(255,255,255))
		score_rect = score_a.get_rect(center = (216,100))
		screen.blit(score_a,score_rect)
	else:
		score_a = game_font.render(f'Score: {int(score)}',True,(255,255,255))
		score_rect = score_a.get_rect(center = (216,100))
		screen.blit(score_a,score_rect)
		hight_score_a = game_font.render(f'Hight Score: {int(hight_score)}',True,(255,255,255))
		hight_score_rect = hight_score_a.get_rect(center = (216,630))
		screen.blit(hight_score_a,hight_score_rect)

pygame.init()
floor_x = bird_moment = score = bird_index = 0
with open("Program/data.txt","r") as file:
    hight_score = file.read()
pipe_height = [525,550,575,600,625,650,675,700,725,750,775,800,825,850]
pipe_y = random.choice(pipe_height)
speed = 4
game_play = True
game_active = True

screen = pygame.display.set_mode((432,768))
clock = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird')

bg = draw("Program/bg.png")
floor = draw("Program/floor.png")
pipe = draw("Program/pipe.png")
pipe2 = draw("Program/pipe2.png")
pipe_rect = pipe.get_rect(center = (500,pipe_y))
pipe2_rect = pipe.get_rect(center = (500,pipe_y-750))
game_over = draw_alpha("Program/message.png")
game_over_rect = game_over.get_rect(center = (216,384))
bird_mid = draw_alpha("Program/bird.png")
bird_up = draw_alpha("Program/bird_up.png")
bird_down = draw_alpha("Program/bird_down.png")
bird_list = [bird_down,bird_mid,bird_up]
bird = bird_list[bird_index]
bird_rect = bird.get_rect(center = (100,350))

bird_flag = pygame.USEREVENT
pygame.time.set_timer(bird_flag,100)

flap_sound = pygame.mixer.Sound('Program/flap.wav')
hit_sound = pygame.mixer.Sound('Program/hit.wav')
score_sound = pygame.mixer.Sound('Program/score.wav')
game_font = pygame.font.Font('Program/04B_19.ttf',40)


while game_play:
	clock.tick(120)
	floor_x -= speed
	pipe2_rect.centerx -= speed
	pipe_rect.centerx -= speed
	bird_moment += 0.16
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_play = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if game_active:
					bird_moment = 0
					bird_moment = -6
					flap_sound.play()
				else:
					game_active = True
					bird_moment = 0
					bird_rect.centery = 300
					pipe_rect.centerx = pipe2_rect.centerx = 500
					pipe_y = random.choice(pipe_height)
					pipe_rect = pipe.get_rect(center = (500,pipe_y))
					pipe2_rect = pipe.get_rect(center = (500,pipe_y-750))
					score = 0
		if event.type == bird_flag:
			if bird_index < 2:
				bird_index += 1
			else:
				bird_index = 0
			bird , bird_rect = bird_list[bird_index], bird_list[bird_index].get_rect(center = (100,bird_rect.centery))
	screen.blit(bg,(0,0))
	if game_active:
		screen.blit(pipe,pipe_rect)
		screen.blit(pipe2,pipe2_rect)
		if pipe_rect.centerx <= -100 and pipe2_rect.centerx <= -100:
			pipe_rect.centerx = 500
			pipe2_rect.centerx = 500
			pipe_y = random.choice(pipe_height)
			pipe_rect = pipe.get_rect(center = (500,pipe_y))
			pipe2_rect = pipe.get_rect(center = (500,pipe_y-750))
		bird_rotated = pygame.transform.rotozoom(bird,-bird_moment*4,1)
		bird_rect.centery += bird_moment
		screen.blit(bird_rotated,bird_rect)
		if bird_rect.colliderect(pipe_rect) or bird_rect.colliderect(pipe2_rect) or bird_rect.top <= 0 or 675 <= bird_rect.bottom <= 700:
			hit_sound.play()
			game_active = False
		if pipe_rect.centerx <= bird_rect.centerx <= pipe2_rect.centerx + 3: 
			score_sound.play()
			score += 1
		if score <= 30:
			speed = 4
		elif score <= 100:
			speed = 5
		else:
			speed = 6
		if score > int(hight_score):
			hight_score = score
			with open("Program/data.txt","w") as file:
				file.write(str(hight_score))
		score_display(game_active)
	else:
		score_display(game_active)
		screen.blit(game_over,game_over_rect)
	screen.blit(floor,(floor_x,675))
	screen.blit(floor,(floor_x + 432,675))
	if floor_x <= -432:
		floor_x = 0
	pygame.display.update()
pygame.quit()