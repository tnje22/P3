import cv2
import mediapipe as mp
import numpy as np
import time
import subprocess

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pTime = 0
cTime = 0

cap = cv2.VideoCapture(0) # This is the path for the training video: "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv"
# setup mediapipe
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Path and process for mask image
        image_path = 'Nicolaj/Images/1920x1080-black-solid-color-background.jpg'
        image1 = cv2.imread(image_path)
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
              
        # Make detection
        results = pose.process(image)
        
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # Defining the shape and dimentions of the image
        h, w, c = image.shape
        
        # Extract landmarks, if it tracks anything
        try:
            landmarks = results.pose_landmarks.landmark
            
            # Translating the default coords form mediapipe to coords that relate to the image
            elbowCx = (landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x)*w
            elbowCy = (landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x)*h
            WristCx = (landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x)*w
            WristCy = (landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y)*h
            
            # Putting the x&y coords in two arrays so you can just call on them
            WristXY = [WristCx, WristCy]
            ElbowXY = [elbowCx, elbowCy]
            
            ElBow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            WrIst = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            Pinky = [landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].x, landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].y]
            IndexKn = [landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x, landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y]              
            
            
            #cv2.circle(image, tuple(np.multiply(ElBow, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            #cv2.circle(image, tuple(np.multiply(WrIst, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            
            #cv2.rectangle(image, tuple(np.multiply(ElBow, [1920, 1080]).astype(int)), tuple(np.multiply(WrIst, [1920, 1080]).astype(int)), (255, 255, 255), cv2.FILLED)
            
            #cv2.circle(image, tuple(np.multiply(Pinky, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            #cv2.circle(image, tuple(np.multiply(IndexKn, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            
        except:
            pass
        
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        #cv2.circle(image1, tuple(np.multiply(ElBow, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
        #cv2.circle(image1, tuple(np.multiply(WrIst, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
        
        # Displays the image
        cv2.imshow('Mediapipe Feed',image)
        
        #cv2.imshow("test frame", image1)
        
        # This checks if the q key is preds, and closes if it is.
        if cv2.waitKey(19) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    