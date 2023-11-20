import cv2
import numpy as np

# Define the region of interest (ROI) in the video frame where the Lego Duplo construction is happening
roi_x, roi_y, roi_width, roi_height = 1150, 400, 300, 300

# Initialize the video capture
video_capture = cv2.VideoCapture('C:/Users/tnj70/Desktop/Data/building_1.mkv')  # Replace 'your_video.mp4' with the actual video file


while True:
    # Read a frame from the video
    ret, frame = video_capture.read()

    if not ret:
        break  # Break the loop if the video is finished

    # Extract the region of interest (ROI)
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    # Convert the ROI to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur to reduce noise
    blurred_roi = cv2.GaussianBlur(gray_roi, (5, 5), 0)

    # Perform edge detection using the Canny edge detector
    edges = cv2.Canny(blurred_roi, 50, 150)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area to get the contour of the last-placed Lego Duplo brick
    filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > 100]

    # Draw a rectangle around the last-placed Lego Duplo brick in the original frame
    for contour in filtered_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x + roi_x, y + roi_y), (x + w + roi_x, y + h + roi_y), (0, 255, 0), 2)


    # Display the original frame with the rectangle around the last-placed Lego Duplo brick
    cv2.imshow('Processed Video', frame)
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects
video_capture.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
