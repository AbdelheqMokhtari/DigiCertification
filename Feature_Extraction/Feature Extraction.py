import cv2
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os

img = cv2.imread("Wheat_1.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Calculate the color histogram
hist = cv2.calcHist([img], [0], None, [256], [0, 256]) # [1] -> for Green, [2] -> for Red
# print(hist)
# print("_______________________________")

# plot the above computed histogram
plt.plot(hist, color='b')
plt.title('Image Histogram For Blue Channel GFG')
# plt.show()

hist = cv2.normalize(hist, hist).flatten()
print(hist)



# df = pd.DataFrame(columns=['image', 'color_features'])
# df = df.append({'image': "image 1", 'color_features': hist}, ignore_index=True)
# print(df)