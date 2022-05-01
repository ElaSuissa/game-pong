from itertools import count
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
PINK = (253, 57, 72)
# ריבועים
square1_y = WINDOW_H/2
square2_y = WINDOW_H/2
# הכדור
circle_x = WINDOW_W/2
circle_y = WINDOW_H/2
hit = True
limit_y = True
count1 = 0
count2= 0

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("pong")


def is_circle_hit_player1 (circle_x, circle_y,square1_y):
     return abs (circle_x - 10) < 30 and (circle_y - square1_y ) < 30

def is_circle_hit_player2 (circle_y,circle_x, square2_y):
    return (circle_y - square2_y)< 30 and abs ( 800-15 - circle_x)< 30
    

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
    # if square1_y-30 <=0:
    #     square1_y = 0
    # if square1_y+30 >=664:
    #    square1_y = 664
    # if square2_y-30 < 800 and square2_y + 30 > 664:    
    square2_y += 20 * hold_player_2

    if is_circle_hit_player1 (circle_x, circle_y,square1_y):
        hit = True
        print("hit player 1")
        count1 +=1
    if is_circle_hit_player2 (circle_y,circle_x, square2_y):
        hit = False
        print ("hit player 2")
        count2 +=1
    #צעדים של הכדור שהוא פוגע בריבוע וחוזר
    if not hit:
        circle_x -= 10
    elif hit:
        circle_x += 10
       
    
    if circle_y <= 0:
        limit_y = True
    elif circle_y >= WINDOW_H:
        limit_y = False
    
    if limit_y ==True:
        circle_y += 5
    elif limit_y == False:
        circle_y -= 3    
    
    if square1_y - 45  <= 0:
        hold_player_1  = 0
    elif square1_y  + 45 >= WINDOW_H:
        hold_player_1= 0
    
    
    if square2_y - 45 <= 0:
        hold_player_2 = 0
    elif square2_y + 45 >= WINDOW_H:
        hold_player_2 = 0
    
    screen.fill(BLACK)
    
    font = pygame.font.SysFont(None, 50)
    img1 = font.render('score:' + str(count1), True, PINK)
    screen.blit(img1, (130,40 ))
    img2 = font.render('score:' + str(count2), True, PINK)
    screen.blit(img2, (530,40 ))
    
    # if is_circle_hit_player1 (circle_x, circle_y,square1_y):


    
    # מצייר את הקווים,הריבועים והכדור
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (0, WINDOW_H), 5)
    pygame.draw.line(screen, (255, 255, 255),
                     (0, WINDOW_H), (WINDOW_W, WINDOW_H), 5)
    pygame.draw.line(screen, (255, 255, 255),
                     (WINDOW_W, WINDOW_H), (WINDOW_W, 0), 5)
    pygame.draw.line(screen, (255, 255, 255), (WINDOW_W, 0), (0, 0), 5)
    pygame.draw.line(screen, (255, 255, 255), (400, 0), (400, 664), 5)
    pygame.draw.line(screen, (232, 31, 63), (800-15, square2_y+30), (800-15, square2_y-30), 10)
    pygame.draw.line(screen, (232, 31, 63), (10, square1_y+30), (10, square1_y-30), 10)
    pygame.draw.circle(screen, (181, 187, 254), (circle_x, circle_y), 15)
    pygame.display.flip()

    clock.tick(30)

pygame.display.update()
