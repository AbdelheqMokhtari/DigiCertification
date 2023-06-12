import cv2
import os
from skimage.filters import median
from scipy.ndimage import gaussian_filter
import numpy as np

# Define Image Path
image_dir = "Full images"
folder = os.listdir(image_dir)
for folderName in folder:
    folderPath = os.path.join(image_dir, folderName)
    print(folderPath)
    j = 0
    for filename in os.listdir(folderPath):
        print("The image selected :", filename)
        filepath = os.path.join(folderPath, filename)
        print("path", filepath)
        img = cv2.imread(filepath)
        # Apply adaptive median filter

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        filtered_image_median = median(gray, behavior='adaptive', mode='reflect')

        # Apply adaptive Gaussian filter
        filtered_image_guassian = gaussian_filter(filtered_image_median, sigma=3)

        # Apply Otsu's method to automatically determine the threshold value
        thresh_val, thresh_img = cv2.threshold(filtered_image_guassian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Use the optimal threshold for Canny edge detection
        edges = cv2.Canny(filtered_image_guassian, threshold1=0.5 * thresh_val, threshold2=thresh_val)

        combined = cv2.bitwise_or(thresh_img, edges)

        # Find contours in the binary image
        contours, hierarchy = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Filter out small contours and draw bounding box around the remaining contours
        for contour in contours:
            if cv2.contourArea(contour) > 2000:  # Minimum area threshold
                # Get the bounding box coordinates
                x, y, w, h = cv2.boundingRect(contour)
                print("Area =", cv2.contourArea(contour), "x =", x, "y =", y, "w =", w, "h =", h)

                # crop image
                crop_img = img[y:(y + h), x:(x + w)]

                # Get the original height and width of the image
                height, width = crop_img.shape[:2]

                # Set the desired output size
                output_size = 330

                # Calculate the amount of padding needed on each side
                h_pad = max(0, (output_size - height) // 2)
                w_pad = max(0, (output_size - width) // 2)

                # Add the padding using copyMakeBorder() function
                output_img = cv2.copyMakeBorder(crop_img, h_pad, h_pad, w_pad, w_pad, cv2.BORDER_CONSTANT, value=(0, 0,
                                                                                                                 0))

                folder_name = f'Crop images/{folderName}'
                # Create the folder and any necessary parent folders
                os.makedirs(folder_name, exist_ok=True)

                cv2.imwrite(f'{folder_name}/{folderName}_{j}.jpeg', output_img)
                j += 1



