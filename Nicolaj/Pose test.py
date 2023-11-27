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

        # Extract landmarks, if it tracks anything
        try:
            landmarks = results.pose_landmarks.landmark

            WristCx = int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x * image.shape[1])
            WristCy = int(landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y * image.shape[0])

            # Putting the x&y coords in an array
            WristXY = [WristCx, WristCy]

            # Assuming box size is 100x100 pixels
            box_size = (100, 100)

            # Define the region of interest (ROI) based on the box size
            roi = image1[WristXY[1]:WristXY[1] + box_size[1], WristXY[0]:WristXY[0] + box_size[0]]

            # Resize the overlay image to match the box size
            resized_overlay = cv2.resize(roi, (box_size[0], box_size[1]))

            # Create a mask using the alpha channel of the overlay image (if exists)
            mask = resized_overlay[:, :, 3] / 255.0 if resized_overlay.shape[2] == 4 else None

            # Blend the images using the mask
            blended_roi = cv2.addWeighted(roi, 1 - mask, resized_overlay[:, :, :3], mask, 0) if mask is not None else roi

            # Update the frame with the blended ROI
            image[WristXY[1]:WristXY[1] + box_size[1], WristXY[0]:WristXY[0] + box_size[0]] = blended_roi

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
