import cv2
import mediapipe as mp
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pTime = 0
cTime = 0

cap = cv2.VideoCapture("C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv")

# setup mediapipe
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()

        # Path and process for mask image
        image_path = 'Nicolaj/Images/Nicolaj\Images\1920x1080-black-solid-color-background.jpg'
        image1 = cv2.imread(image_path)

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Extract landmarks, if it tracks anything
        try:
            landmarks = results.pose_landmarks.landmark

            WristCx = int(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x * image.shape[1])
            WristCy = int(landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y * image.shape[0])
            ElbowCx = int(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x * image.shape[1])
            ElbowCy = int(landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y * image.shape[0])

            # Putting the x&y coords in arrays
            WristXY = [WristCx, WristCy]
            ElbowXY = [ElbowCx, ElbowCy]

            # Assuming box size is 100x100 pixels
            box_size = (100, 100)

            # Calculate the starting point for the region of interest (ROI) for WristXY
            wrist_roi_start_x = max(0, WristXY[0] - box_size[0] // 2)
            wrist_roi_start_y = max(0, WristXY[1] - box_size[1] // 2)

            # Define the region of interest (ROI) for WristXY based on the box size
            wrist_roi = image1[wrist_roi_start_y:wrist_roi_start_y + box_size[1], wrist_roi_start_x:wrist_roi_start_x + box_size[0]]

            # Resize the overlay image to match the box size
            resized_wrist_overlay = cv2.resize(wrist_roi, (box_size[0], box_size[1]))

            # Create a mask using the alpha channel of the overlay image (if exists)
            wrist_mask = resized_wrist_overlay[:, :, 3] / 255.0 if resized_wrist_overlay.shape[2] == 4 else None

            # Blend the images using the mask for WristXY
            blended_wrist_roi = cv2.addWeighted(wrist_roi, 1 - wrist_mask, resized_wrist_overlay[:, :, :3], wrist_mask, 0) if wrist_mask is not None else wrist_roi

            # Update the frame with the blended ROI for WristXY
            image[wrist_roi_start_y:wrist_roi_start_y + box_size[1], wrist_roi_start_x:wrist_roi_start_x + box_size[0]] = blended_wrist_roi

            # Calculate the starting point for the region of interest (ROI) for ElbowXY
            elbow_roi_start_x = max(0, ElbowXY[0] - box_size[0] // 2)
            elbow_roi_start_y = max(0, ElbowXY[1] - box_size[1] // 2)

            # Define the region of interest (ROI) for ElbowXY based on the box size
            elbow_roi = image1[elbow_roi_start_y:elbow_roi_start_y + box_size[1], elbow_roi_start_x:elbow_roi_start_x + box_size[0]]

            # Resize the overlay image to match the box size
            resized_elbow_overlay = cv2.resize(elbow_roi, (box_size[0], box_size[1]))

            # Create a mask using the alpha channel of the overlay image (if exists)
            elbow_mask = resized_elbow_overlay[:, :, 3] / 255.0 if resized_elbow_overlay.shape[2] == 4 else None

            # Blend the images using the mask for ElbowXY
            blended_elbow_roi = cv2.addWeighted(elbow_roi, 1 - elbow_mask, resized_elbow_overlay[:, :, :3], elbow_mask, 0) if elbow_mask is not None else elbow_roi

            # Update the frame with the blended ROI for ElbowXY
            image[elbow_roi_start_y:elbow_roi_start_y + box_size[1], elbow_roi_start_x:elbow_roi_start_x + box_size[0]] = blended_elbow_roi

        except:
            pass

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Displays the image
        cv2.imshow('Mediapipe Feed', image)

        # This checks if the q key is pressed and closes if it is.
        if cv2.waitKey(19) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
