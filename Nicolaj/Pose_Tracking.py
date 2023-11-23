import cv2
import mediapipe as mp
import numpy as np
import time
import subprocess


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
            
            
            
            # Printing the x&y for the left elbow and wrist
            #print("Left wrist ",WristXY,"Left elbow", ElbowXY)                
            
            
            cv2.circle(image, tuple(np.multiply(ElBow, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            cv2.circle(image, tuple(np.multiply(WrIst, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            
            cv2.rectangle(image, tuple(np.multiply(ElBow, [1920, 1080]).astype(int)), tuple(np.multiply(WrIst, [1920, 1080]).astype(int)), (255, 255, 255), cv2.FILLED)
            
            cv2.circle(image, tuple(np.multiply(Pinky, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            cv2.circle(image, tuple(np.multiply(IndexKn, [1920, 1080]).astype(int)), 50, (255, 255, 255), cv2.FILLED)
            
            
            # Mabye not needed        
            #print("Right Elbow: ",landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value], "Right Wrist: ",landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value])
        except:
            pass
        
        
        
        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        
        # Setup the fps by using the time finction
        # cTime = time.time()
        # fps = 1/(cTime-pTime)
        # pTime = cTime
    
        # draws the fps on screen
        # cv2.putText(image, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3)
       
        
        
        
        # Displays the image
        subprocess.call("Nicolaj\Pose_Tracking.py", shell = True)
        cv2.imshow('Mediapipe Feed',image)
        
        # This checks if the q key is preds, and closes if it is.
        if cv2.waitKey(19) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()