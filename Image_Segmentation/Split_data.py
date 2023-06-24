from sklearn.model_selection import train_test_split
import os
import shutil

# Define the path to the directory containing all images
path_to_images = 'Crop images'

# Define the list of classes
classes = ["Ble dur", "Ble tendre", "casee", "echaudes", "maigre", "Metadine"]

# Create the directories for train and test data
os.makedirs('Data/train')
os.makedirs('Data/test')
os.makedirs('Data/validation')

# Loop over each class and split the images into train and test data
for class_name in classes:
    # Find all images belonging to the current class
    class_path = os.path.join(path_to_images, class_name)
    images = os.listdir(class_path)
    # Split the images into train and test data
    train_images, test_images = train_test_split(images, test_size=0.2, random_state=42)
    validation_images, test_images = train_test_split(test_images, test_size=0.5, random_state=42)
    # Move the train images to the train directory
    train_dir = os.path.join('Data/train', class_name)
    os.makedirs(train_dir)
    for image_name in train_images:
        src_path = os.path.join(class_path, image_name)
        dst_path = os.path.join(train_dir, image_name)
        shutil.copy(src_path, dst_path)
    # Move the test images to the test directory
    test_dir = os.path.join('Data/test', class_name)
    os.makedirs(test_dir)
    for image_name in test_images:
        src_path = os.path.join(class_path, image_name)
        dst_path = os.path.join(test_dir, image_name)
        shutil.copy(src_path, dst_path)

    # Move the train images to the Validation directory
    Validation_dir = os.path.join('Data/validation', class_name)
    os.makedirs(Validation_dir)
    for image_name in validation_images:
        src_path = os.path.join(class_path, image_name)
        dst_path = os.path.join(Validation_dir, image_name)
        shutil.copy(src_path, dst_path)