import cv2
import numpy as np

def detect_human_arm(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to reduce noise and help contour detection
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)

        # Use Canny edge detector to find edges in the frame
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours based on area to find the contour of the arm
        arm_contour = max(contours, key=cv2.contourArea)

        # Draw the contour on the original frame
        cv2.drawContours(frame, [arm_contour], -1, (0, 255, 0), 2)

        # Extract the bounding rectangle of the arm
        x, y, w, h = cv2.boundingRect(arm_contour)

        # Define ROIs for the hand, forearm, and upper arm
        hand_roi = frame[y + h//2:, x:x + w]
        forearm_roi = frame[y:y + h//2, x:x + w]
        upper_arm_roi = frame[:y, x:x + w]

        # Draw outlines around hand, forearm, and upper arm in different colors
        cv2.drawContours(frame, [cv2.approxPolyDP(arm_contour, 0.02 * cv2.arcLength(arm_contour, True), True)], 0, (255, 0, 0), 2)
        cv2.drawContours(frame, [cv2.approxPolyDP(arm_contour, 0.02 * cv2.arcLength(arm_contour, True), True)], 0, (0, 255, 0), 2)
        cv2.drawContours(frame, [cv2.approxPolyDP(arm_contour, 0.02 * cv2.arcLength(arm_contour, True), True)], 0, (0, 0, 255), 2)

        # Display the results
        cv2.imshow('Original Frame', frame)
        #cv2.imshow('Hand ROI', hand_roi)
        #cv2.imshow('Forearm ROI', forearm_roi)
        #cv2.imshow('Upper Arm ROI', upper_arm_roi)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object
    cap.release()
    cv2.destroyAllWindows()

# Replace 'your_video_path.mp4' with the path to your video file
video_path = 'C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/%HOMEDRIVE%HOMEPATH%movement1.mkv'
detect_human_arm(video_path)
