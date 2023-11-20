import cv2
import numpy as np
# der kommer en liste af ting der er gjort 
def process_camera_input(camera_input):
    # Add your Lego bricks and their positions processing


    return detected_legos

def identify_current_step(detected_legos):

   #"C:\Users\tnj70\Desktop\Data\Step list dumi.txt"
    num_detected_legos = len(detected_legos)

   
if __name__ == "__main__":
    camera_input_path = "camera_image.jpg"  # Replace with the actual path to the camera input image

    detected_legos = process_camera_input(camera_input_path)
    identify_current_step(detected_legos)