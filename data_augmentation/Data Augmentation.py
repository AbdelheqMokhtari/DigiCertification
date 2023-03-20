import os
import numpy as np
import cv2
from keras.preprocessing.image import ImageDataGenerator

# Define data augmentation parameters
datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
    fill_mode='nearest')

# Define image directory and batch size
img_dir = 'Data'
batch_size = 32

# Load images from directory
img_list = os.listdir(img_dir)
print(img_list)

# Define generator for augmented images
gen = datagen.flow_from_directory(
    img_dir,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical')

# Generate and save augmented images
for i in range(len(img_list) // batch_size):
    X_batch, y_batch = next(gen)
    for j in range(batch_size):
        img = X_batch[j]
        label = np.argmax(y_batch[j])
        img_name = 'augmented_seed_' + str(i * batch_size + j) + '.jpg'
        img_path = os.path.join(img_dir, label, img_name)
        cv2.imwrite(img_path, img)
