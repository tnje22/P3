import numpy as np

#legobrick position seen from the camara
x_Lego_camera = 20
y_Lego_camera = -30
z_Lego_camera = 100
#ur10 position seen from the camara
x_ur10 = 60
y_ur10 = 60
z_ur10 = 100

# Given transformation matrix describing rotation and translation of UR10 seen from the camera
transformation_matrix = np.array([[0, 1, 0, x_ur10],
                                  [1, 0, 0, y_ur10],
                                  [0, 0, 1, z_ur10],
                                  [0, 0, 0, 1]])

# Homogeneous coordinates for UR10 position (including 1 for translation)
ur10_position_homogeneous = np.array([x_ur10, y_ur10, z_ur10, 1])

# Apply transformation matrix to UR10 position
ur10_transformed = np.dot(transformation_matrix, ur10_position_homogeneous)

# Extract transformed coordinates of UR10
x_ur10_transformed = ur10_transformed[0]
y_ur10_transformed = ur10_transformed[1]
z_ur10_transformed = ur10_transformed[2]

# Homogeneous coordinates for Lego brick position seen from the camera (including 1 for translation)
lego_brick_camera_homogeneous = np.array([x_Lego_camera, y_Lego_camera, z_Lego_camera, 1])

# Apply transformation matrix to Lego brick position seen from the camera
lego_brick_transformed = np.dot(transformation_matrix, lego_brick_camera_homogeneous)

# Extract transformed coordinates of Lego brick in the transformed UR10 coordinate system
x_lego_brick_transformed = lego_brick_transformed[0]
y_lego_brick_transformed = lego_brick_transformed[1]
z_lego_brick_transformed = lego_brick_transformed[2]

# Calculate relative position of Lego brick in the transformed UR10 coordinate system
x_Brick_transformed = x_lego_brick_transformed - x_ur10_transformed
y_Brick_transformed = y_lego_brick_transformed - y_ur10_transformed
z_Brick_transformed = z_lego_brick_transformed - z_ur10_transformed

print("Lego brick (xyz) seen from the transformed UR10:")
print(x_Brick_transformed)
print(y_Brick_transformed)
print(z_Brick_transformed)
