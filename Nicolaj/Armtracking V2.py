import cv2
import numpy as np

def calculate_centroid(contour, offset):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"]) + offset[0]
        cy = int(M["m01"] / M["m00"]) + offset[1]
        return cx, cy
    else:
        return None

def crop_roi(frame, x, y, w, h):
    return frame[y:y + h, x:x + w]

def detect_human_arm(video_path, roi):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break

        # Create a mask for the ROI
        mask = np.zeros_like(frame)
        x, y, w, h = roi
        mask[y:y + h, x:x + w] = frame[y:y + h, x:x + w]

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the skin color in HSV
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 50, 255], dtype=np.uint8)

        # Create a binary mask for the skin color
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Apply GaussianBlur to reduce noise
        blurred = cv2.GaussianBlur(mask, (15, 15), 0)

        # Use Canny edge detector to find edges in the frame
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw contours on the original frame within the specified ROI
        for contour in contours:
            # Filter contours based on area to find the contour of the arm
            if cv2.contourArea(contour) > 1000:  # Adjust the area threshold as needed
                # Draw contours on the original frame
                cv2.drawContours(frame[y:y + h, x:x + w], [contour], -1, (0, 255, 0), 2)

                # Calculate centroid of the hand contour
                centroid = calculate_centroid(contour, (x, y))

                if centroid is not None:
                    cx, cy = centroid
                    cv2.circle(frame[y:y + h, x:x + w], (cx, cy), 5, (255, 0, 0), -1)  # Draw a blue circle at the centroid

        # Display the results
        cv2.imshow('Video Feed', frame)
        cv2.imshow('Masked ROI with Contours', mask)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file
    cap.release()
    cv2.destroyAllWindows()

# Specify the path to your video file and the ROI (x, y, width, height)
video_path = "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv"
roi = (470, 100, 1100, 700)  # Example ROI, adjust as needed

# Call the function to start the video feed with the specified ROI
detect_human_arm(video_path, roi)
