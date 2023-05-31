from keras.layers import Input, Conv2D, BatchNormalization, Activation, MaxPooling2D, Add, AveragePooling2D, Flatten, \
    Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf


# Define the ResNet building blocks
def convolutional_block(x, filters, strides=1):
    shortcut = x

    # First block
    x = Conv2D(filters, kernel_size=(3, 3), strides=strides, padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    # Second block
    x = Conv2D(filters, kernel_size=(3, 3), padding='same')(x)
    x = BatchNormalization()(x)

    # Shortcut connection
    shortcut = Conv2D(filters, kernel_size=(1, 1), strides=strides, padding='same')(shortcut)
    shortcut = BatchNormalization()(shortcut)

    x = Add()([x, shortcut])
    x = Activation('relu')(x)

    return x


def identity_block(x, filters):
    shortcut = x

    # First block
    x = Conv2D(filters, kernel_size=(3, 3), padding='same')(x)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)

    # Second block
    x = Conv2D(filters, kernel_size=(3, 3), padding='same')(x)
    x = BatchNormalization()(x)

    x = Add()([x, shortcut])
    x = Activation('relu')(x)

    return x


# Build the ResNet-18 model
def build_resnet18(input_shape, num_classes):
    input_layer = Input(shape=input_shape)

    # Initial conv layer
    x = Conv2D(64, kernel_size=(7, 7), strides=(2, 2), padding='same')(input_layer)
    x = BatchNormalization()(x)
    x = Activation('relu')(x)
    x = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)

    # ResNet blocks
    x = convolutional_block(x, filters=64)
    x = identity_block(x, filters=64)
    x = identity_block(x, filters=64)

    x = convolutional_block(x, filters=128, strides=2)
    x = identity_block(x, filters=128)
    x = identity_block(x, filters=128)

    x = convolutional_block(x, filters=256, strides=2)
    x = identity_block(x, filters=256)
    x = identity_block(x, filters=256)

    x = convolutional_block(x, filters=512, strides=2)
    x = identity_block(x, filters=512)
    x = identity_block(x, filters=512)

    # Final layers
    x = AveragePooling2D(pool_size=(7, 7))(x)
    x = Flatten()(x)
    x = Dense(num_classes, activation='softmax')(x)

    model = Model(inputs=input_layer, outputs=x)

    return model


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
# Set the input shape and number of classes
input_shape = (224, 224, 3)
num_classes = 5  # Replace with the actual number of classes in your dataset

# Build the ResNet-18 model
model = build_resnet18(input_shape, num_classes)

# Compile the model
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])


# Train the model
history = model.fit(train_data, epochs=30, validation_data=validation_data, verbose=1)

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/ResNet18epoch30NoVarieties.h5')

