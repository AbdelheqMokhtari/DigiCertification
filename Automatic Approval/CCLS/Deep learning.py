import cv2
import numpy as np
from keras.utils import img_to_array
from tensorflow import keras
from skimage.filters import median
from scipy.ndimage import gaussian_filter
import pandas as pd
import os

# Load your saved model
model = keras.models.load_model('Model/ALL5_New_ResNet50_epochs100.h5')
columns = ["Image N", "Ble dur", "Casee", "Metadine", "Maigres", "Echaudes", "Total"]
df = pd.DataFrame(columns=columns)
files = os.listdir("image")
print(files)
for i, file in enumerate(files):
    filepath = os.path.join("image", file)
    print(filepath)
    image = cv2.imread(filepath)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

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

    total_number = 0
    # Filter out small contours and draw the remaining contours on the original image

    crop_image = []
    for contour in contours:
        if cv2.contourArea(contour) > 2000:
            total_number += 1
            # Minimum area threshold
            # Get the bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            print("Area =", cv2.contourArea(contour), "x =", x, "y =", y, "w =", w, "h =", h)

            crop_img = image[y:(y + h), x:(x + w)]
            # Get the original height and width of the image
            height, width = crop_img.shape[:2]

            # Set the desired output size
            output_size = 280
            # output_size = 630  # CNCC dataset
            # Calculate the amount of padding needed on each side
            h_pad = max(0, (output_size - height) // 2)
            w_pad = max(0, (output_size - width) // 2)

            # Add the padding using copyMakeBorder() function
            output_img = cv2.copyMakeBorder(crop_img, h_pad, h_pad, w_pad, w_pad, cv2.BORDER_CONSTANT,
                                            value=(0, 0,
                                                   0))

            # crop image
            crop_image.append(output_img)

    preprocessed_images = []
    for image_tf in crop_image:
        # Convert BGR to RGB and resize the image
        image_tf = cv2.cvtColor(image_tf, cv2.COLOR_BGR2RGB)
        image_tf = cv2.resize(image_tf, (224, 224))

        # Convert the OpenCV image to a NumPy array
        image_tf = np.asarray(image_tf)

        image_tf = img_to_array(image_tf)
        normalized_img = image_tf / 255.0
        preprocessed_image = np.expand_dims(normalized_img, axis=0)
        preprocessed_images.append(preprocessed_image)

    preprocessed_images = np.array(preprocessed_images)

    preprocessed_images = preprocessed_images.reshape(-1, 224, 224, 3)

    # print(preprocessed_images)

    # Make predictions on the test data
    y_pred_prob = model.predict(preprocessed_images)

    # Convert the predicted probabilities to labels
    y_pred = np.argmax(y_pred_prob, axis=1)
    y_pred = y_pred.tolist()

    sum_prediction = [i+1, y_pred.count(0), y_pred.count(1), y_pred.count(4), y_pred.count(3),
                      y_pred.count(2),
                      y_pred.count(0) + y_pred.count(1) + y_pred.count(2) + y_pred.count(3) + y_pred.count(4)]

    df.loc[len(df)] = sum_prediction
df.to_csv('Prediction CCLS .csv', index=False)