import cv2
import numpy as np

def process_camera_input(camera_input):
    # Add your Lego bricks and their positions processing
    #arr=[]
    #arr[farve][shape]

    return detected_legos

def identify_current_step(detected_legos):

   #"C:\Users\tnj70\Desktop\Data\Step list dumi.txt"
    num_detected_legos = len(detected_legos)

    if num_detected_legos == 0:
        print("No Lego bricks detected. Waiting for the first step.")
    else:
        print(f"Detected {num_detected_legos} Lego bricks.")

        # Your logic to determine the current step based on the number of detected_legos
        if num_detected_legos <= 5:
            print("Step 1: Placing the base bricks.")
        elif num_detected_legos <= 10:
            print("Step 2: Adding additional bricks.")
        else:
            print("Step 3: Finalizing the Lego structure.")

if __name__ == "__main__":
    camera_input_path = "camera_image.jpg"  # Replace with the actual path to the camera input image

    detected_legos = process_camera_input(camera_input_path)
    identify_current_step(detected_legos)