# import necessary libraries
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from skimage.io import imread
from skimage.transform import resize

# load image data
image_data = []
labels = []

# Load wheat grain images
for i in range(1, 1001):
    image = imread(f'wheat_grains/{i}.jpg', as_gray=True)
    image_resized = resize(image, (100, 100), anti_aliasing=True, mode='reflect')
    image_data.append(image_resized.flatten())
    labels.append('wheat_grain')
# Load valid bean images
for i in range(1, 501):
    image = imread(f'valid_beans/{i}.jpg', as_gray=True)
    image_resized = resize(image, (100, 100), anti_aliasing=True, mode='reflect')
    image_data.append(image_resized.flatten())
    labels.append('valid_bean')

# Load invalid bean images
for i in range(1, 501):
    image = imread(f'invalid_beans/{i}.jpg', as_gray=True)
    image_resized = resize(image, (100, 100), anti_aliasing=True, mode='reflect')
    image_data.append(image_resized.flatten())
    labels.append('invalid_bean')

# Load impurity images
for i in range(1, 501):
    image = imread(f'impurities/{i}.jpg', as_gray=True)
    image_resized = resize(image, (100, 100), anti_aliasing=True, mode='reflect')
    image_data.append(image_resized.flatten())
    labels.append('impurity')

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(image_data, labels, test_size=0.2, random_state=42)

# train the SVM model
svm = SVC(kernel='rbf', gamma=0.001, C=10)
svm.fit(X_train, y_train)

# predict on test data
y_pred = svm.predict(X_test)

# calculate accuracy and confusion matrix
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
