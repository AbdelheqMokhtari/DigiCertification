import cv2
import numpy as np
import darknet

# Load YOLO model
net = darknet.load_net("yolov4.cfg", "yolov4.weights")
meta = darknet.load_meta("coco.data")

# Load image
image = cv2.imread("GTA001.jpg")

# Convert image to Darknet format
image_darknet = darknet.make_image(image.shape[1], image.shape[0], 3)
darknet.copy_image_from_bytes(image_darknet, image.tobytes())

# Perform object detection
detections = darknet.detect_image(net, meta, image_darknet)

# Crop detected objects
for detection in detections:
    class_name = detection[0].decode()
    confidence = detection[1]
    x, y, w, h = detection[2]

    # Crop object
    crop = image[int(y-h/2):int(y+h/2), int(x-w/2):int(x+w/2)]

    # Save cropped object
    cv2.imwrite(f"Save/{class_name}.jpg", crop)
