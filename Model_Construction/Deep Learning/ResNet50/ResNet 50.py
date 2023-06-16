from keras.applications.resnet import ResNet50
from keras.layers import GlobalAveragePooling2D, Dense, Flatten
from keras.models import Model, Sequential
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import json
import h5py

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

# List of class names
# class_names = ['ble dur', 'Ble tendre', 'casee', 'echaudes', 'maigre', 'metadine', 'Mouchten', 'piqee']
class_names = ['Bousselam', 'GTA', 'Oued el bared', 'Vitron']
# class_names = ["ble dur", "Ble tendre", "casee", "echaudes", "maigre", "Metadine", "Mouchten", "piqee"]


def save_history_json(history, file_path):
    history_dict = history.history
    with open(file_path, 'w') as file:
        json.dump(history_dict, file)


# Define the callback to save the best weights
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    'callbacks/best_weights_ResNet50.h5',
    monitor='val_loss',  # Metric to monitor for saving the best weights
    save_best_only=True,
    save_weights_only=True,
    mode='min'  # or 'max' depending on the metric being monitored
)

train_datagen = ImageDataGenerator(rescale=1./255
                                   )

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
num_classes = 4
num_epochs = 100
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(128, activation='relu')(x)
x = Dense(64, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)
# predictions = Dense(num_classes, activation='softmax')(x)

# Create a new model by adding custom classification layers
# model = Sequential()
# model.add(base_model)
# model.add(Flatten())
# model.add(Dense(512, activation='relu'))
# model.add(Dense(256, activation='relu'))
# model.add(Dense(128, activation='relu'))
# model.add(Dense(num_classes, activation='softmax'))

# model = Model(inputs=base_model.input, outputs=predictions)
# Compile the model
model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Say not to train first layer (ResNet) model as it is already trained
# model.layers[0].trainable = True

# Freeze initial layers
for layer in base_model.layers:
    layer.trainable = False

# Unfreeze the last few layers for fine-tuning
num_layers_to_unfreeze = 5
for layer in model.layers[-num_layers_to_unfreeze:]:
    layer.trainable = True

# Train.txt the model
history = model.fit(train_data, epochs=num_epochs, validation_data=validation_data, verbose=1,
                    callbacks=[checkpoint_callback])

# Load the best weights after training
model.load_weights('callbacks/best_weights_ResNet50.h5')

save_history_json(history, 'history/CCLS/ResNet50/ResNet50_epochs100_unfreeze5_history_best_weight.json')

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/CCLS/ResNet50/ResNet50_epochs100_unfreeze5_best_weight_model.h5')

# Save class names as attributes of the HDF5 file
with h5py.File('Model/CCLS/ResNet50/ResNet50_epochs100_unfreeze5_best_weight_model.h5', 'a') as file:
    file.attrs['class_names'] = class_names


























# Create a graph of the training accuracy with respect to epoch values using a library like Matplotlib

# train_accuracy = history.history['accuracy']
# test_accuracy = history.history['val_accuracy']
# epoch_values = np.arange(1, num_epochs+1)
# create a plot of training accuracy vs epoch values
# fig, ax = plt.subplots()
# ax.plot(epoch_values, train_accuracy, label='Training Accuracy')
# ax.plot(epoch_values, test_accuracy, label='Validation Accuracy')
# ax.set_xticks(np.arange(0, num_epochs+1, step=1))
# ax.set_xlabel('Epoch')
# ax.set_ylabel('Accuracy')
# ax.set_title('Training and Validation Accuracy vs Epoch')
# ax.legend(loc='lower right')
# plt.show()

# Save the plot as a PNG image
# fig.savefig('accuracy_vs_epoch20.png', dpi=300, bbox_inches='tight')

# plt.plot(train_accuracy, label='Training Accuracy')
# plt.plot(test_accuracy, label='Test Accuracy')
# plt.title('Accuracy vs Epoch')
# plt.xlabel('Epoch')
# plt.ylabel('Accuracy')
# plt.legend(loc='lower right')
# plt.show()




