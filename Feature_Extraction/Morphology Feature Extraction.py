import cv2 as cv
import numpy as np
import pandas as pd
import os

Columns = ["Height", "Width", "area", "perimeter", "circularity", "aspect_ratio", "solidity"]

df = pd.DataFrame(columns=Columns)

# Define Image Path
image_dir = "Data"
files = os.listdir(image_dir)
for filename in files:
    # Loading image
    print("\nThe image selected :", filename)
    filepath = os.path.join(image_dir, filename)
    img = cv.imread(filepath)

    # initialise an empty list to store all Feature of the image
    Features = []

    # Convert to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Threshold the image to binary
    _, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

    # Find the contours of the wheat plant
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area (which should be the wheat plant)
    max_contour = min(contours, key=cv.contourArea)

    # Get the bounding box of the contour
    x, y, w, h = cv.boundingRect(max_contour)

    # Draw the bounding box on the image
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    height = h
    width = w
    area = cv.contourArea(max_contour)
    perimeter = cv.arcLength(max_contour, True)
    circularity = (4 * np.pi * area) / (perimeter * perimeter)
    aspect_ratio = float(w) / h
    solidity = area / cv.contourArea(cv.convexHull(max_contour))

    Features.append(height)
    print(f"Kernel Height: {height}")

    Features.append(width)
    print(f"Kernel Width: {width}")

    Features.append(area)
    print(f"Kernel Area: {area}")

    Features.append(perimeter)
    print(f"Kernel Perimeter: {perimeter}")

    Features.append(circularity)
    print(f"Kernel Circularity: {circularity}")

    Features.append(aspect_ratio)
    print(f"Kernel Aspect_ratio: {aspect_ratio}")

    Features.append(solidity)
    print(f"Kernel Solidity: {solidity}")

    print(
        "*******************************************************************************************************\n")

    df.loc[len(df)] = Features

print(df)
df.to_csv('Morphological Feature.csv', index=False)

