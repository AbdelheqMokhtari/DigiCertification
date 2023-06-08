from keras.applications.resnet import ResNet50
from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=45)

test_datagen = ImageDataGenerator(rescale=1./255)

validation_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    'Data/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

test_data = test_datagen.flow_from_directory(
    'Data/test',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
validation_data = validation_datagen.flow_from_directory(
    'Data/validation',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

# Build the ResNet50 model
num_classes = 5
num_epochs = 2
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)
# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Say not to train first layer (ResNet) model as it is already trained
model.layers[0].trainable = True

# Train the model
history = model.fit(train_data, epochs=num_epochs, validation_data=validation_data, verbose=1)

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/New.h5')

# Create a graph of the training accuracy with respect to epoch values using a library like Matplotlib

train_accuracy = history.history['accuracy']
test_accuracy = history.history['val_accuracy']
epoch_values = np.arange(1, num_epochs+1)
# create a plot of training accuracy vs epoch values
fig, ax = plt.subplots()
ax.plot(epoch_values, train_accuracy, label='Training Accuracy')
ax.plot(epoch_values, test_accuracy, label='Validation Accuracy')
ax.set_xticks(np.arange(0, num_epochs+1, step=1))
ax.set_xlabel('Epoch')
ax.set_ylabel('Accuracy')
ax.set_title('Training and Validation Accuracy vs Epoch')
ax.legend(loc='lower right')
plt.show()

# Save the plot as a PNG image
# fig.savefig('accuracy_vs_epoch20.png', dpi=300, bbox_inches='tight')

# plt.plot(train_accuracy, label='Training Accuracy')
# plt.plot(test_accuracy, label='Test Accuracy')
# plt.title('Accuracy vs Epoch')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.legend(loc='lower right')
# plt.show()




