'''@author Vipen Loka'''
import sys,pygame
import time
from random import randrange
score=0
def reset_screen():
	pygame.draw.rect(screen,(0,0,0),(0,0,500,500))
	if grid:
		draw_grid()
def draw_grid():
	for i in range(0,500,10):
		pygame.draw.line(screen,(255,255,255),(i,0),(i,500))

	for i in range(0,500,10):
		pygame.draw.line(screen,(255,255,255),(0,i),(500,i))

def head_move():
	global score,candy
	reset_screen()
	tail_move()
	if direction=='d':
		snake[0][1]+=10

	elif direction=='u':
		snake[0][1]-=10

	elif direction=='r':
		snake[0][0]+=10

	elif direction=='l':
		snake[0][0]-=10

	snake[0][0]%=500;snake[0][1]%=500
	# print(snake[0][:2],candy[:2])
	if snake[0][:2]==candy[:2]:
		score+=1
		snake.append([0,0,10,10])
		candy=[randrange(0,480,10),randrange(0,480,10),10,10]
	for i in range(len(snake)):
		pygame.draw.rect(screen,(0,255,255),snake[i])

def tail_move():
	for i in range(len(snake)-1,0,-1):
		snake[i][0]=snake[i-1][0]
		snake[i][1]=snake[i-1][1]


def display_candy():
	pygame.draw.rect(screen,(254,127,156),candy)

def frame_update():
	head_move()
	display_candy()


def change_direction(i):
	# print(i.key)
	global direction
	if i.key in [pygame.K_w,pygame.K_UP] and direction!='d':
		direction='u'
	elif i.key in [pygame.K_s,pygame.K_DOWN] and direction!='u':
		direction='d'
	elif i.key in [pygame.K_a,pygame.K_LEFT] and direction!='r':
		direction='l'
	elif i.key in [pygame.K_d,pygame.K_RIGHT] and direction!='l':
		direction='r'


pygame.init()
pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake @author Vipen Loka")
screen=pygame.display.get_surface()

# pygame.draw.rect(screen,(0,255,255),(200,200,10,10))

grid=False
snake=[[200,200,10,10],[200,200,10,10],[200,200,10,10],[200,200,10,10],[200,200,10,10]]
candy=[randrange(0,480,10),randrange(0,480,10),10,10]
previous_time=0
direction='r'
pause=0
while 1:
	for i in pygame.event.get():
		if i.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if i.type==pygame.KEYDOWN:
			change_direction(i)
			if i.key==pygame.K_p:
				pause^=1

	if not pause and time.time()-previous_time>0.05:
		previous_time=time.time()
		# head_move()
		frame_update()
		


	pygame.display.update()

