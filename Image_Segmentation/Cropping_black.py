import cv2
import os

# Define Image Path
image_dir = "Bousselam_image"
files = os.listdir(image_dir)
j = 0
for filename in files:
    # Loading image
    print("The image selected :", filename)
    filepath = os.path.join(image_dir, filename)
    print("path", filepath)
    img = cv2.imread(filepath)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

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
        if area > 5000 and x > 10 and y > 10 and w > 90 and h > 90:  # filter out small noise
            print("Area =", area, "x =", x, "y =", y, "w =", w, "h =", h)
            # crop_img = img[(y-40):(y+h+40), (x-40):(x+w+40)]
            crop_img = img[(y-10):(y + h + 10), (x-10):(x + w + 10)]
            cv2.imwrite(f'Bousselam_add/Wheat_{j}.jpeg', crop_img)
            j += 1
    print("number =", j, "\n****************************************************************************************\n")
