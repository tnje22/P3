import cv2
import numpy as np

# Function to remove a white background
def remove_white_background(frame):
    lower_white = np.array([200, 200, 200])
    upper_white = np.array([255, 255, 255])
    mask = cv2.inRange(frame, lower_white, upper_white)
    result = cv2.bitwise_and(frame, frame, mask=~mask)
    return result

# Function to detect the human hand
def detect_hand(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        hand_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(hand_contour)
        return x, y, w, h
    else:
        return None

# Function to filter skin color
def filter_skin_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_skin = np.array([0, 20, 70], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    skin_mask = cv2.inRange(hsv, lower_skin, upper_skin)
    filtered_frame = cv2.bitwise_and(frame, frame, mask=skin_mask)

    return filtered_frame

# Main function
def main():
    video_capture = cv2.VideoCapture('C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/%HOMEDRIVE%HOMEPATH%movement1.mkv')

    while video_capture.isOpened():
        ret, frame = video_capture.read()

        if not ret:
            break

        frame = remove_white_background(frame)
        filtered_frame = filter_skin_color(frame)
        hand_coords = detect_hand(filtered_frame)

        if hand_coords:
            x, y, w, h = hand_coords

            # Draw bounding box and center dot
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            center_x, center_y = x + w // 2, y + h // 2
            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

            # Print coordinates
            print(f"Hand coordinates: ({center_x}, {center_y})")

        cv2.imshow('Hand Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ != "__main":
    main()
