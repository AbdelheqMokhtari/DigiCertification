from skimage.feature import graycomatrix, graycoprops
import numpy as np
import os
import cv2 as cv
import pandas as pd

Columns = ["GLCM_ASM", "GLCM_Contrast", "GLCM_Correlation", "GLCM_Energy", "GLCM_Homogeneity", "GLCM_Max_Prob",
           "GLRM_Contrast_1_0", "GLRM_Contrast_1_45", "GLRM_Contrast_1_90", "GLRM_Contrast_1_135", "GLRM_Contrast_2_0",
           "GLRM_Contrast_2_45", "GLRM_Contrast_2_90", "GLRM_Contrast_2_135", "GLRM_Contrast_3_0", "GLRM_Contrast_3_45",
           "GLRM_Contrast_3_90", "GLRM_Contrast_3_135", "GLRM_Contrast_4_0", "GLRM_Contrast_4_45", "GLRM_Contrast_4_90",
           "GLRM_Contrast_4_135", "GLRM_Correlation_1_0", "GLRM_Correlation_1_45", "GLRM_Correlation_1_90",
           "GLRM_Correlation_1_135", "GLRM_Correlation_2_0",  "GLRM_Correlation_2_45", "GLRM_Correlation_2_90",
           "GLRM_Correlation_2_135", "GLRM_Correlation_3_0", "GLRM_Correlation_3_45", "GLRM_Correlation_3_90",
           "GLRM_Correlation_3_135", "GLRM_Correlation_4_0", "GLRM_Correlation_4_45", "GLRM_Correlation_4_90",
           "GLRM_Correlation_4_135", "GLRM_Energy_1_0", "GLRM_Energy_1_45", "GLRM_Energy_1_90", "GLRM_Energy_1_135",
           "GLRM_Energy_2_0",  "GLRM_Energy_2_45", "GLRM_Energy_2_90", "GLRM_Energy_2_135", "GLRM_Energy_3_0",
           "GLRM_Energy_3_45", "GLRM_Energy_3_90", "GLRM_Energy_3_135", "GLRM_Energy_4_0", "GLRM_Energy_4_45",
           "GLRM_Energy_4_90", "GLRM_Energy_4_135", "GLRM_Homogenity_1_0", "GLRM_Homogenity_1_45",
           "GLRM_Homogenity_1_90", "GLRM_Homogenity_1_135", "GLRM_Homogenity_2_0",  "GLRM_Homogenity_2_45",
           "GLRM_Homogenity_2_90", "GLRM_Homogenity_2_135", "GLRM_Homogenity_3_0", "GLRM_Homogenity_3_45",
           "GLRM_Homogenity_3_90", "GLRM_Homogenity_3_135", "GLRM_Homogenity_4_0", "GLRM_Homogenity_4_45",
           "GLRM_Homogenity_4_90", "GLRM_Homogenity_4_135", "GLRM_ASM_1_0", "GLRM_ASM_1_45",
           "GLRM_ASM_1_90", "GLRM_ASM_1_135", "GLRM_ASM_2_0",  "GLRM_ASM_2_45", "GLRM_ASM_2_90", "GLRM_ASM_2_135",
           "GLRM_ASM_3_0", "GLRM_ASM_3_45", "GLRM_ASM_3_90", "GLRM_ASM_3_135", "GLRM_ASM_4_0", "GLRM_ASM_4_45",
           "GLRM_ASM_4_90", "GLRM_ASM_4_135", "GLRM_Dissimilarity_1_0", "GLRM_Dissimilarity_1_45",
           "GLRM_Dissimilarity_1_90", "GLRM_Dissimilarity_1_135", "GLRM_Dissimilarity_2_0",  "GLRM_Dissimilarity_2_45",
           "GLRM_Dissimilarity_2_90", "GLRM_Dissimilarity_2_135", "GLRM_Dissimilarity_3_0", "GLRM_Dissimilarity_3_45",
           "GLRM_Dissimilarity_3_90", "GLRM_Dissimilarity_3_135", "GLRM_Dissimilarity_4_0", "GLRM_Dissimilarity_4_45",
           "GLRM_Dissimilarity_4_90", "GLRM_Dissimilarity_4_135"]

df = pd.DataFrame(columns=Columns)
print(df.shape)
# Define Image Path
image_dir = "Data"
files = os.listdir(image_dir)
for filename in files:
    # Loading image
    print("The image selected :", filename)
    filepath = os.path.join(image_dir, filename)
    img = cv.imread(filepath)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # initialise an empty list to store all Feature of the image
    Features = []

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

    Features.append(asm)
    print('asm: {:.2f}'.format(asm))

    Features.append(contrast)
    print('contrast: {:.2f}'.format(contrast))

    Features.append(correlation)
    print('Correlation: {:.2f}'.format(correlation))

    Features.append(energy)
    print('energy: {:.2f}'.format(energy))

    Features.append(homogeneity)
    print('homogenity: {:.2f}'.format(homogeneity))

    Features.append(max_prob)
    print('max_prob: {:.2f}\n'.format(max_prob))

    # GLRM
    print("\nComputer the GLRM .... :\n")

    # Define the distances and angles for the GLRLM
    distances = [1, 2, 3, 4]
    angles = [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4]
    text = [0, 45, 90, 135]

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
    print("Calculating Contrast ...\n")
    for i, elements in enumerate(contrast):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Contrast GLRM with distance of ", i+1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Correlation ...\n")
    for i, elements in enumerate(correlation):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Correlation GLRM with distance of ", i+1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Energy ...\n")
    for i, elements in enumerate(energy):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Energy GLRM with distance of ", i+1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Homogeneity ...\n")
    for i, elements in enumerate(homogeneity):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Homogeneity GLRM with distance of ", i+1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating ASM ...\n")
    for i, elements in enumerate(ASM):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("ASM GLRM with distance of ", i+1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Dissimilarity ...\n")
    for i, elements in enumerate(dissimilarity):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Dissimilarity GLRM with distance of ", i+1, "and angle of ", angle, "Degree = ", element)

    print("******************************************************************************************************\n")
    print(len(Features))
    df.loc[len(df)] = Features

print(df)
print(df.shape)
df.to_csv('Texture_Feature.csv', index=False)





