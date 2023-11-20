import cv2
import numpy as np

# Function to process the frame and identify new Lego Duplo blocks
def process_frame(frame, background_model, threshold=25):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve accuracy
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Compute the absolute difference between the current frame and the background model
    diff = cv2.absdiff(background_model, gray)

    # Threshold the difference to identify significant changes
    _, thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    # Apply morphological operations to further reduce noise
    kernel = np.ones((5, 5), np.uint8)
    thresholded = cv2.erode(thresholded, kernel, iterations=1)
    thresholded = cv2.dilate(thresholded, kernel, iterations=2)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around identified objects
    for contour in contours:
        if cv2.contourArea(contour) > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame

def main():
    # Open the camera
    cap = cv2.VideoCapture(0)

    # Read the first frame to initialize the background model
    _, background_model = cap.read()
    background_model = cv2.cvtColor(background_model, cv2.COLOR_BGR2GRAY)

    while True:
        # Read the current frame
        _, frame = cap.read()

        # Process the frame to identify new Lego Duplo blocks
        result_frame = process_frame(frame, background_model)

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
