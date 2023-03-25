import os
from PIL import Image

j = 0
image_dir = "Black_image"
files = os.listdir(image_dir)
for filename in files:
    filepath = os.path.join(image_dir, filename)

    # Open image and get dimensions
    img = Image.open(filepath)
    width, height = img.size

    # Create new blank image with 256x256 dimensions
    new_img = Image.new("RGB", (256, 256), (0, 0, 0))

    # Calculate the size of the resized image and center the original image on it
    if width > height:
        ratio = 256 / width
        new_width = 256
        new_height = int(height * ratio)
        y_offset = (256 - new_height) // 2
        x_offset = 0
    else:
        ratio = 256 / height
        new_height = 256
        new_width = int(width * ratio)
        x_offset = (256 - new_width) // 2
        y_offset = 0

    # Resize the original image and paste it into the new image
    resized_img = img.resize((new_width, new_height))
    new_img.paste(resized_img, (x_offset, y_offset))

    # Save the new image
    print(j)
    new_img.save(f'Resized Image/seed_{j}.png')
    j += 1
