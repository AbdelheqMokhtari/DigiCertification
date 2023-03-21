from skimage.feature import graycomatrix, graycoprops
import numpy as np
import os
import cv2 as cv


# Define Image Path
image_dir = "Data"
files = os.listdir(image_dir)
for filename in files:
    # Loading image
    print("The image selected :", filename)
    filepath = os.path.join(image_dir, filename)
    img = cv.imread(filepath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Convert the image to a numpy array
    img_arr = np.array(gray)

    print("\nComputer the GLCM .... :\n")

    # Compute the GLCM
    glcm = graycomatrix(img_arr, distances=[1], angles=[0, np.pi / 4, np.pi / 2, 3 * np.pi / 4], levels=256,
                        symmetric=True, normed=True)

    # Compute the statistical measures
    asm = graycoprops(glcm, 'ASM')[0, 0]
    contrast = graycoprops(glcm, 'contrast')[0, 0]
    correlation = graycoprops(glcm, 'correlation')[0, 0]
    energy = graycoprops(glcm, 'energy')[0, 0]
    homogeneity = graycoprops(glcm, 'homogeneity')[0, 0]
    max_prob = np.max(glcm)

    print('asm: {:.2f}'.format(asm))
    print('contrast: {:.2f}'.format(contrast))
    print('Correlation: {:.2f}'.format(correlation))
    print('energy: {:.2f}'.format(energy))
    print('homogenity: {:.2f}'.format(homogeneity))
    print('max_prob: {:.2f}\n'.format(max_prob))

    # GLRM
    print("\nComputer the GLRM .... :\n")

    # Define the distances and angles for the GLRLM
    distances = [1, 2, 3, 4]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]

    # Calculate the GLRM
    glrlm = graycomatrix(img_arr, distances=distances, angles=angles, levels=256, symmetric=True, normed=True)

    # Calculate texture measures from the GLRLM
    contrast = graycoprops(glrlm, 'contrast')
    dissimilarity = graycoprops(glrlm, 'dissimilarity')
    homogeneity = graycoprops(glrlm, 'homogeneity')
    energy = graycoprops(glrlm, 'energy')
    correlation = graycoprops(glrlm, 'correlation')
    ASM = graycoprops(glrlm, 'ASM')

    # Print the texture measures
    # print("Contrast: ", contrast)
    for elements in contrast:
        for element in elements:
            print("Contrast: ", element)
    # print("Contrast: ", contrast[0][0])
    # print("Dissimilarity: ", dissimilarity)
    # print("Homogeneity: ", homogeneity)
    # print("Energy: ", energy)
    # print("Correlation: ", correlation)
    # print("ASM: ", ASM)
    break




