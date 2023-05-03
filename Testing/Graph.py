import matplotlib.pyplot as plt

history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
train_accuracy = history.history['accuracy']
test_accuracy = history.history['val_accuracy']

plt.plot(train_accuracy, label='Training Accuracy')
plt.plot(test_accuracy, label='Test Accuracy')
plt.title('Accuracy vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()
plt.savefig('accuracy_graph.png')

