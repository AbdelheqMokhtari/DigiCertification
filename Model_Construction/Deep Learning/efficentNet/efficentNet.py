import json
import h5py
import tensorflow as tf
from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.efficientnet import EfficientNetB7

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

# List of class names
class_names = ['Avoine', 'Ble dur', 'ble tendre', 'orge', 'triticale']


def save_history_json(history, file_path):
    history_dict = history.history
    with open(file_path, 'w') as file:
        json.dump(history_dict, file)


# Define the callback to save the best weights
checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    'callbacks/best_weights.h5',
    monitor='val_loss',  # Metric to monitor for saving the best weights
    save_best_only=True,
    save_weights_only=True,
    mode='min'  # or 'max' depending on the metric being monitored
)

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   rotation_range=45)

test_datagen = ImageDataGenerator(rescale=1. / 255)

validation_datagen = ImageDataGenerator(rescale=1. / 255)

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

num_classes = 5

base_model = EfficientNetB7(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation='relu')(x)
x = Dense(256, activation='relu')(x)
x = Dense(128, activation='relu')(x)
x = Dense(64, activation='relu')(x)
x = Dense(32, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# freeze the base DenseNet121 Model
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

# Unfreeze the last few layers for fine-tuning
# num_layers_to_unfreeze = 5
# for layer in model.layers[-num_layers_to_unfreeze:]:
#    layer.trainable = True

history = model.fit(
    train_data,
    steps_per_epoch=train_data.n // train_data.batch_size,
    epochs=50,
    validation_data=validation_data,
    validation_steps=validation_data.n // validation_data.batch_size,
    callbacks=[checkpoint_callback]
)

save_history_json(history, 'history/CNCC/efficentNet_V2/efficentNet_V2_epochs50_unfreeze5_history.json')

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/CNCC/efficentNet/efficentNet_epochs50_unfreeze5_model.h5')

# Save class names as attributes of the HDF5 file
with h5py.File('Model/CNCC/efficentNet/efficentNet_epochs50_freeze_model.h5', 'a') as file:
    file.attrs['class_names'] = class_names

