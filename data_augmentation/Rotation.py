import cv2

# Load the image
img = cv2.imread('Data/image.png')

# Define the rotation angle
angle = 45
second_angle = 135

# Get the image size
height, width = img.shape[:2]

# Define the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
second_rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), second_angle, 1)

# Rotate the image using the rotation matrix
rotated = cv2.warpAffine(img, rotation_matrix, (width, height))
second_rotated = cv2.warpAffine(img, second_rotation_matrix, (width, height))

# Display the original and rotated images
cv2.imshow('Original', img)
cv2.imshow('Rotated', rotated)
cv2.imshow('Rotated', second_rotated)

# Save the rotated image
cv2.imwrite('Data/rotated_image.jpg', rotated)
cv2.imwrite('Data/rotated_image2.jpg', second_rotated)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
