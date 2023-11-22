import numpy as np

# Lego brick position seen from the camera
x_Lego_camera = 20
y_Lego_camera = -30
z_Lego_camera = 100

# UR10 position seen from the camera
x_ur10 = 60
y_ur10 = 60
z_ur10 = 100

# Belt movement in an arbitrary direction of the camara 
belt_movement_x = 10  # Assume the UR10 moves 10 cm in the X direction
belt_movement_y = 0   # Assume no movement in the Y direction
belt_movement_z = 0   # Assume no movement in the Z direction

# Given transformation matrix describing rotation and translation of UR10 seen from the camera
transformation_matrix = np.array([[1, 0, 0, x_ur10 + belt_movement_x],
                                  [0, 1, 0, y_ur10 + belt_movement_y],
                                  [0, 0, 1, z_ur10 + belt_movement_z],
                                  [0, 0, 0, 1]])

# Homogeneous coordinates for Lego brick position seen from the camera (including 1 for translation)
lego_brick_camera_homogeneous = np.array([x_Lego_camera, y_Lego_camera, z_Lego_camera, 1])

# Apply transformation matrix to Lego brick position seen from the camera
lego_brick_transformed = np.dot(transformation_matrix, lego_brick_camera_homogeneous)

# Extract transformed coordinates of Lego brick in the transformed UR10 coordinate system
x_Brick_transformed = lego_brick_transformed[0] - (x_ur10 + belt_movement_x)
y_Brick_transformed = lego_brick_transformed[1] - (y_ur10 + belt_movement_y)
z_Brick_transformed = lego_brick_transformed[2] - (z_ur10 + belt_movement_z)

print("Lego brick (xyz) seen from the transformed UR10:")
print(x_Brick_transformed)
print(y_Brick_transformed)
print(z_Brick_transformed)
