import cv2
import numpy as np

# Load the image and convert it to grayscale
img = cv2.imread("GTA001.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#  Appliquer un filtre de flou Gaussian
bb = cv2.GaussianBlur(img, (3, 3), 0)

# Apply thresholding
thresh_value = 100
ret, thresh = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)

# Apply morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find connected components
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(opened)
# Crop individual kernels
for i in range(1, ret):
    x, y, w, h, area = stats[i]
    if area > 1000 and x > 10 and y > 10 and w > 40 and h > 40:  # filter out small noise
        print("Area =", area, "x =", x, "y =", y, "w =", w, "h =", h)
        # crop_img = img[(y-40):(y+h+40), (x-40):(x+w+40)]
        # crop_img = img[(y - 100):(y + h + 100), (x - 100):(x + w + 100)]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imwrite('example_saved.jpg', img)

