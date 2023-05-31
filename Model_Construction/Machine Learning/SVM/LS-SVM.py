import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, mean_squared_error, confusion_matrix, classification_report, \
    mean_absolute_error, r2_score
from sklearn.svm import SVR

# Step 1: Load the CSV file
data = pd.read_csv('Features/Features Final.csv')

# Separate features and labels
X = data.drop('label', axis=1)
y = data['label']

# Step 2: Preprocess the data
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Step 3: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the LS-SVM classifier
model = SVR(kernel='linear', C=10)
model.fit(X_train, y_train)

# Step 5: Predict class labels
y_pred = model.predict(X_test)
print(y_test)
print(y_pred)

# Step 6: Evaluate the classifier
total_samples = len(y_test)
correct_predictions = 0

for true_label, pred_label in zip(y_test, y_pred):
    if true_label == pred_label:
        correct_predictions += 1

accuracy = correct_predictions / total_samples
print(f"Accuracy: {accuracy}")

# confusion_mat = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:")
# print(confusion_mat)

# classification_rep = classification_report(y_test, y_pred)
# print("Classification Report:")
# print(classification_rep)

# Regression Evaluation
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

# Step 7: Fine-tune the model if needed
# You can adjust the hyperparameters or explore different kernels to improve performance
