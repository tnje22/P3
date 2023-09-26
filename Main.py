import cv2 
import numpy as np

game = cv2.imread("pictures/1.jpg")

height = 20
width = 20
hypo = 90

cx = int(height / 2)
cy = int(width / 2)

start_point = cx - hypo, cy - hypo
end_point = cx + hypo, cy + hypo


pixel_center_bgr = game[cx, cy]
b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
cv2.rectangle(game, start_point, end_point, (0, 0, 255), 3)

Higth = 250
Width = 150
R = game[Higth,Width][2]
G = game[Higth,Width][1]
B = game[Higth,Width][0]
print(game[Higth,Width])
print(B)
print(G)
print(R)

cv2.imshow("test",game)
cv2.waitKey(0)
cv2.destroyAllWindows()