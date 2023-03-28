from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
from PIL import Image
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelBinarizer

# Load the seed dataset and preprocess the data
# Load the dataset
data = []
labels = []
classes = ['barley', 'corn', 'wheat']
for class_name in classes:
    class_path = os.path.join('data', class_name)
    for img_name in os.listdir(class_path):
        img_path = os.path.join(class_path, img_name)
        img = Image.open(img_path)
        img = img.resize((224, 224))
        img = np.array(img)
        img = img / 255.0
        data.append(img)
        labels.append(class_name)

# Convert the data and labels to NumPy arrays
data = np.array(data)
labels = np.array(labels)

# One-hot encode the labels
lb = LabelBinarizer()
labels = lb.fit_transform(labels)

# Split the dataset into training, validation, and testing sets
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_test, y_test, test_size=0.5, random_state=42)
# Build the ResNet50 model
num_classes = 5
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_data, epochs=num_epochs, validation_data=val_data)

# Evaluate the model
model.evaluate(test_data)

# Fine-tune the model

# Predict using the model
predictions = model.predict(new_data)
