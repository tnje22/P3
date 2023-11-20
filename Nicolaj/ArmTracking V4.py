import cv2
import numpy as np

def calculate_centroid(contour, offset):
    M = cv2.moments(contour)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"]) + offset[0]
        cy = int(M["m01"] / M["m00"]) + offset[1]
        return cx, cy
    else:
        return None

def crop_roi(frame, x, y, w, h):
    return frame[y:y + h, x:x + w]

def group_contours(contours, threshold_area):
    grouped_contours = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > threshold_area:
            grouped_contours.append(contour)

    return grouped_contours

def create_black_square(frame, region):
    x, y, w, h = region
    frame[y:y+h, x:x+w] = 0  # Set the specified region to black

def detect_human_arm(video_path, roi, square_region, threshold_area=375):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break

        # Create a mask for the ROI
        mask = np.zeros_like(frame)
        x, y, w, h = roi
        mask[y:y + h, x:x + w] = frame[y:y + h, x:x + w]

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)

        # Define the lower and upper bounds for the skin color in HSV
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 50, 255], dtype=np.uint8)

        # Create a binary mask for the skin color
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # Apply GaussianBlur to reduce noise
        blurred = cv2.GaussianBlur(mask, (15, 15), 0)

        # Use Canny edge detector to find edges in the frame
        edges = cv2.Canny(blurred, 50, 150)

        # Find contours in the edges with a higher hierarchy level
        contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Group contours based on area
        grouped_contours = group_contours(contours, threshold_area)

        # Check if grouped contours were found
        if grouped_contours:
            # Combine all grouped contours into a single blob
            all_contours = np.vstack(grouped_contours)

            # Find the bounding rectangle that encloses all grouped contours
            x, y, w, h = cv2.boundingRect(all_contours)

            # Draw the rectangle around the combined blob
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Choose one contour (e.g., the largest) for further processing
            main_contour = all_contours

            # Draw the contour on the original frame
            cv2.drawContours(frame, [main_contour], -1, (255, 0, 0), 2)

            # Calculate centroid of the hand contour
            centroid = calculate_centroid(main_contour, (roi[0], roi[1]))

            if centroid is not None:
                cx, cy = centroid
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)  # Draw a blue circle at the centroid

                # Print the position of the combined blob
                print("Blob Position:", (cx, cy))

        # Create a black square in the specified region
        create_black_square(frame, square_region)

        # Display the results
        cv2.imshow('Video Feed', frame)
        cv2.imshow('Masked ROI', mask)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file
    cap.release()
    cv2.destroyAllWindows()

# Specify the path to your video file, the ROI (x, y, width, height), and the square region (x, y, width, height)
video_path = "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv"
roi = (470, 100, 1100, 700)  # Example ROI, adjust as needed
square_region = (500, 300, 500, 500)  # Example square region, adjust as needed

# Call the function to start the video feed with the specified ROI and square region
detect_human_arm(video_path, roi, square_region)
