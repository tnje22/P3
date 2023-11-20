import cv2
import numpy as np

def calculate_centroid(contour):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        return cx, cy
    else:
        return None

def detect_human_arm():
    # Open the webcam
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the skin color in HSV
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)

        # Create a binary mask for the skin color
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Apply GaussianBlur to reduce noise
        blurred = cv2.GaussianBlur(mask, (15, 15), 0)

        # Use Canny edge detector to find edges in the frame
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Check if contours were found
        if contours:
            # Filter contours based on area to find the contour of the arm
            arm_contour = max(contours, key=cv2.contourArea)

            # Draw the contour on the original frame
            cv2.drawContours(frame, [arm_contour], -1, (0, 255, 0), 2)

            # Draw the contour on the original frame
            cv2.drawContours(frame, [arm_contour], -1, (0, 255, 0), 2)

            # Calculate centroid of the hand contour
            centroid = calculate_centroid(arm_contour)

            if centroid is not None:
                cx, cy = centroid
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)  # Draw a blue circle at the centroid
            
            # Extract the bounding rectangle of the arm
            x, y, w, h = cv2.boundingRect(arm_contour)

            # Define ROIs for the hand, forearm, and upper arm
            hand_roi = frame[y + h//2:, x:x + w]
            forearm_roi = frame[y:y + h//2, x:x + w]
            upper_arm_roi = frame[:y, x:x + w]

            # Draw outlines around hand, forearm, and upper arm in different colors
            cv2.drawContours(frame, [cv2.approxPolyDP(arm_contour, 0.02 * cv2.arcLength(arm_contour, True), True)], 0, (0, 255, 0), 2)
            cv2.drawContours(frame, [cv2.approxPolyDP(arm_contour, 0.02 * cv2.arcLength(arm_contour, True), True)], 0, (0, 255, 0), 2)
            cv2.drawContours(frame, [cv2.approxPolyDP(arm_contour, 0.02 * cv2.arcLength(arm_contour, True), True)], 0, (0, 255, 0), 2)

        # Display the results
        cv2.imshow('Webcam Feed', frame)
        #cv2.imshow('Hand ROI', hand_roi)
        #cv2.imshow('Forearm ROI', forearm_roi)
        #cv2.imshow('Upper Arm ROI', upper_arm_roi)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam
    cap.release()
    cv2.destroyAllWindows()

# Call the function to start the webcam feed
detect_human_arm()
