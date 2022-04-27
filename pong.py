from cv2 import circle
from numpy import square
import pygame
import time
from pickle import TRUE

# גודל של המסך
WINDOW_W = 800
WINDOW_H = 664
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
# צבע
BLACK = (0, 0, 0)
# ריבועים
square1_y = WINDOW_H/2
square2_y = WINDOW_H/2
# הכדור
circle_x = WINDOW_W/2
circle_y = WINDOW_H/2
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("pong")

hold_player_1 = 0
hold_player_2 = 0

clock = pygame.time.Clock()
# הזזה של הריבועים עם המקשים
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hold_player_1 = -1
            elif event.key == pygame.K_s:
                hold_player_1 = 1
            if event.key == pygame.K_UP:
                hold_player_2 = -1
            elif event.key == pygame.K_DOWN:
                hold_player_2 = 1
        elif event.type == pygame.KEYUP:
            hold_player_1 = 0
            hold_player_2 = 0

    square1_y += 20 * hold_player_1
    square2_y += 20 * hold_player_2
    screen.fill(BLACK)
    # מצייר את הקווים,הריבועים והכדור
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (0, WINDOW_H), 5)
    pygame.draw.line(screen, (255, 255, 255),
                     (0, WINDOW_H), (WINDOW_W, WINDOW_H), 5)
    pygame.draw.line(screen, (255, 255, 255),
                     (WINDOW_W, WINDOW_H), (WINDOW_W, 0), 5)
    pygame.draw.line(screen, (255, 255, 255), (WINDOW_W, 0), (0, 0), 5)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 664), 5)
    pygame.draw.line(screen, (232, 31, 63),
                     (800-15, square2_y+30), (800-15, square2_y-30), 10)
    pygame.draw.line(screen, (232, 31, 63),
                     (10, square1_y+30), (10, square1_y-30), 10)
    pygame.draw.circle(screen, (181, 187, 254), (circle_x, circle_y), 15)
    pygame.display.flip()

    clock.tick(15)

pygame.display.update()