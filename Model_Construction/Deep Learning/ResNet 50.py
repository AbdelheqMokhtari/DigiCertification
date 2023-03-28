from keras.applications.resnet import ResNet50
from keras.layers import GlobalAveragePooling2D, Dense
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale=1./255)

test_datagen = ImageDataGenerator(rescale=1./255)

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

# Build the ResNet50 model
num_classes = 2
num_epochs = 32
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
model.fit(train_data, epochs=num_epochs)

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/my_model.h5')
