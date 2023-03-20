import cv2

img =cv2.imread('test.JPG')

#  Appliquer un filtre de flou Gaussian
bb = cv2.GaussianBlur(img, (3, 3), 0)
# Afficher l’image originale et l’image après traitement
cv2.imshow('Image originale', img)
cv2.imshow('Image après gaussian', bb)

#  Appliquer un filtre de median
filtered_img = cv2.medianBlur(img, 3)

# Afficher l’image originale et l’image après traitement

cv2.imshow('Image après median', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

