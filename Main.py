import cv2 
import numpy as np

img = cv2.imread("pictures/1.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

Square1 = img2[0:100,0:100]
Square2 = img2[0:100,100:200]
Square3 = img2[0:100,200:300]
Square4 = img2[0:100,300:400]
Square5 = img2[0:100,400:500]
Square6 = img2[100:200,0:100]

Average1 = np.average(Square1,axis=0); colorAverage1 = np.average(Average1,axis=0); print('Average =',colorAverage1)
Average2 = np.average(Square2,axis=0); colorAverage2 = np.average(Average2,axis=0); print('Average =',colorAverage2)
Average3 = np.average(Square3,axis=0); colorAverage3 = np.average(Average3,axis=0); print('Average =',colorAverage3)
Average4 = np.average(Square4,axis=0); colorAverage4 = np.average(Average4,axis=0); print('Average =',colorAverage4)
Average5 = np.average(Square5,axis=0); colorAverage5 = np.average(Average5,axis=0); print('Average =',colorAverage5)
Average6 = np.average(Square6,axis=0); colorAverage6 = np.average(Average6,axis=0); print('Average =',colorAverage6)


cv2.imshow('test1', Square1)
cv2.imshow('test2', Square2)
cv2.imshow('test3', Square3)
cv2.imshow('test4', Square4)
cv2.imshow('test5', Square5)
cv2.imshow('test6', Square6)
cv2.imshow('max',img2)
cv2.waitKey(0)
