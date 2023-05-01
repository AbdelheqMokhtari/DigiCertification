from keras.applications.resnet import ResNet50
from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
# import tensorflow as tf
import matplotlib.pyplot as plt

# physical_devices = tf.config.list_physical_devices('GPU')
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

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
num_classes = 7
num_epochs = 20
base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
x = base_model.output
x = GlobalAveragePooling2D()(x)
predictions = Dense(num_classes, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)
# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

# Say not to train first layer (ResNet) model as it is already trained
model.layers[0].trainable = False

# Train the model
history = model.fit(train_data, epochs=num_epochs, validation_data=validation_data, verbose=1)

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/ResNet50.h5')

# Create a graph of the training accuracy with respect to epoch values using a library like Matplotlib

train_accuracy = history.history['accuracy']
test_accuracy = history.history['val_accuracy']

plt.plot(train_accuracy, label='Training Accuracy')
plt.plot(test_accuracy, label='Test Accuracy')
plt.title('Accuracy vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.show()

plt.savefig('plot/accuracy_graph.png')

