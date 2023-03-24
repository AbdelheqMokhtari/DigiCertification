import cv2
import numpy as np

# Load the image and convert it to grayscale
img = cv2.imread("imane.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the seeds
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Apply morphological operations to remove noise and gaps within the segmented seeds
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=3)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel, iterations=3)

# Find contours of the segmented seeds
contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Select the contours that have a sufficient area (assuming small seeds have less area than large ones)
min_seed_area = 2000  # you may need to adjust this based on the specific characteristics of your seeds
seed_contours = []
for c in contours:
    if cv2.contourArea(c) > min_seed_area:
        seed_contours.append(c)
j = 0
# Draw a bounding box around each selected seed and crop the image
for i, c in enumerate(seed_contours):
    x, y, w, h = cv2.boundingRect(c)
    crop_img = img[y:y+h, x:x+w]
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # cv2.imshow("Data/Seed {}".format(i+1), crop_img)
    cv2.imwrite(f'test/seed_{j}.png', crop_img)
    j += 1

# Display the original image with detected seeds and bounding boxes
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

