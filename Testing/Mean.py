import numpy as np
from PIL import Image
import cv2 as cv

# Load image
img = Image.open('Wheat_1.jpg')
img_opencv = cv.imread("Wheat_1.jpg")
img_array = np.array(img)
#img_array = np.array(img_opencv)

# Calculate mean for each channel
mean = np.mean(img_array, axis=(0, 1))

# Print mean values for each channel
print('Mean R: {:.2f}'.format(mean[0]))
print('Mean G: {:.2f}'.format(mean[1]))
print('Mean B: {:.2f}'.format(mean[2]))