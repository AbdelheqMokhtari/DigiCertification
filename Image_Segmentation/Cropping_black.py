import cv2

# Load the image
img = cv2.imread("black.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
thresh_value = 100
ret, thresh = cv2.threshold(gray, thresh_value, 255, cv2.THRESH_BINARY)

# Apply morphological operations
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
opened = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

# Find connected components
ret, labels, stats, centroids = cv2.connectedComponentsWithStats(opened)
j = 0
# Crop individual kernels
for i in range(1, ret):
    x, y, w, h, area = stats[i]
    if area > 1000:  # filter out small noise
        print("x =", x, "y =", y, "w =", w, "h =", h)
        # crop_img = img[(y-40):(y+h+40), (x-40):(x+w+40)]
        crop_img = img[y:y + h, x:x + w]
        cv2.imwrite(f'Black_image/Wheat_{j}.jpeg', crop_img)
        j += 1
