import numpy
import pandas
import pygame
import random
import sys #exit from screen#
pygame.init()
WIDTH=800
HEIGHT=600
BACKGROUND_COLOR=(68,34,82)
player_position=[500,500]
player_size=50
enemy_size=50
enemy_pos=[random.randint(0,WIDTH-50),0]
enemy_list=[enemy_pos] #initially contains only one enemy #
speed=10
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #sets screen with given pixels#
game_over=0
score=0
clock=pygame.time.Clock() #to set frame time #
myFont=pygame.font.SysFont("monospace",35)
def set_level(score,speed):
	if score<20:
		speed=5
	elif score<40:
		speed=8
	elif score<60:
		speed=12
	else:
		speed=15
	return speed
def drop_enemies(enemy_list):
	delay=random.random()
	if len(enemy_list)<5 and delay<0.1:
		x_pos=random.randint(0,WIDTH-50)
		y_pos=0
		enemy_list.append([x_pos,y_pos])
def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.circle(screen,(124,57,201),(enemy_pos[0],enemy_pos[1]),20,20)
def update_enemy_positions(enemy_list,score):
	for idx,enemy_pos in enumerate(enemy_list):
		if(enemy_pos[1]>=0 and enemy_pos[1]<HEIGHT):
			enemy_pos[1]+=speed
		else:
			enemy_list.pop(idx)
			score+=1
	return score
def collision_check(enemy_list,player_position):
	for enemy_pos in enemy_list:
		if detect_collision(enemy_pos,player_position):
			return True
	return False
def detect_collision(player_position,enemy_pos):
	p_x=player_position[0]
	p_y=player_position[1]
	e_x=enemy_pos[0]
	e_y=enemy_pos[1]
	if (e_x>=p_x and (e_x<(p_x+60))) or (p_x>=e_x and (p_x<(e_x+60)) ):
		if(e_y>=p_y and e_y<(p_y+60)) or (p_y>=e_y and p_y<(e_y+60) ):
			return True
	return False
while not game_over:
	for event in pygame.event.get(): 	#get() will take the type of event#
		if event.type==pygame.QUIT:
			sys.exit
		if event.type==pygame.KEYDOWN:
			x=player_position[0]   # x=500 #
			y=player_position[1]   # y=500 #
			if event.key==pygame.K_LEFT:
				x-=player_size
			elif event.key==pygame.K_RIGHT:    #if we used else then for any key it would move user block to right #
				x+=player_size
			player_position=[x,y] # set new position #
	
	screen.fill(BACKGROUND_COLOR) #reset the screen/refill the screen #
	
	
	
	drop_enemies(enemy_list)
	score=update_enemy_positions(enemy_list,score)
	speed=set_level(score,speed)
	text="Score:" + str(score)
	label=myFont.render(text,1,(255,0,0))
	screen.blit(label,(WIDTH-200,HEIGHT-40))
	if collision_check(enemy_list,player_position):
		
		game_over=True
	draw_enemies(enemy_list)
	
	pygame.draw.rect(screen,(219,89,202),(player_position[0],player_position[1],50,50))	#rect(surface==screen,color(r,g,b),rect(x,y,height,width),width=0(optional))#
	clock.tick(50) #set speed of falling blocks #
	pygame.display.update() #in pygame we always need updated screen after every iteration#
pygame.init()
screena=pygame.display.set_mode((500,400))
myFonta=pygame.font.SysFont("monospace",35)
screen_time=0
screena.fill((195,13,116))
while not screen_time:
	for event in pygame.event.get():   
		if event.type==pygame.QUIT:
			screen_time=True
		else:
			myFont=pygame.font.SysFont("monospace",35)
			texta="SCORE IS:" + str(score)			
			labela=myFont.render(texta,1,(0,0,0))
			screena.blit(labela,(100,200))
			pygame.display.update()
			#
			
			
	
