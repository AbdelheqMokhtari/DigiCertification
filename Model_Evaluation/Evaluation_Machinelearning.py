import joblib
import numpy as np
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
import json
from sklearn.model_selection import train_test_split

# class_names = ["Bousselam", "GTA", "Oued el bared", "Vitron"]
# class_names = ["Avoine", "Ble dur", "Ble tendre", "Orge", "Triticale"]
class_names = ["ble dur", "Ble tendre", "casee", "echaudes", "maigre", "Metadine", "Mouchten", "piqee"]
# Load the SVM model
svm_model = joblib.load('CCLS/Model/SVM/Features CCLS V1 Normalized.pkl')

# Load the test dataset
test_data = pd.read_csv('CCLS/Data/Features CCLS V1 Normalized.csv')

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
plt.savefig('CCLS/Confusion Matrix/SVM/confusion_matrix_CCLS_V1_Normalized.png')
plt.show()

# Save the classification report as a JSON file
with open('CCLS/Classification report/SVM/Classification_report_CCLS_V1_Normalized.json', 'w') as json_file:
    json.dump(class_metrics, json_file)
