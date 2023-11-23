import cv2
import numpy as np
import mediapipe as mp
import time
from Pose_Tracking import WristXY, ElbowXY

image_path = 'test.png'
image1 = cv2.imread(image_path)

while True:
 print(WristXY, ElbowXY)