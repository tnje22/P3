import cv2 
import numpy as np

game = cv2.imread("pictures/1.jpg")
cv2.imshow("test",game)


Higth = 250
Width = 150
R = game[Higth,Width][2]
G = game[Higth,Width][1]
B = game[Higth,Width][0]
print(game[Higth,Width])
print(B)
print(G)
print(R)

cv2.waitKey(0)
cv2.destroyAllWindows()