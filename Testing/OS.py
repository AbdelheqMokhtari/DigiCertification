import os
import cv2 as cv
image_dir = "Data"
files = os.listdir(image_dir)
print(files)
for filename in files:
    filepath = os.path.join(image_dir, filename)
    img = cv.imread(filepath)
    cv.imshow('image', img)
    cv.waitKey(0)

