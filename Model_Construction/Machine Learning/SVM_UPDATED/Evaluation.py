import pickle
import cv2 as cv
import numpy as np
import pandas as pd
import os
from scipy.stats import skew, kurtosis, entropy
import pywt
from skimage.feature import graycomatrix, graycoprops
import joblib
import pandas as pd
import cv2
from skimage.filters import median
from scipy.ndimage import gaussian_filter

# Load the pickled SVM model
with open('Model/New Features CCLS V1 Final.pkl', 'rb') as file:
    model = pickle.load(file)
model_SVM = joblib.load('Model/New Features CCLS V1 Final.pkl')

columns = ["Height", "Width", "area", "perimeter", "circularity", "aspect_ratio", "solidity", 'SF1', 'SF2', 'SF3',
           'SF4', "Rectangularity", "MeanB", "MeanG", "MeanR", "std_Blue", "std_Green", "std_Red", "skew_Blue",
           "skew_Green", "skew_Red", "kurtosis_Blue", "kurtosis_Green", "kurtosis_Red", "entropy_Blue",
           "entropy_Green", "entropy_Red", "Wavelet_Blue", "Wavelet_Green", "Wavelet_Red", "MeanHue", "MeanSaturation",
           "MeanValue", "std_Hue", "std_Saturation", "std_Value", "skew_Hue", "skew_Saturation", "skew_Value",
           "kurtosis_Hue", "kurtosis_Saturation", "kurtosis_Value", "entropy_Hue", "entropy_Saturation",
           "entropy_Value", "Wavelet_Hue", "Wavelet_Saturation", "Wavelet_Value", "MeanL", "MeanA", "MeanB.1", "std_L",
           "std_A", "std_B", "skew_L", "skew_A", "skew_B", "kurtosis_L", "kurtosis_A", "kurtosis_B", "entropy_L",
           "entropy_A", "entropy_B", "Wavelet_L", "Wavelet_A", "Wavelet_B", "MeanYB", "MeanCB", "MeanCR", "std_YB",
           "std_CB", "std_CR", "skew_YB", "skew_CB", "skew_CR", "kurtosis_YB", "kurtosis_CB", "kurtosis_CR",
           "entropy_YB", "entropy_CB", "entropy_CR", "Wavelet_YB", "Wavelet_CB", "Wavelet_CR", "MeanX", "MeanY",
           "MeanZ", "std_X", "std_Y", "std_Z", "skew_X", "skew_Y", "skew_Z", "kurtosis_X", "kurtosis_Y", "kurtosis_Z",
           "entropy_X", "entropy_Y", "entropy_Z", "Wavelet_X", "Wavelet_Y", "Wavelet_Z", "GLCM_ASM", "GLCM_Contrast",
           "GLCM_Correlation", "GLCM_Energy", "GLCM_Homogeneity", "GLCM_Max_Prob", "GLRM_Contrast_1_0",
           "GLRM_Contrast_1_45", "GLRM_Contrast_1_90", "GLRM_Contrast_1_135", "GLRM_Contrast_2_0", "GLRM_Contrast_2_45",
           "GLRM_Contrast_2_90", "GLRM_Contrast_2_135", "GLRM_Contrast_3_0", "GLRM_Contrast_3_45", "GLRM_Contrast_3_90",
           "GLRM_Contrast_3_135", "GLRM_Contrast_4_0", "GLRM_Contrast_4_45", "GLRM_Contrast_4_90",
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
df = pd.DataFrame(columns=columns)

image = cv2.imread("Images/Metadine_1.jpeg")

cv2.imshow("yo ", image)
cv2.waitKey(0)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filtered_image_median = median(gray, behavior='adaptive', mode='reflect')

# Apply adaptive Gaussian filter
filtered_image_guassian = gaussian_filter(filtered_image_median, sigma=3)

# Apply Otsu's method to automatically determine the threshold value
thresh_val, thresh_img = cv2.threshold(filtered_image_guassian, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Use the optimal threshold for Canny edge detection
edges = cv2.Canny(filtered_image_guassian, threshold1=0.5 * thresh_val, threshold2=thresh_val)

combined = cv2.bitwise_or(thresh_img, edges)

# Find contours in the binary image
contours, hierarchy = cv2.findContours(combined, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total_number = 0
# Filter out small contours and draw the remaining contours on the original image

crop_image = []
for contour in contours:
    if cv2.contourArea(contour) > 2000:
        total_number += 1
        # Minimum area threshold
        # Get the bounding box coordinates
        x, y, w, h = cv2.boundingRect(contour)
        print("Area =", cv2.contourArea(contour), "x =", x, "y =", y, "w =", w, "h =", h)

        crop_img = image[y:(y + h), x:(x + w)]
        # Get the original height and width of the image
        height, width = crop_img.shape[:2]

        # Set the desired output size
        output_size = 290  # CCLS dataset
        # output_size = 630  # CNCC dataset
        # Calculate the amount of padding needed on each side
        h_pad = max(0, (output_size - height) // 2)
        w_pad = max(0, (output_size - width) // 2)

        # Add the padding using copyMakeBorder() function
        output_img = cv2.copyMakeBorder(crop_img, h_pad, h_pad, w_pad, w_pad, cv2.BORDER_CONSTANT,
                                        value=(0, 0,
                                               0))

        # crop image
        crop_image.append(output_img)


for image in crop_image:
    cv2.imshow("Hello ", image)
    cv2.waitKey(0)

    # initialise an empty list to store all Feature of the image
    Features = []

    # convert image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Threshold the image to binary
    _, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

    # Find the contours of the wheat plant
    contours, _ = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Find the contour with the largest area (which should be the wheat plant)
    max_contour = max(contours, key=cv.contourArea)
    # Get the bounding box of the contour
    x, y, w, h = cv.boundingRect(max_contour)

    height = h
    width = w
    area = cv.contourArea(max_contour)
    perimeter = cv.arcLength(max_contour, True)
    circularity = (4 * np.pi * area) / (perimeter * perimeter)
    aspect_ratio = float(w) / h
    solidity = area / cv.contourArea(cv.convexHull(max_contour))

    # Calculate the minimum bounding rectangle (MBR) of the object
    _, _, width, height = cv.boundingRect(max_contour)
    mbr_area = width * height

    # Calculate Rectangularity
    Re = area / mbr_area

    # Calculate Shape Factor 1 (SF1)
    sf1 = area / (perimeter ** 2)

    # Calculate Shape Factor 2 (SF2)
    sf2 = (perimeter ** 2) / area

    # Calculate Shape Factor 3 (SF3)
    sf3 = perimeter / np.sqrt(area)

    # Calculate Feret's diameter
    (x, y), (width, height), angle = cv.minAreaRect(max_contour)
    if width > height:
        feret_diameter = width
    else:
        feret_diameter = height

    # Calculate Shape Factor 4 (SF4)
    sf4 = area / (feret_diameter ** 2)

    Features.append(height)
    print(f"Kernel Height: {height}")

    Features.append(width)
    print(f"Kernel Width: {width}")

    Features.append(area)
    print(f"Kernel Area: {area}")

    Features.append(perimeter)
    print(f"Kernel Perimeter: {perimeter}")

    Features.append(circularity)
    print(f"Kernel Circularity: {circularity}")

    Features.append(aspect_ratio)
    print(f"Kernel Aspect_ratio: {aspect_ratio}")

    Features.append(solidity)
    print(f"Kernel Solidity: {solidity}")

    Features.append(Re)
    print(f"Kernel Rectangularity : {Re}")

    Features.append(sf1)
    print(f"Shape factor 1: {sf1}")

    Features.append(sf2)
    print(f"Shape factor 2: {sf2}")

    Features.append(sf3)
    print(f"Shape factor 3: {sf3}")

    Features.append(sf4)
    print(f"Shape factor 4: {sf4}")
    print(
        "*******************************************************************************************************\n")

    # RGB Space Color
    print("\nRGB Color Feature Extraction :\n")
    img_array = np.array(image)

    # Split the image into color channels
    b, g, r = cv.split(image)

    # Calculate the mean of each color component (RGB)
    mean = np.mean(img_array, axis=(0, 1))
    MeanB = mean[0]
    MeanG = mean[1]
    MeanR = mean[2]

    Features.append(MeanB)
    print('Mean R: {:.2f}'.format(MeanB))

    Features.append(MeanG)
    print('Mean G: {:.2f}'.format(MeanG))

    Features.append(MeanR)
    print('Mean B: {:.2f}'.format(MeanR))

    # Calculate the standard deviation of each color component (RGB)
    std_dev = np.std(img_array, axis=(0, 1))
    std_Blue = std_dev[0]
    std_Green = std_dev[1]
    std_Red = std_dev[2]

    Features.append(std_Blue)
    print('Standard Deviation B: {:.2f}'.format(std_Blue))

    Features.append(std_Green)
    print('Standard Deviation G: {:.2f}'.format(std_Green))

    Features.append(std_Red)
    print('\nStandard Deviation R: {:.2f}'.format(std_Red))

    # Calculate the skewness of each color component (RGB)
    skew_Blue = skew(b.flatten())
    skew_Green = skew(g.flatten())
    skew_Red = skew(r.flatten())

    Features.append(skew_Blue)
    print('Skewness B: {:.2f}'.format(skew_Blue))

    Features.append(skew_Green)
    print('Skewness G: {:.2f}'.format(skew_Green))

    Features.append(skew_Red)
    print('\nSkewness R: {:.2f}'.format(skew_Red))

    # Calculate the kurtosis of each color component (RGB)
    kurtosis_Blue = kurtosis(b.flatten())
    kurtosis_Green = kurtosis(g.flatten())
    kurtosis_Red = kurtosis(r.flatten())

    Features.append(kurtosis_Blue)
    print('kurtosis B: {:.2f}'.format(kurtosis_Blue))

    Features.append(kurtosis_Red)
    print('\nkurtosis R: {:.2f}'.format(kurtosis_Red))

    Features.append(kurtosis_Green)
    print('kurtosis G: {:.2f}'.format(kurtosis_Green))

    # Compute the probability distribution of each color channel
    hist_b = cv.calcHist([b], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_g = cv.calcHist([g], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_r = cv.calcHist([r], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])

    # Compute the entropy of each color channel
    entropy_B = entropy(hist_b, base=2)
    entropy_G = entropy(hist_g, base=2)
    entropy_R = entropy(hist_r, base=2)

    entropy_Blue = float(entropy_B[0])
    entropy_Green = float(entropy_G[0])
    entropy_Red = float(entropy_R[0])

    Features.append(entropy_Blue)
    print('entropy B: {:.2f}'.format(entropy_Blue))

    Features.append(entropy_Green)
    print('entropy G: {:.2f}'.format(entropy_Green))

    Features.append(entropy_Red)
    print('\nentropy R: {:.2f}'.format(entropy_Red))

    # Perform one-level DWT using db4 wavelet for the three component
    coefficient_b = pywt.dwt2(b, 'db4')
    coefficient_g = pywt.dwt2(g, 'db4')
    coefficient_r = pywt.dwt2(r, 'db4')

    # Get the approximation coefficients (LL) and Take the mean of the LL coefficients
    LL, (LH, HL, HH) = coefficient_b
    Wavelet_Blue = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_g
    Wavelet_Green = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_r
    Wavelet_Red = np.mean(LL)

    Features.append(Wavelet_Blue)
    print('\nWavelet_Blue R: {:.2f}'.format(Wavelet_Blue))

    Features.append(Wavelet_Green)
    print('\nWavelet_Green R: {:.2f}'.format(Wavelet_Green))

    Features.append(Wavelet_Red)
    print('\nWavelet_Red R: {:.2f}'.format(Wavelet_Red))

    # HSV space Color
    print(
        "--------------------------------------------------------------------------------------------------------\n"
        "HSV Color Feature Extraction :\n")

    hsv_img = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hsv_array = np.array(hsv_img)

    # Split the image into color channels
    h, s, v = cv.split(hsv_img)

    # Calculate the mean of each color component (HSV)
    mean_hsv = np.mean(hsv_array, axis=(0, 1))
    MeanHue = mean_hsv[0]
    MeanSaturation = mean_hsv[1]
    MeanValue = mean_hsv[2]

    Features.append(MeanHue)
    print('Mean H: {:.2f}'.format(MeanHue))

    Features.append(MeanSaturation)
    print('Mean S: {:.2f}'.format(MeanSaturation))

    Features.append(MeanValue)
    print('Mean V: {:.2f}'.format(MeanValue))

    # Calculate the standard deviation of each color component (HSV)
    std_dev = np.std(hsv_array, axis=(0, 1))
    std_Hue = std_dev[0]
    std_Saturation = std_dev[1]
    std_Value = std_dev[2]

    Features.append(std_Hue)
    print('\nStandard Deviation Hue: {:.2f}'.format(std_Hue))

    Features.append(std_Saturation)
    print('Standard Deviation Saturation: {:.2f}'.format(std_Saturation))

    Features.append(std_Value)
    print('Standard Deviation Value: {:.2f}'.format(std_Value))

    # Calculate the skewness of each color component (HSV)
    skew_Hue = skew(h.flatten())
    skew_Saturation = skew(s.flatten())
    skew_Value = skew(v.flatten())

    Features.append(skew_Hue)
    print('\nSkewness Hue: {:.2f}'.format(skew_Hue))

    Features.append(skew_Saturation)
    print('Skewness Saturation: {:.2f}'.format(skew_Saturation))

    Features.append(skew_Value)
    print('Skewness Value: {:.2f}'.format(skew_Value))

    # Calculate the kurtosis of each color component (HSV)
    kurtosis_Hue = kurtosis(h.flatten())
    kurtosis_Saturation = kurtosis(s.flatten())
    kurtosis_Value = kurtosis(v.flatten())

    Features.append(kurtosis_Hue)
    print('\nKurtosis Hue: {:.2f}'.format(kurtosis_Hue))

    Features.append(kurtosis_Saturation)
    print('Kurtosis Saturation: {:.2f}'.format(kurtosis_Saturation))

    Features.append(kurtosis_Value)
    print('Kurtosis Value: {:.2f}'.format(kurtosis_Value))

    # Compute the probability distribution of each color channel
    hist_h = cv.calcHist([h], [0], None, [180], [0, 180]) / (image.shape[0] * image.shape[1])
    hist_s = cv.calcHist([s], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_v = cv.calcHist([v], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])

    # Compute the entropy of each color channel
    entropy_h = entropy(hist_h, base=2)
    entropy_s = entropy(hist_s, base=2)
    entropy_v = entropy(hist_v, base=2)

    entropy_Hue = float(entropy_h[0])
    entropy_Saturation = float(entropy_s[0])
    entropy_Value = float(entropy_v[0])

    Features.append(entropy_Hue)
    print('\nentropy Hue: {:.2f}'.format(entropy_Hue))

    Features.append(entropy_Saturation)
    print('entropy Saturation: {:.2f}'.format(entropy_Saturation))

    Features.append(entropy_Value)
    print('entropy Value: {:.2f}'.format(entropy_Value))

    # Perform one-level DWT using db4 wavelet for the three component
    coefficient_h = pywt.dwt2(h, 'db4')
    coefficient_s = pywt.dwt2(s, 'db4')
    coefficient_v = pywt.dwt2(v, 'db4')

    # Get the approximation coefficients (LL) and Take the mean of the LL coefficients for the three component
    LL, (LH, HL, HH) = coefficient_h
    Wavelet_Hue = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_s
    Wavelet_Saturation = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_v
    Wavelet_Value = np.mean(LL)

    Features.append(Wavelet_Hue)
    print('\nWavelet_Hue : {:.2f}'.format(Wavelet_Hue))

    Features.append(Wavelet_Saturation)
    print('\nWavelet_Saturation : {:.2f}'.format(Wavelet_Saturation))

    Features.append(Wavelet_Value)
    print('\nWavelet_Value : {:.2f}'.format(Wavelet_Value))

    # LAB Space Color
    print(
        "-------------------------------------------------------------------------------------------------------\n"
        "LAB Color Feature Extraction :\n")

    LAB_img = cv.cvtColor(image, cv.COLOR_BGR2Lab)
    LAB_array = np.array(LAB_img)

    # Split the image into LAB color channels
    l, a, b = cv.split(LAB_img)

    # Calculate the mean of each color component (LAB)
    mean_LAB = np.mean(LAB_array, axis=(0, 1))
    MeanL = mean_LAB[0]
    MeanA = mean_LAB[1]
    MeanB = mean_LAB[2]

    Features.append(MeanL)
    print('Mean L: {:.2f}'.format(MeanL))

    Features.append(MeanA)
    print('Mean A: {:.2f}'.format(MeanA))

    Features.append(MeanB)
    print('Mean B: {:.2f}'.format(MeanB))

    # Calculate the standard deviation of each color component (LAB)
    std_dev = np.std(LAB_array, axis=(0, 1))
    std_L = std_dev[0]
    std_A = std_dev[1]
    std_B = std_dev[2]

    Features.append(std_L)
    print('\nStandard Deviation Hue: {:.2f}'.format(std_L))

    Features.append(std_A)
    print('Standard Deviation Saturation: {:.2f}'.format(std_A))

    Features.append(std_B)
    print('Standard Deviation Value: {:.2f}'.format(std_B))

    # Calculate the skewness of each color component (LAB)
    skew_L = skew(l.flatten())
    skew_A = skew(a.flatten())
    skew_B = skew(b.flatten())

    Features.append(skew_L)
    print('\nSkewness L: {:.2f}'.format(skew_L))

    Features.append(skew_A)
    print('Skewness A: {:.2f}'.format(skew_A))

    Features.append(skew_B)
    print('Skewness B: {:.2f}'.format(skew_B))

    # Calculate the kurtosis of each color component (LAB)
    kurtosis_L = kurtosis(l.flatten())
    kurtosis_A = kurtosis(a.flatten())
    kurtosis_B = kurtosis(b.flatten())

    Features.append(kurtosis_L)
    print('\nKurtosis L: {:.2f}'.format(kurtosis_L))

    Features.append(kurtosis_A)
    print('Kurtosis A: {:.2f}'.format(kurtosis_A))

    Features.append(kurtosis_B)
    print('Kurtosis B: {:.2f}'.format(kurtosis_B))

    # Compute the probability distribution of each color channel
    hist_l = cv.calcHist([l], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_a = cv.calcHist([a], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_b = cv.calcHist([b], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])

    # Compute the entropy of each color channel
    entropy_l = entropy(hist_l, base=2)
    entropy_a = entropy(hist_a, base=2)
    entropy_b = entropy(hist_b, base=2)

    entropy_L = float(entropy_l[0])
    entropy_A = float(entropy_a[0])
    entropy_B = float(entropy_b[0])

    Features.append(entropy_L)
    print('\nentropy L: {:.2f}'.format(entropy_L))

    Features.append(entropy_A)
    print('entropy A: {:.2f}'.format(entropy_A))

    Features.append(entropy_B)
    print('entropy B: {:.2f}'.format(entropy_B))

    # Perform one-level DWT using db4 wavelet for the three component
    coefficient_l = pywt.dwt2(l, 'db4')
    coefficient_a = pywt.dwt2(a, 'db4')
    coefficient_b = pywt.dwt2(b, 'db4')

    # Get the approximation coefficients (LL) and Take the mean of the LL coefficients for the three component
    LL, (LH, HL, HH) = coefficient_l
    Wavelet_L = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_a
    Wavelet_A = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_b
    Wavelet_B = np.mean(LL)

    Features.append(Wavelet_L)
    print('\nWavelet_Blue R: {:.2f}'.format(Wavelet_L))

    Features.append(Wavelet_A)
    print('\nWavelet_Blue R: {:.2f}'.format(Wavelet_A))

    Features.append(Wavelet_B)
    print('\nWavelet_Blue R: {:.2f}'.format(Wavelet_B))

    # YCC space Color
    print(
        "------------------------------------------------------------------------------------------------------\n"
        "YCC Color Feature Extraction :\n")

    YCC_img = cv.cvtColor(image, cv.COLOR_BGR2YCR_CB)
    YCC_array = np.array(YCC_img)

    # Split the image into color channels
    yb, cb, cr = cv.split(YCC_img)

    # Calculate the mean of each color component (YCC)
    mean_YCC = np.mean(YCC_array, axis=(0, 1))
    MeanYB = mean_YCC[0]
    MeanCB = mean_YCC[1]
    MeanCR = mean_YCC[2]

    Features.append(MeanYB)
    print('Mean Y: {:.2f}'.format(MeanYB))

    Features.append(MeanCB)
    print('Mean CR: {:.2f}'.format(MeanCB))

    Features.append(MeanCR)
    print('Mean CB: {:.2f}'.format(MeanCR))

    # Calculate the standard deviation of each color component (YCC)
    std_dev = np.std(YCC_array, axis=(0, 1))
    std_YB = std_dev[0]
    std_CB = std_dev[1]
    std_CR = std_dev[2]

    Features.append(std_YB)
    print('\nStandard Deviation Y: {:.2f}'.format(std_YB))

    Features.append(std_CB)
    print('Standard Deviation CB: {:.2f}'.format(std_CB))

    Features.append(std_CR)
    print('Standard Deviation CR: {:.2f}'.format(std_CR))

    # Calculate the skewness of each color component (YCC)
    skew_YB = skew(yb.flatten())
    skew_CB = skew(cb.flatten())
    skew_CR = skew(cr.flatten())

    Features.append(skew_YB)
    print('\nSkewness Y: {:.2f}'.format(skew_YB))

    Features.append(skew_CB)
    print('Skewness Cb: {:.2f}'.format(skew_CB))

    Features.append(skew_CR)
    print('Skewness Cr: {:.2f}'.format(skew_CR))

    # Calculate the kurtosis of each color component (YCC)
    kurtosis_YB = kurtosis(yb.flatten())
    kurtosis_CB = kurtosis(cb.flatten())
    kurtosis_CR = kurtosis(cr.flatten())

    Features.append(kurtosis_YB)
    print('\nKurtosis Y: {:.2f}'.format(kurtosis_YB))

    Features.append(kurtosis_CB)
    print('Kurtosis Cb: {:.2f}'.format(kurtosis_CB))

    Features.append(kurtosis_CR)
    print('Kurtosis Cr: {:.2f}'.format(kurtosis_CR))

    # Compute the probability distribution of each color channel
    hist_yb = cv.calcHist([yb], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_cb = cv.calcHist([cb], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_cr = cv.calcHist([cr], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])

    # Compute the entropy of each color channel
    entropy_yb = entropy(hist_yb, base=2)
    entropy_cb = entropy(hist_cb, base=2)
    entropy_cr = entropy(hist_cr, base=2)

    entropy_YB = float(entropy_yb[0])
    entropy_CB = float(entropy_cb[0])
    entropy_CR = float(entropy_cr[0])

    Features.append(entropy_YB)
    print('\nentropy Y: {:.2f}'.format(entropy_YB))

    Features.append(entropy_CB)
    print('entropy CB: {:.2f}'.format(entropy_CB))

    Features.append(entropy_CR)
    print('entropy CR: {:.2f}'.format(entropy_CR))

    # Perform one-level DWT using db4 wavelet for the three component
    coefficient_yb = pywt.dwt2(yb, 'db4')
    coefficient_cb = pywt.dwt2(cb, 'db4')
    coefficient_cr = pywt.dwt2(cr, 'db4')

    # Get the approximation coefficients (LL) and Take the mean of the LL coefficients for the three component
    LL, (LH, HL, HH) = coefficient_yb
    Wavelet_YB = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_cb
    Wavelet_CB = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_cr
    Wavelet_CR = np.mean(LL)

    Features.append(Wavelet_YB)
    print('\nWavelet_yb: {:.2f}'.format(Wavelet_YB))

    Features.append(Wavelet_CB)
    print('\nWavelet_cb: {:.2f}'.format(Wavelet_CB))

    Features.append(Wavelet_CR)
    print('\nWavelet_cr: {:.2f}'.format(Wavelet_CR))

    # XYZ Space Color
    print(
        "-------------------------------------------------------------------------------------------------------\n"
        "XYZ Color Feature Extraction :\n")

    XYZ_img = cv.cvtColor(image, cv.COLOR_BGR2XYZ)
    XYZ_array = np.array(XYZ_img)

    # Split the image into color channels
    x, y, z = cv.split(XYZ_img)

    mean_XYZ = np.mean(XYZ_array, axis=(0, 1))
    MeanX = mean_XYZ[0]
    MeanY = mean_XYZ[1]
    MeanZ = mean_XYZ[2]

    Features.append(MeanX)
    print('Mean X: {:.2f}'.format(MeanX))

    Features.append(MeanY)
    print('Mean Y: {:.2f}'.format(MeanY))

    Features.append(MeanZ)
    print('Mean Z: {:.2f}'.format(MeanZ))

    # Calculate the standard deviation of each color component (XYZ)
    std_dev = np.std(XYZ_array, axis=(0, 1))
    std_X = std_dev[0]
    std_Y = std_dev[1]
    std_Z = std_dev[2]

    Features.append(std_X)
    print('\nStandard Deviation X: {:.2f}'.format(std_X))

    Features.append(std_Y)
    print('Standard Deviation Y: {:.2f}'.format(std_Y))

    Features.append(std_Z)
    print('Standard Deviation Z: {:.2f}'.format(std_Z))

    # Calculate the skewness of each color component (XYZ)
    skew_X = skew(x.flatten())
    skew_Y = skew(y.flatten())
    skew_Z = skew(z.flatten())

    Features.append(skew_X)
    print('\nSkewness X: {:.2f}'.format(skew_X))

    Features.append(skew_Y)
    print('Skewness Y: {:.2f}'.format(skew_Y))

    Features.append(skew_Z)
    print('Skewness Z: {:.2f}'.format(skew_Z))

    # Calculate the kurtosis of each color component (YCC)
    kurtosis_X = kurtosis(x.flatten())
    kurtosis_Y = kurtosis(y.flatten())
    kurtosis_Z = kurtosis(z.flatten())

    Features.append(kurtosis_X)
    print('\nKurtosis X: {:.2f}'.format(kurtosis_X))

    Features.append(kurtosis_Y)
    print('Kurtosis Y: {:.2f}'.format(kurtosis_Y))

    Features.append(kurtosis_Z)
    print('Kurtosis Z: {:.2f}'.format(kurtosis_Z))

    # Compute the probability distribution of each color channel
    hist_x = cv.calcHist([x], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_y = cv.calcHist([y], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])
    hist_z = cv.calcHist([z], [0], None, [256], [0, 256]) / (image.shape[0] * image.shape[1])

    # Compute the entropy of each color channel
    entropy_x = entropy(hist_x, base=2)
    entropy_y = entropy(hist_y, base=2)
    entropy_z = entropy(hist_z, base=2)

    entropy_X = float(entropy_x[0])
    entropy_Y = float(entropy_y[0])
    entropy_Z = float(entropy_z[0])

    Features.append(entropy_X)
    print('\nentropy X: {:.2f}'.format(entropy_X))

    Features.append(entropy_Y)
    print('entropy Y: {:.2f}'.format(entropy_Y))

    Features.append(entropy_Z)
    print('entropy Z: {:.2f}'.format(entropy_Z))

    # Perform one-level DWT using db4 wavelet for the three component
    coefficient_x = pywt.dwt2(x, 'db4')
    coefficient_y = pywt.dwt2(y, 'db4')
    coefficient_z = pywt.dwt2(z, 'db4')

    # Get the approximation coefficients (LL) and Take the mean of the LL coefficients for the three component
    LL, (LH, HL, HH) = coefficient_x
    Wavelet_X = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_y
    Wavelet_Y = np.mean(LL)

    LL, (LH, HL, HH) = coefficient_z
    Wavelet_Z = np.mean(LL)

    Features.append(Wavelet_YB)
    print('\nWavelet_X: {:.2f}'.format(Wavelet_X))

    Features.append(Wavelet_CB)
    print('\nWavelet_Y: {:.2f}'.format(Wavelet_Y))

    Features.append(Wavelet_CR)
    print('\nWavelet_Z: {:.2f}'.format(Wavelet_Z))

    print(
        "*******************************************************************************************************\n")

    print("\nComputer the GLCM .... :\n")

    # Convert the image to a numpy array
    img_arr = np.array(gray)

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
            print("Contrast GLRM with distance of ", i + 1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Correlation ...\n")
    for i, elements in enumerate(correlation):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Correlation GLRM with distance of ", i + 1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Energy ...\n")
    for i, elements in enumerate(energy):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Energy GLRM with distance of ", i + 1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Homogeneity ...\n")
    for i, elements in enumerate(homogeneity):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Homogeneity GLRM with distance of ", i + 1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating ASM ...\n")
    for i, elements in enumerate(ASM):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("ASM GLRM with distance of ", i + 1, "and angle of ", angle, "Degree = ", element)

    print("\nCalculating Dissimilarity ...\n")
    for i, elements in enumerate(dissimilarity):
        for element, angle in zip(elements, text):
            Features.append(element)
            print("Dissimilarity GLRM with distance of ", i + 1, "and angle of ", angle, "Degree = ", element)
    df.loc[len(df)] = Features


# Load the CSV file
# df = pd.read_csv('Features CNCC V1 Normalized.csv')
# df = df.drop('label', axis=1)
# Predict the target labels using the loaded model
y_pred = model_SVM.predict(df)
print(y_pred)