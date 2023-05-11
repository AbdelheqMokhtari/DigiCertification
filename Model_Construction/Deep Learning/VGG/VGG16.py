import tensorflow as tf
from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import VGG16, preprocess_input

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rescale=1./255,
    rotation_range=45
)

test_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rescale=1./255
)

validation_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rescale=1./255
)

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

num_classes = 8

base_model = VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(256, activation='relu')(x)
predictions = Dense(num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

# freeze the base DenseNet121 Model
for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer=Adam(lr=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(
    train_data,
    steps_per_epoch=train_data.n // train_data.batch_size,
    epochs=30,
    validation_data=validation_data,
    validation_steps=validation_data.n // validation_data.batch_size
)

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/VGG16epoch30.h5')