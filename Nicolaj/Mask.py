import cv2
import numpy as np
import mediapipe as mp
import time
import Pose_Tracking

image_path = 'Nicolaj/Images/1920x1080-black-solid-color-background.jpg'
image1 = cv2.imread(image_path)

new_Elbow = Pose_Tracking.ElBow
new_Wrist = Pose_Tracking.WrIst

print("Elbow x/y ", new_Elbow, "Wrist x/y ", new_Wrist)
#cv2.imshow("test frame", image1)
#cv2.waitKey(0)