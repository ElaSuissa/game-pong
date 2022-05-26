A = []
A[0] = 3
print("aaa")


import cv2
import mediapipe as mp

# define a video capture object
vid = cv2.VideoCapture(0)

mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils

index_finger_y_player1 = 0
index_finger_y_player2 = 0

index_finger5_y_player2= 0
index_finger8_y_player2 =0 

while(True):
	# Capture the video frame
	# by frame
    ret, frame = vid.read()
    index_finger_x = 0

    RGB_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	
    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks
    
    if multiLandMarks and len(multiLandMarks)==2:
        # go over all hands found and draw them on the BGR image
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(frame, handLms, mp_Hands.HAND_CONNECTIONS)
            # the location of the index finger tip is number 8 in the landmarks
            index_finger_y = multiLandMarks[0].landmark[8].y
            index_finger_y1 = multiLandMarks[0].landmark[5].y
            
            index_finger8_y_player2 = multiLandMarks[1].landmark[8].y
            index_finger5_y_player2 = multiLandMarks[1].landmark[5].y
    
        if index_finger_y < index_finger_y1:
            print ("finger1 = up")
        else:
            print ("finger1 =down")
         
        if index_finger5_y_player2 < index_finger8_y_player2:
            print ("finger2 = up")
        else:
             print ("finger2 =down")
    
    # Display the resulting frame
    # font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    # org
    org = (50, 50)
    
    # fontScale
    fontScale = 1
    
    # Blue color in BGR
    color = (255, 0, 0)
    
    # Line thickness of 2 px
    thickness = 2
    
    # Using cv2.putText() method
    # frame = cv2.putText(frame, "y=%.2f" % index_finger_y, org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow('frame', frame)
	
    

	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
