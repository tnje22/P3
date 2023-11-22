import cv2
import mediapipe as mp
import numpy as np
import time

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pTime = 0
cTime = 0

cap = cv2.VideoCapture("C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv") # This is the path for the training video: "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv"
# setup mediapipe
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # Make detection
        results = pose.process(image)
        
        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        h, w, c = image.shape
        # Extract landmarks
        try:
            landmarks = results.pose_landmarks.landmark
            
            elbowCx = (landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x)*w
            elbowCy = (landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x)*h
            print(elbowCx,elbowCy) 
                    
            #print("Right Elbow: ",landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value], "Right Wrist: ",landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])
        except:
            pass
        
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        
        # cTime = time.time()
        # fps = 1/(cTime-pTime)
        # pTime = cTime
    
        # draws the fps on screen
        # cv2.putText(image, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
        
        cv2.imshow('Mediapipe Feed',image)
        
        if cv2.waitKey(19) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()