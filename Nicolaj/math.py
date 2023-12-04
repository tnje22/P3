import numpy as np

cos_theta1 = np.cos(135)
sin_theta1 = np.sin(135)
cos_theta2 = np.cos(180)
sin_theta2 = np.sin(180)

A = np.array([[cos_theta1,-sin_theta1,0,1463.29],[cos_theta2*sin_theta1,cos_theta2*cos_theta1,-sin_theta2,653.35],[sin_theta2*sin_theta1,sin_theta2*cos_theta1,cos_theta2,-1295.13],[0,0,0,1]])

InvA = np.linalg.inv(A)

print("1. matrix: ", A)
print("2. matrix: " ,InvA)