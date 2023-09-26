import cv2 
import numpy as np

img = cv2.imread("pictures/1.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

Square1 = img2[0:100,0:100]; Square2 = img2[0:100,100:200]; Square3 = img2[0:100,200:300]; Square4 = img2[0:100,300:400]; Square5 = img2[0:100,400:500]
Square6 = img2[100:200,0:100]; Square7 = img2[100:200,100:200]; Square8 = img2[100:200,200:300]; Square9 = img2[100:200,300:400]; Square10 = img2[100:200,400:500]



Average1 = np.average(Square1,axis=0); colorAverage1 = np.average(Average1,axis=0); print('Average =',colorAverage1[0])
Average2 = np.average(Square2,axis=0); colorAverage2 = np.average(Average2,axis=0); print('Average =',colorAverage2[0])
Average3 = np.average(Square3,axis=0); colorAverage3 = np.average(Average3,axis=0); print('Average =',colorAverage3[0])
Average4 = np.average(Square4,axis=0); colorAverage4 = np.average(Average4,axis=0); print('Average =',colorAverage4[0])
Average5 = np.average(Square5,axis=0); colorAverage5 = np.average(Average5,axis=0); print('Average =',colorAverage5[0])
Average6 = np.average(Square6,axis=0); colorAverage6 = np.average(Average6,axis=0); print('Average =',colorAverage6[0])
Average7 = np.average(Square7,axis=0); colorAverage7 = np.average(Average7,axis=0); print('Average =',colorAverage7[0])
Average8 = np.average(Square8,axis=0); colorAverage8 = np.average(Average8,axis=0); print('Average =',colorAverage8[0])
Average9 = np.average(Square9,axis=0); colorAverage9 = np.average(Average9,axis=0); print('Average =',colorAverage9[0])
Average10 = np.average(Square10,axis=0); colorAverage10 = np.average(Average10,axis=0); print('Average =',colorAverage10[0])


cv2.imshow('test1', Square1); cv2.imshow('test2', Square2); cv2.imshow('test3', Square3); cv2.imshow('test4', Square4); cv2.imshow('test5', Square5)
cv2.imshow('test6', Square6); cv2.imshow('test7', Square7); cv2.imshow('test8', Square8); cv2.imshow('test9', Square9); cv2.imshow('test10',Square10)


cv2.imshow('max',img2)
cv2.waitKey(0)
