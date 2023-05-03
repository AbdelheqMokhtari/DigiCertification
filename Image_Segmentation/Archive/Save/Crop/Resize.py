import cv2
import numpy as np

# Load input image
img = cv2.imread('Vitron_0.jpeg')

# Get the original height and width of the image
height, width = img.shape[:2]

# Set the desired output size
output_size = 224

# Calculate the amount of padding needed on each side
h_pad = max(0, (output_size - height) // 2)
w_pad = max(0, (output_size - width) // 2)

# Add the padding using copyMakeBorder() function
output_img = cv2.copyMakeBorder(img, h_pad, h_pad, w_pad, w_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))

# Display the result
cv2.imwrite(f'Vitron_0_size.jpeg', output_img)

