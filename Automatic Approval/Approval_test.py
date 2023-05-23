import cv2
import numpy as np
from tensorflow import keras

# Load your saved model
model = keras.models.load_model('Model/ResNet50New20.h5')

image = cv2.imread("Crop images/Orge.jpeg")

resized_image = cv2.resize(image, (224, 224))
normalized_image = resized_image / 255.0  # Normalize pixel values
preprocessed_image = np.expand_dims(normalized_image, axis=0)

preprocessed_image = np.array(preprocessed_image)

# Make predictions on the test data
y_pred_prob = model.predict(preprocessed_image)

# Convert the predicted probabilities to labels
y_pred = np.argmax(y_pred_prob, axis=1)
print(y_pred)