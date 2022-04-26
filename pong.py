from pickle import TRUE
import pygame
# screen size 
WINDOW_W = 800
WINDOW_H = 664
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("pong")

#pygame.draw.line(screen, (20,20,20), (60, 80), (130, 100), 100)
RED=(255,0,0)
size = (50, 50)
points = [(25, 0), (50, 25), (25, 50), (0, 25)]

lines = pygame.Surface(size)
pygame.draw.lines(lines, RED, False, points)

lines_closed = pygame.Surface(size)
pygame.draw.lines(lines_closed, RED, True, points)

play = True
while play:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        play = False
    
    
    