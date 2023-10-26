import cv2
import numpy as np

def detect_hand_in_roi(video_file_path, roi):
    cap = cv2.VideoCapture(video_file_path)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        # Crop the frame to the specified region of interest (ROI)
        x, y, w, h = roi
        frame_roi = frame[y:y+h, x:x+w]

        # Convert the ROI to the HSV color space
        hsv = cv2.cvtColor(frame_roi, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the skin color (adjust as needed)
        lower_skin = np.array([0, 20, 70])
        upper_skin = np.array([20, 255, 255])

        # Create a mask to threshold the ROI based on the skin color
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Bitwise AND to apply the mask to the ROI
        hand = cv2.bitwise_and(frame_roi, frame_roi, mask=mask)

        # Convert the hand region to grayscale
        gray_hand = cv2.cvtColor(hand, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale hand region
        blurred = cv2.GaussianBlur(gray_hand, (15, 15), 0)

        # Apply adaptive thresholding to create a binary image for hand detection
        thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

        # Find contours in the binary image for hand detection
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
            x_hand, y_hand, w_hand, h_hand = cv2.boundingRect(hand_contour)
            cv2.rectangle(frame_roi, (x_hand, y_hand), (x_hand + w_hand, y_hand + h_hand), (0, 255, 0), 2)

            center_x = x_hand + w_hand // 2
            center_y = y_hand + h_hand // 2
            cv2.circle(frame_roi, (center_x, center_y), 5, (0, 0, 255), -1)

        # Display the frame with the ROI
        cv2.imshow("Hand Detection", frame_roi)
        cv2.imshow("Binary Image", thresh)
        cv2.imshow("Video", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage:
video_file_path = "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/%HOMEDRIVE%HOMEPATH%movement1.mkv"
roi = (200, 200, 1000, 600)  # Adjust this to specify your desired ROI
detect_hand_in_roi(video_file_path, roi)
