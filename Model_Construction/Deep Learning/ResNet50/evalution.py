import json

import h5py
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
import seaborn as sns
from tensorflow import keras
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report

test_datagen = ImageDataGenerator(rescale=1./255)

test_data = test_datagen.flow_from_directory(
    'Data/test',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

y_true = test_data.classes

# Load your saved model
model = keras.models.load_model('Model/CNCC/ResNet50_epochs50_false_unfreeze10.h5')

# Retrieve the class names from the HDF5 file attributes
with h5py.File('Model/CNCC/ResNet50_epochs50_false_unfreeze10.h5', 'r') as file:
    class_names = file.attrs['class_names']

# class_names = ['Avoine', 'Ble dur', 'ble tendre', 'orge', 'triticale']

# Make predictions on the test data
y_pred_prob = model.predict(test_data)

# Convert the predicted probabilities to labels
y_pred_labels = np.argmax(y_pred_prob, axis=1)

# Generate the confusion matrix
cm = confusion_matrix(y_true, y_pred_labels)

# Create a DataFrame from the confusion matrix
cm_df = pd.DataFrame(cm, index=class_names, columns=class_names)

# Plot the confusion matrix as a heatmap
plt.figure(figsize=(10, 7))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.savefig('Confusion Matrix/confusion_matrix3.png')
plt.close()

# Generate the classification report
report = classification_report(y_true, y_pred_labels, target_names=class_names, output_dict=True)
report_df = pd.DataFrame(report).transpose()

# Save the classification report as a PNG image or as a CSV table
report_df.to_csv('Classification rapport/CNCC/classification_report.csv', index=True)

# Convert the classification report to a dictionary
report_dict = classification_report(y_true, y_pred_labels, target_names=class_names, output_dict=True)

TN = confusion_mat.sum(axis=0) - np.diag(confusion_mat)
FP = confusion_mat.sum(axis=1) - np.diag(confusion_mat)
FN = np.diag(confusion_mat) - confusion_mat.sum(axis=1)
TP = np.diag(confusion_mat)

# Specify the output file path for the JSON file
output_file = 'Classification rapport/CNCC/classification_report.json'

# Save the classification report as a JSON file
with open(output_file, 'w') as file:
    json.dump(report_dict, file, indent=4)


