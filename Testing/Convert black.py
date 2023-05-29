import cv2
import numpy as np

# Load the image
image = cv2.imread('image/Bousselam004.jpg')

# Define the gamma value
gamma = 0.8

# Apply gamma correction
gamma_img = np.power(image / 255.0, gamma)
gamma_img = np.uint8(gamma_img * 255)

# Convert to grayscale
gray = cv2.cvtColor(gamma_img, cv2.COLOR_BGR2GRAY)
# Define the structuring element
kernel = np.ones((21, 21), np.uint8)

# Perform close operation
img_close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Apply median blur
img_blur = cv2.medianBlur(img_close, 15)  # Here, 15 is the kernel size

# Apply Otsu's method to automatically determine the threshold value
thresh_val, thresh_img = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a blank mask of the same size as the image
mask = np.zeros_like(image[:, :, 0])

# Draw contours on the mask
cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

# Apply the mask to the image
result = cv2.bitwise_and(image, image, mask=mask)

cv2.imwrite('image/result.jpg', result)
# Display the resulting image
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
