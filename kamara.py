import cv2
import cv2

# Function to detect object in the camera feed using OpenCV
def detect_object(frame):
    # Your object detection code here
    # This can involve techniques like color thresholding, contour detection, or deep learning-based methods
    # Return the coordinates (x, y) of the detected object
    object_x, object_y = 320, 240  # Example coordinates (center of the frame)
    return object_x, object_y

# Main function
def main():
    # Initialize the camera (assuming camera index 0, adjust if necessary)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame from the camera
        ret, frame = cap.read()

        # Detect object in the frame
        object_x, object_y = detect_object(frame)

        # Print object coordinates in the camera frame
        print("Object Coordinates in Camera Frame: X={}, Y={}".format(object_x, object_y))

        # Display the frame with the detected object
        cv2.imshow('Object Detection', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()