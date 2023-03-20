import cv2

# Charger l’image de blé
img = cv2.imread('test.JPG')

# Convertir l’image en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer un filtre de flou gaussien
blur = cv2.GaussianBlur(gray, (3, 3), 0)

# Appliquer un seuillage adaptatif pour binariser l’image
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV, 11, 4)
# Afficher l’image originale et l’image après traitement
cv2.imshow('Image originale', img)

cv2.imshow('Image après traitement', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()