import cv2
import numpy as np

# Create a VideoCapture object to capture video from your webcam
cap = cv2.VideoCapture(0)

hand_position = (0, 0)  # Initialize hand_position to (0, 0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to the grayscale frame
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    # Threshold the blurred image to create a binary image
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Filter the contours to find the hand contour
    hand_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            hand_contour = contour

    # Draw a bounding box around the hand and calculate the center
    if hand_contour is not None:
        x, y, w, h = cv2.boundingRect(hand_contour)
        if w * h > 5000:  # Filter out smaller contours (adjust this value as needed)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Calculate the center point
            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

        # Update the hand_position variable
            hand_position = (center_x, center_y)

    # Display the frame
    cv2.imshow("Hand Detection", frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

# Print the final hand position
print("Final hand position:", hand_position)
