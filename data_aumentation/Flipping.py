import cv2

# Load the image
img = cv2.imread('Data/image.png')

# Flip the image horizontally
flipped = cv2.flip(img, 1)
flipped_ver = cv2.flip(img, 0)

# Display the original and flipped image
cv2.imshow('Original', img)
cv2.imshow('Flipped', flipped)
cv2.imshow('Flipped_ver', flipped_ver)

# Save the flipped image
cv2.imwrite('Data/flipped_image.jpg', flipped)
cv2.imwrite('Data/flipped_vert_image.jpg', flipped_ver)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()