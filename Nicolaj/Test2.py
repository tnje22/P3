import cv2
import numpy as np

def detect_hand_in_video(video_file_path):
    # Create a VideoCapture object to capture video from the specified file
    cap = cv2.VideoCapture(video_file_path)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to the grayscale frame
        blurred = cv2.GaussianBlur(gray, (15, 15), 0)

        # Threshold the blurred image to create a binary image
        _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

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

        # Color-based segmentation to filter out the table (white color)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_white = np.array([0, 0, 200])
        upper_white = np.array([180, 25, 255])
        table_mask = cv2.inRange(hsv, lower_white, upper_white)

        # Find contours in the table mask
        table_contours, _ = cv2.findContours(table_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Exclude the table area from the hand contour
        if hand_contour is not None:
            for table_contour in table_contours:
                cv2.drawContours(thresh, [table_contour], 0, (0, 0, 0), -1)  # Draw filled black contour

            # Find the hand contour again after excluding the table
            new_hand_contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            max_area = 0
            for contour in new_hand_contours:
                area = cv2.contourArea(contour)
                if area > max_area:
                    max_area = area
                    hand_contour = contour

        # Draw a bounding box around the hand and calculate the center
        if hand_contour is not None:
            x, y, w, h = cv2.boundingRect(hand_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            center_x = x + w // 2
            center_y = y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

        cv2.imshow("Hand Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Example usage:
video_file_path = "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/%HOMEDRIVE%HOMEPATH%movement1.mkv"
detect_hand_in_video(video_file_path)
