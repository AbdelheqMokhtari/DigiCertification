from keras.applications.resnet import preprocess_input, decode_predictions
from keras.models import load_model
from keras.utils import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
import cv2
import numpy as np
# Load the h5 model file
model = load_model('Model/ResNet50New20.h5')


# Load and preprocess the new image
img_keras = load_img('Crop images/Triticale.jpeg', target_size=(224, 224))
img_keras = img_to_array(img_keras)
normalized_img = img_keras / 255.0
img_keras = np.expand_dims(normalized_img, axis=0)
# img = preprocess_input(img)

# load and preprocess the new image using openCV
img = cv2.imread('Crop images/Triticale.jpeg')

# Convert BGR to RGB and resize the image
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (224, 224))

# Convert the OpenCV image to a NumPy array
img = np.asarray(img)

img = img_to_array(img)
normalized_img = img / 255.0
img = np.expand_dims(normalized_img, axis=0)

# Make predictions on the preprocessed image
predictions = model.predict(img)

# Convert one-hot encoded predictions to class labels
class_labels = np.argmax(predictions, axis=1)

# Process the predictions as needed
print(class_labels)




