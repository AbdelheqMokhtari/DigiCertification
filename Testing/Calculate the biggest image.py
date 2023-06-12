import cv2
import os

# Define the path to the directory containing all images
path_to_images = 'Crop images'

# Define the list of classes
classes = ["Bousselam", "GTA", "Oued el bared", "Vitron"]
max_height = 0
max_width = 0

# Loop over each class and split the images into train and test data
for class_name in classes:
    # Find all images belonging to the current class
    class_path = os.path.join(path_to_images, class_name)
    images = os.listdir(class_path)
    for image in images:
        image_path = os.path.join(class_path, image)
        img = cv2.imread(image_path)
        height, width = img.shape[:2]
        if height > max_height:
            filename = image_path
        if width > max_width:
            filename2 = image_path
        max_height = max(max_height, height)
        max_width = max(max_width, width)

print(max_width)
print(max_height)
print(filename2)
print(filename)
