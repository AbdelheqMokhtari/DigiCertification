import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from imblearn.combine import SMOTEENN
from collections import Counter
import joblib

scaler = StandardScaler()
data = pd.read_csv('Features CNCC V1.csv')
data = data.dropna()
print(data.shape)
X = data.drop('label', axis=1)  # X contains the features

y = data['label']  # y contains the labels

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = SVC(kernel='linear', C=11, random_state=42)

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc}\n")

f1 = f1_score(y_test, y_pred, average=None)
print(f'f1 score {f1}\n')

# Save the trained model to a file
joblib.dump(model, 'Model/Features CNCC V1 Scaled.pkl')

