import numpy as np

theta1 = (135*(np.pi/180))
theta2 = (180*(np.pi/180))

cos_theta1 = np.cos(theta1)
sin_theta1 = np.sin(theta1)
cos_theta2 = np.cos(theta2)
sin_theta2 = np.sin(theta2)

tx = 1463.29
ty = 653.35
tz = -1295.13

A = np.array([[cos_theta1,-sin_theta1,0,tx],[cos_theta2*sin_theta1,cos_theta2*cos_theta1,-sin_theta2,ty],[sin_theta2*sin_theta1,sin_theta2*cos_theta1,cos_theta2,tz],[0,0,0,1]])

# Traformation along Z
B = np.array([[cos_theta1,-sin_theta1,0,1000],[sin_theta1,cos_theta1,0,0],[0,0,1,0],[0,0,0,1]])
# Tanslation fra cam til base
C = np.array([[-463.20],[-653.35],[1295.13],[1]])


# dot B and C
BC = np.dot(B,C)

print("rot_y: ",B)
print("Transl:",C)
print("Multiply: ",BC)

# product of BC
K = np.array([[cos_theta2,0,-sin_theta2,1519.12356628175],[0,1,0,609.861611661065],[sin_theta2,0,cos_theta2,1295.13000000000],[0,0,0,1]])

print("Matrix k: ", K)

#InvA = np.linalg.inv(A)

#print("1. matrix: ", A)
#rint("2. matrix: " ,InvA)