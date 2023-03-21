#1
import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv

# Load the seed image
img = cv2.imread('/content/Blé dur 3-20002.JPG')

# Perform thresholding to binarize the image
#ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Perform opening morphological operation to remove small objects
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Perform connected component analysis to detect the individual seeds
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(opening)

# Create a CSV file to store the seed properties
with open('seed_properties.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Seed', 'Area', 'Perimeter', 'Aspect Ratio', 'Circularity'])

    # Loop through the detected seeds and extract their morphology
    for i in range(1, ret):
        # Create a mask for the current seed
        mask = np.zeros_like(opening, dtype=np.uint8)
        mask[labels == i] = 255

        # Find the contours of the seed
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the bounding box of the seed
        x, y, w, h = cv2.boundingRect(contours[0])

        # Extract the seed image
        seed = img[y:y+h, x:x+w]

        # Calculate the seed properties
        area = cv2.contourArea(contours[0])
        perimeter = cv2.arcLength(contours[0], True)
        aspect_ratio = float(w)/h
        circularity = (4*np.pi*area)/(perimeter*perimeter)

        # Write the seed properties to the CSV file
        writer.writerow([i, area, perimeter, aspect_ratio, circularity])

        # Save the extracted seed image
        cv2.imwrite('seed'+str(i)+'.jpg', seed)

        # Display the extracted seed image
        plt.imshow(cv2.cvtColor(seed, cv2.COLOR_BGR2RGB))
        plt.show()
        #2
import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv

# Load the seed image
img = cv2.imread('/content/Blé dur 3-20002.JPG')

# Perform thresholding to binarize the image
#ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Perform opening morphological operation to remove small objects
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Perform connected component analysis to detect the individual seeds
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(opening)

# Create a CSV file to store the seed properties
with open('seed_properties.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Seed', 'Area', 'Perimeter', 'Aspect Ratio', 'Circularity'])

    # Loop through the detected seeds and extract their morphology
    for i in range(1, ret):
        # Create a mask for the current seed
        mask = np.zeros_like(opening, dtype=np.uint8)
        mask[labels == i] = 255

        # Find the contours of the seed
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the bounding box of the seed
        x, y, w, h = cv2.boundingRect(contours[0])

        # Extract the seed image
        seed = img[y:y+h, x:x+w]

        # Convert the seed image to grayscale
        gray = cv2.cvtColor(seed, cv2.COLOR_BGR2GRAY)

        # Threshold the grayscale image
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

        # Perform closing morphological operation to fill holes in the seed
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
        closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        # Calculate the seed properties
        area = cv2.contourArea(contours[0])
        perimeter = cv2.arcLength(contours[0], True)
        aspect_ratio = float(w)/h
        circularity = (4*np.pi*area)/(perimeter*perimeter)
        solidity = area/cv2.contourArea(cv2.convexHull(contours[0]))
        extent = area/(w*h)

        # Write the seed properties to the CSV file
        writer.writerow([i, area, perimeter, aspect_ratio, circularity])

        # Display the seed morphology properties
        print("Seed {}: ".format(i))
        print("  Area: {:.2f}".format(area))
        print("  Perimeter: {:.2f}".format(perimeter))
        print("  Aspect Ratio: {:.2f}".format(aspect_ratio))
        print("  Circularity: {:.2f}".format(circularity))
        print("  Solidity: {:.2f}".format(solidity))
        print("  Extent: {:.2f}".format(extent))

        # Save the extracted seed image
        cv2.imwrite('seed'+str(i)+'.jpg', seed)

        # Display the extracted seed image
        plt.imshow(cv2.cvtColor(seed, cv2.COLOR_BGR2RGB))
        #3
 import cv2
import numpy as np
import matplotlib.pyplot as plt
import csv

# Load the seed image
img = cv2.imread('/content/Blé dur 3-20002.JPG')

# Perform thresholding to binarize the image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Perform opening morphological operation to remove small objects
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Perform connected component analysis to detect the individual seeds
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(opening)

# Create a CSV file to store the seed properties
with open('seed_properties.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Seed', 'Length', 'Width', 'Area', 'Perimeter', 'Aspect Ratio', 'Circularity'])

    # Loop through the detected seeds and extract their morphology
    for i in range(1, ret):
        # Create a mask for the current seed
        mask = np.zeros_like(opening, dtype=np.uint8)
        mask[labels == i] = 255

        # Find the contours of the seed
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Get the bounding box of the seed
        x, y, w, h = cv2.boundingRect(contours[0])

        # Extract the seed image
        seed = img[y:y+h, x:x+w]

        # Calculate the seed properties
        area = cv2.contourArea(contours[0])
        perimeter = cv2.arcLength(contours[0], True)
        aspect_ratio = float(w)/h
        circularity = (4*np.pi*area)/(perimeter*perimeter)
        length = max(w, h)
        width = min(w, h)

        # Write the seed properties to the CSV file
        writer.writerow([i, length, width, area, perimeter, aspect_ratio, circularity])

        # Display the seed morphology properties
        print("Seed {}: ".format(i))
        print("  Length: {:.2f}".format(length))
        print("  Width: {:.2f}".format(width))
        print("  Area: {:.2f}".format(area))
        print("  Perimeter: {:.2f}".format(perimeter))
        print("  Aspect Ratio: {:.2f}".format(aspect_ratio))
        print("  Circularity: {:.2f}".format(circularity))

        # Save the extracted seed image
        cv2.imwrite('seed'+str(i)+'.jpg', seed)

        # Display the extracted seed image
        plt.figure(figsize=(5,5))
        plt.imshow(cv2.cvtColor(seed, cv2.COLOR_BGR2RGB))
        plt.title('Seed ' + str(i), fontsize=15)
        plt.axis('off')
        plt.show()
