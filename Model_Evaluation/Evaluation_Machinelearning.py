import joblib
import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.model_selection import train_test_split

# class_names = ["Bousselam", "GTA", "Oued el bared", "Vitron"]
class_names = ["Avoine", "Ble dur", "Ble tendre", "Orge", "Triticale"]
# class_names = ["ble dur", "Ble tendre", "casee", "echaudes", "maigre", "Metadine", "Mouchten", "piqee"]
# Load the SVM model
svm_model = joblib.load('CNCC/SVM/Features CNCC V1 Normalized.pkl')

# Load the test dataset
test_data = pd.read_csv('CNCC/Data/Features CNCC V1 Normalized.csv')

# Extract the features and labels from the test dataset
X = test_data.drop('label', axis=1)
y = test_data['label']

# Extract the training features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Predict the labels for the test dataset
y_pred = svm_model.predict(X_test)

print(y_pred)
# Calculate accuracy
accuracy = metrics.accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Calculate F1 score, precision, recall for each class
class_metrics = metrics.classification_report(y_test, y_pred, target_names=class_names, output_dict=True)
print('Classification Report:\n', class_metrics)

# Calculate confusion matrix
confusion_matrix = metrics.confusion_matrix(y_test, y_pred)
print('Confusion Matrix:\n', confusion_matrix)

# Create a DataFrame from the confusion matrix
cm_df = pd.DataFrame(confusion_matrix, index=class_names, columns=class_names)

# Save the confusion matrix as an image
plt.figure(figsize=(12, 10))
sns.heatmap(cm_df, annot=True, fmt='d', cmap='Greens')
plt.xlabel('Predicted labels')
plt.ylabel('True labels')
plt.title('Confusion Matrix')
plt.savefig('CNCC/SVM/confusion_matrix_CNCC_V1_Normalized.png')
plt.show()

# Calculate the true negatives (TN) for each class
num_classes = len(confusion_matrix)
TN = []

for i in range(num_classes):
    mask = np.ones(num_classes, dtype=bool)
    mask[i] = False
    TN.append(np.sum(confusion_matrix[mask][:, mask]))
for i, item in enumerate(TN):
    TN[i] = int(item)

# Calculate the true positives (TP) for each class
TP = np.diag(confusion_matrix)

# Convert the NumPy array to a Python array
TP = TP.tolist()

# Calculate the false negatives (FN) for each class
num_classes = confusion_matrix.shape[0]
FN = np.sum(confusion_matrix, axis=1) - np.diag(confusion_matrix)

FN = FN.tolist()


# Calculate the false positives (FP) for each class
num_classes = confusion_matrix.shape[0]
FP = np.sum(confusion_matrix, axis=0) - np.diag(confusion_matrix)

FP = FP.tolist()
print(TP)
print(TN)
print(FP)
print(FN)
# specificity = TN / (TN + FP)
specificity = [TN / (TN + FP) for TN, FP in zip(TN, FP)]
# sensitivity = TP / (TP + FN)
sensitivity = [TP / (TP + FN) for TP, FN in zip(TP, FN)]

accuracy = [(TP + TN) / (TP + TN + FP + FN) for TP, TN, FP, FN in zip(TP, TN, FP, FN)]

print(specificity)
print(sensitivity)

# add specificity and sensitivity to a report dict
class_metrics['specificity'] = specificity
class_metrics['sensitivity'] = sensitivity

class_metrics['TP'] = TP
class_metrics['TN'] = TN
class_metrics['FP'] = FP
class_metrics['FN'] = FN

sensitivity_avg = sum(sensitivity) / len(sensitivity)
specificity_avg = sum(specificity) / len(specificity)
class_metrics['sensitivity_avg'] = sensitivity_avg
class_metrics['specificity_avg'] = specificity_avg
class_metrics['accuracy_class'] = accuracy


# Save the classification report as a JSON file
with open('CNCC/SVM/Classification_report_CNCC_V1_Normalized.json', 'w') as json_file:
    json.dump(class_metrics, json_file)
