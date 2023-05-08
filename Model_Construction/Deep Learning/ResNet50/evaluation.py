from keras.preprocessing.image import ImageDataGenerator
import numpy as np
from tensorflow import keras
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score
# from sklearn.metrics import plot_confusion_matrix

test_datagen = ImageDataGenerator(rescale=1./255)

test_data = test_datagen.flow_from_directory(
    'Data/test',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

y_true = test_data.classes
print(y_true)

# Load your saved model
model = keras.models.load_model('Model/ResNet50New20.h5')

# Make predictions on the test data
y_pred_prob = model.predict(test_data)

# Convert the predicted probabilities to labels
y_pred = np.argmax(y_pred_prob, axis=1)
print(y_pred)
# Assuming y_true and y_pred are your true and predicted labels, respectively
cm = confusion_matrix(y_true, y_pred)

# Calculate the classification report, which includes precision, recall, and F1 score for each class
class_names = ['Avoine', 'Ble tendre', 'Bousselam', 'GTA', 'Orge', "Oued el bared", "Triticale", "Vitron"]
cr = classification_report(y_true, y_pred, target_names=class_names)

# Plot the confusion matrix
# disp = plot_confusion_matrix(model, test_data, test_data.classes, display_labels=class_names,
# cmap=plt.cm.Blues, normalize=None)
# disp.ax_.set_title("Confusion Matrix")
# plt.show()

# Create a heatmap visualization of the confusion matrix
plt.figure(figsize=(10, 10))
sns.heatmap(cm, annot=True, cmap='Blues', fmt='g')
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

# Save the plot to a file
plt.savefig('Evaluation/confusion_matrix.png')

# Calculate the overall accuracy
accuracy = accuracy_score(y_true, y_pred)

# Calculate the F1 score for each class
f1_scores = f1_score(y_true, y_pred, average=None)

print(cr)
print(accuracy)
print(f1_scores)

