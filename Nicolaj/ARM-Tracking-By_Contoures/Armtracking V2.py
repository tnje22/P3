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

def detect_human_arm(video_path, roi, threshold_area=375):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Variable to store x and y positions of grouped contours
    grouped_contours_positions = []

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

        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Group contours based on area
        grouped_contours = group_contours(contours, threshold_area)

        # Check if grouped contours were found
        if grouped_contours:
            # Find the bounding rectangle that encloses all grouped contours
            x, y, w, h = cv2.boundingRect(np.vstack(grouped_contours))
            
            # Draw the rectangle around all the grouped contours
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Draw rectangles around each grouped contour
            for contour in grouped_contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Store x and y positions of each grouped contour
                grouped_contours_positions.append((x, y))

            # Choose one contour (e.g., the largest) for further processing
            main_contour = np.vstack(grouped_contours)

            # Draw the contour on the original frame
            cv2.drawContours(frame, [main_contour], -1, (255, 0, 0), 2)

            # Calculate centroid of the hand contour
            centroid = calculate_centroid(main_contour, (roi[0], roi[1]))

            if centroid is not None:
                cx, cy = centroid
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)  # Draw a blue circle at the centroid

        # Display the results
        cv2.imshow('Video Feed', frame)
        cv2.imshow('Masked ROI', mask)

        # Print the x and y positions of grouped contours
        if grouped_contours_positions:
            print("Grouped Contours Positions:", grouped_contours_positions)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video file
    cap.release()
    cv2.destroyAllWindows()

# Specify the path to your video file and the ROI (x, y, width, height)
video_path = "C:/Users/Nicol/OneDrive/Skrivebord/Lego Building Videos/building_1.mkv"
roi = (470, 100, 1100, 700)  # Example ROI, adjust as needed

# Call the function to start the video feed with the specified ROI
detect_human_arm(video_path, roi)
