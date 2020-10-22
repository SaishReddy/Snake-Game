import pygame
import sys
import time
from random import randrange

score = 0


def reset_screen():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 500, 500))
    if grid:
        draw_grid()


def draw_grid():
    for j in range(0, 500, 10):
        pygame.draw.line(screen, (255, 255, 255), (j, 0), (j, 500))

    for j in range(0, 500, 10):
        pygame.draw.line(screen, (255, 255, 255), (0, j), (500, j))


def head_move():
    global score, candy
    reset_screen()
    tail_move()
    if direction == 'd':
        snake[0][1] += 10

    elif direction == 'u':
        snake[0][1] -= 10

    elif direction == 'r':
        snake[0][0] += 10

    elif direction == 'l':
        snake[0][0] -= 10

    snake[0][0] %= 500
    snake[0][1] %= 500
    # print(snake[0][:2],candy[:2])
    if snake[0][:2] == candy[:2]:
        score += 1
        snake.append([0, 0, 10, 10])
        candy = [randrange(0, 480, 10), randrange(0, 480, 10), 10, 10]
    for j in range(len(snake)):
        pygame.draw.rect(screen, (0, 255, 255), snake[j])


def tail_move():
    for j in range(len(snake) - 1, 0, -1):
        snake[j][0] = snake[j - 1][0]
        snake[j][1] = snake[j - 1][1]


def display_candy():
    pygame.draw.rect(screen, (254, 127, 156), candy)


def frame_update():
    head_move()
    display_candy()
    display_score(pause == 1)  # Score function gets called.


def change_direction(j):
    # print(i.key)
    global direction
    if j.key in [pygame.K_w, pygame.K_UP] and direction != 'd':
        direction = 'u'
    elif j.key in [pygame.K_s, pygame.K_DOWN] and direction != 'u':
        direction = 'd'
    elif j.key in [pygame.K_a, pygame.K_LEFT] and direction != 'r':
        direction = 'l'
    elif j.key in [pygame.K_d, pygame.K_RIGHT] and direction != 'l':
        direction = 'r'


# fn for text
def text_objects(text, fonts):
    text_surface = fonts.render(text, True, (255, 255, 255))
    return text_surface, text_surface.get_rect()


def display_score(paused=False):
    """
    A function to display score: [int].
    :param paused: If the game is paused the text "Score" is visible along with number
    :return: a surface displaying score upon the main surface.
    """
    score_text = pygame.font.SysFont('comicsansms', size=20)
    # score_surf, score_rect = text_objects(text="Score:{}".format(score), fonts=score_text)
    if not paused:
        score_surf, score_rect = text_objects(text="{}".format(score), fonts=score_text)
        score_rect.center = (500 - 10, 10)
    else:
        score_surf, score_rect = text_objects(text="Score:{}".format(score), fonts=score_text)
        score_rect.center = (500 - 40, 10)
    screen.blit(score_surf, score_rect)


pygame.init()
pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
screen = pygame.display.get_surface()

# pygame.draw.rect(screen,(0,255,255),(200,200,10,10))

grid = False
snake = [[200, 200, 10, 10], [200, 200, 10, 10], [200, 200, 10, 10], [200, 200, 10, 10], [200, 200, 10, 10]]
candy = [randrange(0, 480, 10), randrange(0, 480, 10), 10, 10]
previous_time = 0
direction = 'r'
pause = 0
while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            change_direction(i)
            if i.key == pygame.K_p:
                pause ^= 1
                pause_text = pygame.font.SysFont(name="comicsansms", size=27)  # Font name, size
                text_surf, text_rect = text_objects(text="Paused", fonts=pause_text)  # Text, font
                text_rect.center = (46, 20)  # Defining the centre of text rectangle
                screen.blit(text_surf, text_rect)  # Overlap the rectangle surface on the the screen at a position.

    if not pause and time.time() - previous_time > 0.05:
        previous_time = time.time()
        # head_move()
        frame_update()

    pygame.display.update()
