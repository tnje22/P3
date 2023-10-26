import cv2
import numpy as np

# Create a VideoCapture object to capture video from your camera
cap = cv2.VideoCapture(0)

#creating a while loop so the code will constand run
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    #if the code can't read a camera or the camera is not activated it breaks the loop
    if not ret:
        break
    
    #otherwise it will continue witht he loop
    
    #First we convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Then we apply Gaussian blur to the grayscale frame
    blurred = cv2.GaussianBlur(gray, (15, 15), 0)

    #We then threshold the blurred image to create a binary image
    _, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)

    #And then we locate contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #We then filter the contours to find the hand contour
    hand_contour = None
    max_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > max_area:
            max_area = area
            hand_contour = contour

    #After filtering we then draw a bounding box around the hand, so we know the area where the hand is.
    if hand_contour is not None:
        x, y, w, h = cv2.boundingRect(hand_contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        #We add a center point to Calculate the thand position in (x,y)
        center_x = x + w // 2 
        center_y = y + h // 2
        cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

        #Here we constandly update the hand_position variable
        hand_position = (center_x, center_y)
        
        
    #Lastly we display the frame(camerea feed + our code)
    cv2.imshow("Hand Detection", frame)

    #If the 'q' key is pressed we then exit the loop and stops the script. this we can changes to somethin different if we nne to.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Closes the windows and stops the camera recording
cap.release()
cv2.destroyAllWindows()

#We then print the final hand position using the han_position variable
print("Final hand position:", hand_position)