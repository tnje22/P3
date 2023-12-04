import numpy as np

cos_theta1 = np.cos(135)
sin_theta1 = np.sin(135)
cos_theta2 = np.cos(180)
sin_theta2 = np.sin(180)

tx = 1463.29
ty = 653.35
tz = -1295.13

A = np.array([[cos_theta1,-sin_theta1,0,tx],[cos_theta2*sin_theta1,cos_theta2*cos_theta1,-sin_theta2,ty],[sin_theta2*sin_theta1,sin_theta2*cos_theta1,cos_theta2,tz],[0,0,0,1]])

InvA = np.linalg.inv(A)

print("1. matrix: ", A)
print("2. matrix: " ,InvA)