import cv2
import numpy as np
# Load image
img = cv2.imread('Bousselam009.jpg')

# Perform histogram equalization
# img_eq = cv2.equalizeHist(img_blur)

# Define the gamma value
gamma = 0.8

# Apply gamma correction
gamma_img = np.power(img/255.0, gamma)
gamma_img = np.uint8(gamma_img*255)

# Convert to grayscale
gray = cv2.cvtColor(gamma_img, cv2.COLOR_BGR2GRAY)

# Define the structuring element
kernel = np.ones((21, 21), np.uint8)

# Perform close operation
img_close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Apply median blur
img_blur = cv2.medianBlur(img_close, 15)  # Here, 15 is the kernel size

# Apply Gaussian blur with kernel size 5x5 and standard deviation of 0
blurred = cv2.GaussianBlur(img_close, (5, 5), 0)  # no improvements

# Perform histogram equalization
img_eq = cv2.equalizeHist(blurred)  # bad

# Apply Otsu's method to automatically determine the threshold value
thresh_val, thresh_img = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter out small contours and draw the remaining contours on the original image
# for contour in contours:
    # if cv2.contourArea(contour) > 100: # Minimum area threshold
        # cv2.drawContours(img, [contour], 0, (0, 255, 0), 2)


# Display results
# cv2.imshow('Gamma Correction Image', gamma_img)
# cv2.imshow('input  Image', img_blur)
# cv2.imshow('blur Image', img_blur)
# cv2.imshow('Gaussian Image', blurred)
# cv2.imshow('eq Image', img_eq)
# cv2.imshow('eq Image', thresh_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite('Save/gray_image.jpg', gray)
# cv2.imwrite('Save/blur_image.jpg', img_blur)
# cv2.imwrite('Save/HE_image.jpg', gamma_img)
# cv2.imwrite('Save/Gaussian_Image.jpg', blurred)
# cv2.imwrite('Save/Histogram_Image.jpg', img_eq)
cv2.imwrite('Save/OTSU_Image_0.8_close_median_15.jpg', thresh_img)
cv2.imwrite('Save/image.jpg', img)

j = 0
# Filter out small contours and draw bounding box around the remaining contours
for contour in contours:
    if cv2.contourArea(contour) > 100: # Minimum area threshold
        x, y, w, h = cv2.boundingRect(contour)
        print("Area =", cv2.contourArea(contour), "x =", x, "y =", y, "w =", w, "h =", h)
        crop_img = img[y:(y + h), x:(x + w)]
        # Get the original height and width of the image
        height, width = img.shape[:2]

        # Set the desired output size
        output_size = 224

        # Calculate the amount of padding needed on each side
        h_pad = max(0, (output_size - height) // 2)
        w_pad = max(0, (output_size - width) // 2)

        # Add the padding using copyMakeBorder() function
        output_img = cv2.copyMakeBorder(img, h_pad, h_pad, w_pad, w_pad, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        cv2.imwrite(f'Save/Crop/Vitron_{j}.jpeg', output_img)
        j += 1

