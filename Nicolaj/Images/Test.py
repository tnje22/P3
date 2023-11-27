import cv2
import numpy as np

# Load the images
image1 = cv2.imread("Nicolaj/Images/1920x1080-black-solid-color-background.jpg")
image2 = cv2.imread("Nicolaj/Images/test.png")

# Define the coordinates of the region you want to overlap
x, y, w, h = 100, 100, 200, 200

# Crop the region from the first image
crop_region = image1[y:y+h, x:x+w]

# Resize the crop region to match the size of the region in the second image
crop_region_resized = cv2.resize(crop_region, (w, h))

# Overlap the resized crop region onto the second image
image2[y:y+h, x:x+w] = crop_region_resized

# Display the result
cv2.imshow('Result', image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
