from sklearn.metrics import confusion_matrix
import numpy as np

# Load the model and test data
model = keras.models.load_model('model.h5')
X_test, y_test = load_test_data()

# Make predictions on the test data
y_pred = model.predict(X_test)

# Convert predictions to labels
y_pred = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)

# Compute the confusion matrix
labels = ['class_0', 'class_1', 'class_2', ... , 'class_n'] # list of class labels
cm = confusion_matrix(y_true, y_pred, labels=labels)

# Visualize the confusion matrix
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
