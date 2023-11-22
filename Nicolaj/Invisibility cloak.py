import cv2
import time
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands

hands = mpHands.Hands()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    
    
    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)
    