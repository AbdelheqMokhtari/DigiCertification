import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

# Load the trained KNN classifier from a file
knn = joblib.load('knn_classifier.pkl')

# Load the testing dataset from a CSV file
test_data = pd.read_csv('Features Final.csv')  # Replace 'testing_dataset.csv' with the actual filename

# Separate the features (X_test) and the class labels (y_test)
X_test = test_data.iloc[:, :-1].values
y_test = test_data.iloc[:, -1].values

# Predict the class labels for the test set
y_pred = knn.predict(X_test)

# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

# Print the evaluation metrics
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# Compare y_pred and y_test
print("Actual Class Labels:", y_test)
print("Predicted Class Labels:", y_pred)
print(test_data['label'].value_counts())




