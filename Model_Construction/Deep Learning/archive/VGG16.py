from keras.applications.vgg16 import VGG16
from keras.layers import Dropout
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam

train_datagen = ImageDataGenerator(rescale=1./255)

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

num_epochs = 20
vgg_conv = VGG16(weights='imagenet')
# vgg_conv = VGG16(weights=None, include_top=False, input_shape=(64, 64, 3))
# vgg_conv.load_weights('../input/vgg16/vgg16_weights_tf_dim_ordering_tf_kernels_notop.h5')

for layer in vgg_conv.layers[:-4]:
    layer.trainable = False

model = Sequential()
model.add(vgg_conv)

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax'))

model.summary()


model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(train_data, epochs=num_epochs, validation_data=validation_data, verbose=1)

# Evaluate the model
model.evaluate(test_data)

# Save the model
model.save('Model/VGG16.h5')