from itertools import count
from cv2 import circle, imshow
from numpy import square
import pygame
import time
from pickle import TRUE
import cv2
import mediapipe as mp

#לאיזה מצלמה המחשב מתחבר
vid = cv2.VideoCapture(0)

#מאתחל את המערכת של זיהוי היידים
mp_Hands = mp.solutions.hands
#קולט יידים, מספר מקסימום ורמת ביטחון 
hands = mp_Hands.Hands(max_num_hands=1,min_detection_confidence=0.7)
#מצייר את הנקודות על היידים
mpDraw = mp.solutions.drawing_utils


index_finger_y_player1 = 0

# גודל של המסך
WINDOW_W = 800
WINDOW_H = 664
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

# צבע
WHITE = (255, 255, 225)
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


#פונקציות שבודקות אם הכדור פגע במלבן של השחקנים 
def is_circle_hit_player1 (circle_x, circle_y,square1_y):
    return abs (circle_x - 10) < 30 and (circle_y - square1_y ) < 30


def is_circle_hit_player2 (circle_y,circle_x, square2_y):
    return abs (circle_y - square2_y)< 30 and abs ( 800-15 - circle_x)< 30

#פונקציה שבודקת אם הכדור יצא מהמשחק והשחקן הפסיד
def if_lose (circle_x):
    return (circle_x > WINDOW_W) or (circle_x < 0)

hold_player_1 = 0
hold_player_2 = 0


LOSE_IMAGE = pygame.image.load("lose pic.png")


clock = pygame.time.Clock()

# הזזה של הריבועים עם המקשים
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                hold_player_2 = -1
            elif event.key == pygame.K_DOWN:
                hold_player_2 = 1
        elif event.type == pygame.KEYUP:
            hold_player_1 = 0
            hold_player_2 = 0  
    square1_y += 20 * hold_player_1   


#קורא את התמונה 
    ret, frame = vid.read()
    max_num_hands=1
    
    #משנה מ BGR לRGB
    RGB_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#מחפש ידיים בתמונה
    results = hands.process(RGB_image)
    # לוקח רשימה של הפרטים על הידיים שהוא מצא
    multiLandMarks = results.multi_hand_landmarks
    
    
    # אם הוא מוצא ידיים, הוא עובר על היידים ומצייר אותם 
    if multiLandMarks and len(multiLandMarks)==1:
        # for handLms in multiLandMarks:
         # mpDraw.draw_landmarks(frame, handLms, mp_Hands.HAND_CONNECTIONS)

 #מיקום הנקודות שעל היד
        index_finger8_y_player2 = multiLandMarks[0].landmark[8].y
        index_finger5_y_player2 = multiLandMarks[0].landmark[5].y
        index_finger12_y_player2 = multiLandMarks[0].landmark[12].y
        index_finger9_y_player2 = multiLandMarks[0].landmark[9].y
        
 
    
        hold_player_1 = 0
        hold_player_2 = 0
        
    #אם האצבע מורמת אז הריבוע עולה למעלה ואם יש שתי אצבעות מורמות אז הואר עוצר במקום
        if (index_finger8_y_player2 < index_finger5_y_player2) and square2_y >= 30 and (index_finger12_y_player2 > index_finger9_y_player2):
            # print ("finger1 =up")
            # hold_player_2 = -1
            square2_y -= 10
            
        if (index_finger8_y_player2 > index_finger5_y_player2) and square2_y <= WINDOW_H -30 and (index_finger12_y_player2 > index_finger9_y_player2):
            # print ("finger1 = down")
            # hold_player_2 = 1
            square2_y += 10
        
        
        

#בודק אם הכדור פגע במלבן של השחקן הראשון ומוסיף לו נקודה
    if is_circle_hit_player1 (circle_x, circle_y,square1_y):
        hit = True
        print("hit player 1")
        count1 +=1



 #בודק אם הכדור פגע במלבן של השחקן השני ומוסיף לו נקודה
    if is_circle_hit_player2 (circle_y,circle_x, square2_y):
        hit = False
        print ("hit player 2")
        count2 +=1
    


    # (מהירות הכדור) החזרה של הכדור כשהוא פוגע בריבוע
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
        square1_y +=5
    elif limit_y == False:
        circle_y -= 3
        square1_y -= 3    


    if square2_y - 45 <= 0:
        hold_player_2 = 0
    elif square2_y + 45 >= WINDOW_H:
        hold_player_2 = 0

        
    screen.fill(WHITE)

    #מציג תמונה של "הפסדת" אחרי שהפונקציה בדקה שהפסדת 
    if if_lose (circle_x):
        screen.blit(LOSE_IMAGE, (160,200))
                
    #  מצייר את הקווים במסגרת ובאמצע
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, WINDOW_H), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, WINDOW_H), (WINDOW_W, WINDOW_H), 5)
    pygame.draw.line(screen, (0, 0, 0), (WINDOW_W, WINDOW_H), (WINDOW_W, 0), 5)
    pygame.draw.line(screen, (0, 0, 0), (WINDOW_W, 0), (0, 0), 5)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 664), 5)
    
    # מצייר את הריבועים של השחקנים
    pygame.draw.line(screen, (PINK), (800-15, square2_y+30), (800-15, square2_y-30), 10)
    pygame.draw.line(screen, (PINK), (10, square1_y+30), (10, square1_y-30), 10)
    
    # מצייר את הכדור
    pygame.draw.circle(screen, (PINK), (circle_x, circle_y), 15)
    
    font = pygame.font.SysFont(None, 50)
    
    #ניקוד
    img = font.render('score:' + str(count2), True, PINK) 
    screen.blit(img, (350,50 ))
    pygame.display.flip()
    clock.tick(253)
pygame.display.update()