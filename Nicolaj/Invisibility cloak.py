import cv2
import time
import numpy as np
import mediapipe as mp

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    
    cv2.imshow("Hand Tracking", img)
    cv2.waitKey(1)
    