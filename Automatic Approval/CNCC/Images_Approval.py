import cv2
import numpy as np
from keras.utils import img_to_array
from tensorflow import keras

image = cv2.imread("Image/Orge 19.jpg")

# Define the gamma value
gamma = 0.8

# Apply gamma correction
gamma_img = np.power(image/255.0, gamma)
gamma_img = np.uint8(gamma_img*255)

# Convert to grayscale
gray = cv2.cvtColor(gamma_img, cv2.COLOR_BGR2GRAY)

# Define the structuring element
kernel = np.ones((21, 21), np.uint8)

# Perform close operation
img_close = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# Apply median blur
img_blur = cv2.medianBlur(img_close, 15)  # Here, 15 is the kernel size

# Apply Otsu's method to automatically determine the threshold value
thresh_val, thresh_img = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


total_number = 0
# Filter out small contours and draw the remaining contours on the original image
for contour in contours:
    if cv2.contourArea(contour) > 1000:  # Minimum area threshold
        # cv2.drawContours(image, [contour], 0, (0, 255, 0), 5)
        total_number += 1


crop_image = []
for contour in contours:
    if cv2.contourArea(contour) > 1000:  # Minimum area threshold
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)
        print("Area =", cv2.contourArea(contour), "x =", x, "y =", y, "w =", w, "h =", h)

        crop_img = image[y:(y + h), x:(x + w)]
        # Get the original height and width of the image
        height, width = crop_img.shape[:2]

        # Set the desired output size
        output_size = 350

        # Calculate the amount of padding needed on each side
        h_pad = max(0, (output_size - height) // 2)
        w_pad = max(0, (output_size - width) // 2)

        # Add the padding using copyMakeBorder() function
        output_img = cv2.copyMakeBorder(crop_img, h_pad, h_pad, w_pad, w_pad, cv2.BORDER_CONSTANT,
                                        value=(0, 0,
                                               0))

        # crop image
        crop_image.append(output_img)

# Load your saved model
model = keras.models.load_model('Model/ResNet50New20.h5')

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
print(y_pred)
