import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('Features/Features V1.csv')
data = data.reset_index()
X = data.drop('label', axis=1)  # X contains the features
y = data['label']  # y contains the labels
print("test")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = SVC(kernel='linear', C=11, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {acc}")
print(f"Confusion matrix:\n{cm}")

# Use a feature selection algorithm to select the best features
selector = SelectKBest(f_classif, k=20)
X_train_selected = selector.fit_transform(X_train, y_train)

# Evaluate the performance of the SVM model on the test set using the selected features
model.fit(X_train_selected, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
print(f"Accuracy: {acc}")
print(f"Confusion matrix:\n{cm}")

# Evaluate the performance of the SVM model on the test set using the selected features
score = model.score(X_train_selected, y_test)

print("Score:", score)