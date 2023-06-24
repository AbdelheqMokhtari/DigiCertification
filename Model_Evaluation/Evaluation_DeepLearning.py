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
    'CCLS/Data/test',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

y_true = test_data.classes

# Load your saved model
model = keras.models.load_model('CCLS/ResNet50/ResNet50_epochs100_freeze_best_weight_model.h5')

# Retrieve the class names from the HDF5 file attributes
with h5py.File('CCLS/ResNet50/ResNet50_epochs100_freeze_best_weight_model.h5', 'r') as file:
    class_names = file.attrs['class_names']

# class_names = ['Avoine', 'Ble dur', 'ble tendre', 'orge', 'triticale']

# Make predictions on the test data
y_pred_prob = model.predict(test_data)

# Convert the predicted probabilities to labels
y_pred_labels = np.argmax(y_pred_prob, axis=1)

# Generate the confusion matrix
confusion_mat = confusion_matrix(y_true, y_pred_labels)

# Create a DataFrame from the confusion matrix
cm_df = pd.DataFrame(confusion_mat, index=class_names, columns=class_names)

# Plot the confusion matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Greens')
# sns.heatmap(cm_df, annot=True, fmt='d', cmap='Blues')
plt.xlabel('output class')
plt.ylabel('target class')
plt.title('Confusion Matrix')
plt.savefig('CCLS/ResNet50/ResNet50_epochs100_freeze_best_weight_confusion_matrix.png')
plt.close()

# Generate the classification report
report = classification_report(y_true, y_pred_labels, target_names=class_names, output_dict=True)
report_df = pd.DataFrame(report).transpose()

# Save the classification report as a PNG image or as a CSV table
report_df.to_csv(
    'CCLS/ResNet50/ResNet50_epochs100_freeze_best_weight_classification_report.csv',
    index=True
)

# Convert the classification report to a dictionary
report_dict = classification_report(y_true, y_pred_labels, target_names=class_names, output_dict=True)

# Calculate the true negatives (TN) for each class
num_classes = len(confusion_mat)
TN = []

for i in range(num_classes):
    mask = np.ones(num_classes, dtype=bool)
    mask[i] = False
    TN.append(np.sum(confusion_mat[mask][:, mask]))
for i, item in enumerate(TN):
    TN[i] = int(item)

# Calculate the true positives (TP) for each class
TP = np.diag(confusion_mat)

# Convert the NumPy array to a Python array
TP = TP.tolist()

# Calculate the false negatives (FN) for each class
num_classes = confusion_mat.shape[0]
FN = np.sum(confusion_mat, axis=1) - np.diag(confusion_mat)

FN = FN.tolist()


# Calculate the false positives (FP) for each class
num_classes = confusion_mat.shape[0]
FP = np.sum(confusion_mat, axis=0) - np.diag(confusion_mat)

FP = FP.tolist()
print(TP)
print(TN)
print(FP)
print(FN)
# specificity = TN / (TN + FP)
specificity = [TN / (TN + FP) for TN, FP in zip(TN, FP)]
# sensitivity = TP / (TP + FN)
sensitivity = [TP / (TP + FN) for TP, FN in zip(TP, FN)]
# accuracy (TP + TN) / (TP + TN + FP + FN)
accuracy = [TP / (TP + FN) for TP, TN, FP, FN in zip(TP, TN, FP, FN)]

print(specificity)
print(sensitivity)

# add specificity and sensitivity to a report dict
report_dict['specificity'] = specificity
report_dict['sensitivity'] = sensitivity
report_dict['TP'] = TP
report_dict['TN'] = TN
report_dict['FP'] = FP
report_dict['FN'] = FN

sensitivity_avg = sum(sensitivity) / len(sensitivity)
specificity_avg = sum(specificity) / len(specificity)
report_dict['sensitivity_avg'] = sensitivity_avg
report_dict['specificity_avg'] = specificity_avg
report_dict['accuracy_class'] = accuracy

# Specify the output file path for the JSON file
output_file = \
    'CCLS/ResNet50/ResNet50_epochs100_freeze_best_weight_classification_report.json'

# Save the classification report as a JSON file
with open(output_file, 'w') as file:
    json.dump(report_dict, file, indent=4)


# specificity = TN / (TN + FP)
# specificity = []
# for TN, FP in zip(TN, FP):
#    if (TN + FP) == 0:
#        spec = TN  # Set specificity to 0 or any desired default value
#    else:
#        spec = TN / (TN + FP)
#    specificity.append(spec)
# sensitivity = TP / (TP + FN)
# sensitivity = []
# for TP, FN in zip(TP, FN):
#    if (TP + FN) == 0:
#        spec = TP  # Set specificity to 0 or any desired default value
#    else:
#        spec = TP / (TP + FN)
#    sensitivity.append(spec)