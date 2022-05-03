from itertools import count
import pygame
import time
from pickle import TRUE

# גודל של המסך
WINDOW_W = 800
WINDOW_H = 664
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# צבע
BLACK = (0, 0, 0)
WHITE = (250, 250, 250)

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

#פונקציות שבודקות אם הכדור פגע במלבן של השחקנים 
def is_circle_hit_player1 (circle_x, circle_y,square1_y):
     return abs (circle_x - 10) < 30 and abs (circle_y - square1_y ) < 30

def is_circle_hit_player2 (circle_y,circle_x, square2_y):
    return abs (circle_y - square2_y)< 30 and abs ( 800-15 - circle_x)< 30
    

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


#בודק אם הכדור פגע במלבן של השחקן הראשון ומוסיף לו נקודה
    if is_circle_hit_player1 (circle_x, circle_y,square1_y):
        hit = True
        print("hit player 1")
        count1 +=1 


 #הבודק אם הכדור פגע במלבן של השחקן השני ומוסיף לו נקודה
    if is_circle_hit_player2 (circle_y,circle_x, square2_y):
        hit = False
        print ("hit player 2")
        count2 +=1


    #החזרה של הכדור כשהוא פוגע בריבוע
    if not hit:
        circle_x -= 10
    elif hit:
        circle_x += 10
       
    #גבולות של הכדור
    if circle_y <= 0:
        limit_y = True
    elif circle_y >= WINDOW_H:
        limit_y = False
    
    if limit_y ==True:
        circle_y += 5
    elif limit_y == False:
        circle_y -= 3    
    
    #גבולות של המרובעים
    if square1_y - 45  <= 0:
        hold_player_1  = 0
    elif square1_y  + 45 >= WINDOW_H:
        hold_player_1= 0
    
    if square2_y - 45 <= 0:
        hold_player_2 = 0
    elif square2_y + 45 >= WINDOW_H:
        hold_player_2 = 0
    

    screen.fill(BLACK)
    
    #הניקוד של שני השחקנים
    font = pygame.font.SysFont(None, 45)
    img1 = font.render('score:' + str(count1), True, WHITE)
    screen.blit(img1, (130,40 ))
    img2 = font.render('score:' + str(count2), True, WHITE)
    screen.blit(img2, (530,40 ))
    


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
