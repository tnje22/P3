import cv2
import numpy as np
#path to video data
video_path = "C:/Users/tnj70/Desktop/Data/building_1.mkv"

# Function to process the frame and identify new Lego Duplo blocks
def process_frame(frame, background_model, roi, threshold=25):
    # Extract the region of interest (ROI) from the frame
    x, y, w, h = roi
    roi_frame = frame[y:y+h, x:x+w]

    # Ensure the ROI frame has the same size as the background model
    roi_frame = cv2.resize(roi_frame, (background_model.shape[1], background_model.shape[0]))

    # Convert the ROI frame to grayscale
    gray = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve accuracy
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute the absolute difference between the current frame and the background model
    diff = cv2.absdiff(background_model, gray)

    # Threshold the difference to identify significant changes
    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Apply morphological operations to further reduce noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around identified objects
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x_roi, y_roi, w_roi, h_roi = cv2.boundingRect(contour)
            # Convert coordinates to global frame
            x_roi_global, y_roi_global = x + x_roi, y + y_roi
            
            cv2.rectangle(frame,(x_roi_global, y_roi_global), (x_roi_global + w_roi, y_roi_global + h_roi), (0, 255, 0), 2)

    return frame



def main():
    # Open the camera
    cap = cv2.VideoCapture(video_path)

    # Read the first frame to initialize the background model
    _, background_model = cap.read()
    background_model = cv2.cvtColor(background_model, cv2.COLOR_BGR2GRAY)

    # Define the region of interest (x, y, width, height)
    roi = (1150, 400, 50, 50)

    while True:
        # Read the current frame
        _, frame = cap.read()

        # Process the frame within the specified ROI
        result_frame = process_frame(frame, background_model, roi)

        # Display the result
        cv2.imshow('Lego Duplo Detection', result_frame)

        # Update the background model for the next iteration
        background_model = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
