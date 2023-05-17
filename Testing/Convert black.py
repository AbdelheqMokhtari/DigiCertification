import cv2
import numpy as np

# Load the image
image = cv2.imread('your_image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to obtain a binary image
_, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours of the grains
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank mask image
mask = np.zeros_like(image)

# Draw the contours on the mask image
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Convert the mask image to grayscale
mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

# Threshold the mask image to obtain a binary mask
_, binary_mask = cv2.threshold(mask_gray, 1, 255, cv2.THRESH_BINARY)

# Apply the binary mask to the original image
result = cv2.bitwise_and(image, image, mask=binary_mask)

# Display the resulting image
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
