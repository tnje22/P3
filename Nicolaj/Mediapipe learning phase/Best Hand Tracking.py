
#RUN this to get the mediapipe: pip install mediapipe

import cv2
import time
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0) #This is the path for the training video: "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv"
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 0:
                    cv2.circle(img, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    #draws the fps on screen
    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
    
    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
    