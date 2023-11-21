import cv2
import time
import numpy as np

fourcc = cv2.VideoWtiter_fourcc(*'XVID')
out = VideoWriter('output.avi',fourcc,20.0,(640,480))