import cv2
import numpy as np


# Load the YOLO model for hand detection
yolo_net = cv2.dnn.readNet("Nicolaj/yolov3-tiny.weights", "Nicolaj/yolov3-tiny.cfg")

# Set the confidence threshold
confidence_threshold = 0.4

# Open the video file
cap = cv2.VideoCapture("C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/%HOMEDRIVE%HOMEPATH%movement1.mkv")

# Define custom cropping coordinates
x_custom = 100  # Top-left corner x-coordinate
y_custom = 150  # Top-left corner y-coordinate
w_custom = 200  # Width of the cropped area
h_custom = 200  # Height of the cropped area

# Initialize cropped_frame outside the loop
cropped_frame = None


while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Get the height and width of the frame
    height, width = frame.shape[:2]

    # Prepare the frame for YOLO detection
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    yolo_net.setInput(blob)
    outs = yolo_net.forward(yolo_net.getUnconnectedOutLayersNames())

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            if confidence > confidence_threshold and class_id == 0:  # 0 corresponds to the "hand" class
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

               # Crop the frame using the custom coordinates
                cropped_frame = frame[y_custom:y_custom + h_custom, x_custom:x_custom + w_custom]

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                print(f"Hand detected at (x, y): ({x + w / 2}, {y + h / 2})")

    cv2.imshow("Hand Detection", frame)
    if cropped_frame is not None:
        cv2.imshow("Cropped Hand", cropped_frame)  # Display the cropped framee

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()