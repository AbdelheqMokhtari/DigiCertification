import cv2
import numpy as np
# Load image
img = cv2.imread('GTA001.jpg')

# Perform histogram equalization
# img_eq = cv2.equalizeHist(img_blur)

# Define the gamma value
gamma = 0.6

# Apply gamma correction
gamma_img = np.power(img/255.0, gamma)
gamma_img = np.uint8(gamma_img*255)

# Convert to grayscale
gray = cv2.cvtColor(gamma_img, cv2.COLOR_BGR2GRAY)

# Apply median blur
img_blur = cv2.medianBlur(gray, 5)  # Here, 5 is the kernel size

# Apply Gaussian blur with kernel size 5x5 and standard deviation of 0
blurred = cv2.GaussianBlur(img_blur, (5, 5), 0)

# Perform histogram equalization
img_eq = cv2.equalizeHist(blurred)  # bad

# Apply Otsu's method to automatically determine the threshold value
thresh_val, thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display results
cv2.imshow('Gamma Correction Image', gamma_img)
cv2.imshow('input  Image', img_blur)
cv2.imshow('blur Image', img_blur)
cv2.imshow('Gaussian Image', blurred)
cv2.imshow('eq Image', img_eq)
cv2.imshow('eq Image', thresh_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Save/gray_image.jpg', gray)
cv2.imwrite('Save/blur_image.jpg', img_blur)
cv2.imwrite('Save/HE_image.jpg', gamma_img)
cv2.imwrite('Save/Gaussian_Image.jpg', blurred)
cv2.imwrite('Save/Histogram_Image.jpg', img_eq)
cv2.imwrite('Save/OTSU_Image.jpg', thresh_img)
