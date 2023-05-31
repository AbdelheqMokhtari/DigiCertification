import cv2
import numpy as np

image = cv2.imread("image_input/Avoine_0.jpeg")

resized_image = cv2.resize(image, (224, 224))

cv2.imwrite('image_output/Avoine_0.jpg', resized_image)

