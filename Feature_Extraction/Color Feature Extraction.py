import cv2 as cv
import numpy as np
import pandas as pd
import os
from scipy.stats import skew, kurtosis, entropy
import pywt

columns = ["MeanB", "MeanG", "MeanR", "std_Blue", "std_Green", "std_Red", "skew_Blue", "skew_Green", "skew_Red",
           "kurtosis_Blue", "kurtosis_Green", "kurtosis_Red", "entropy_Blue", "entropy_Green", "entropy_Red",
           "MeanHue", "MeanSaturation", "MeanValue", "std_Hue", "std_Saturation", "std_Value", "skew_Hue",
           "skew_Saturation", "skew_Value", "kurtosis_Hue", "kurtosis_Saturation", "kurtosis_Value", "entropy_Hue",
           "entropy_Saturation", "entropy_Value", "MeanL", "MeanA", "MeanB", "std_L", "std_A", "std_B", "skew_L",
           "skew_A", "skew_B", "kurtosis_L", "kurtosis_A", "kurtosis_B", "entropy_L", "entropy_A", "entropy_B",
           "MeanYB", "MeanCB", "MeanCR", "std_YB", "std_CB", "std_CR", "skew_YB", "skew_CB", "skew_CR", "kurtosis_YB",
           "kurtosis_CB", "kurtosis_CR", "entropy_YB", "entropy_CB", "entropy_CR", "MeanX", "MeanY", "MeanZ", "std_X",
           "std_Y", "std_Z", "skew_X", "skew_Y", "skew_Z", "kurtosis_X", "kurtosis_Y", "kurtosis_Z", "entropy_X",
           "entropy_Y", "entropy_Z", "mean_LL"]

df = pd.DataFrame(columns=columns)

# Define Image Path
image_dir = "Data"
files = os.listdir(image_dir)
for filename in files:
    # Loading image
    print("The image selected :", filename)
    filepath = os.path.join(image_dir, filename)
    img = cv.imread(filepath)

    # initialise an empty list to store all Feature of the image
    Features = []

    # RGB Space Color
    print("\nRGB Color Feature Extraction :\n")
    img_array = np.array(img)

    # Split the image into color channels
    b, g, r = cv.split(img)

    # Calculate the mean of each color component (RGB)
    mean = np.mean(img_array, axis=(0, 1))
    MeanB = mean[0]
    MeanG = mean[1]
    MeanR = mean[2]

    print('Mean R: {:.2f}'.format(MeanR))
    print('Mean G: {:.2f}'.format(MeanG))
    print('Mean B: {:.2f}'.format(MeanB))

    # Calculate the standard deviation of each color component (RGB)
    std_dev = np.std(img_array, axis=(0, 1))
    std_Blue = std_dev[0]
    std_Green = std_dev[1]
    std_Red = std_dev[2]

    print('\nStandard Deviation R: {:.2f}'.format(std_Red))
    print('Standard Deviation G: {:.2f}'.format(std_Green))
    print('Standard Deviation B: {:.2f}'.format(std_Blue))

    # Calculate the skewness of each color component (RGB)
    skew_Blue = skew(b.flatten())
    skew_Green = skew(g.flatten())
    skew_Red = skew(r.flatten())

    print('\nSkewness R: {:.2f}'.format(skew_Red))
    print('Skewness G: {:.2f}'.format(skew_Green))
    print('Skewness B: {:.2f}'.format(skew_Blue))

    # Calculate the kurtosis of each color component (RGB)
    kurtosis_Blue = kurtosis(b.flatten())
    kurtosis_Green = kurtosis(g.flatten())
    kurtosis_Red = kurtosis(r.flatten())

    print('\nkurtosis R: {:.2f}'.format(kurtosis_Red))
    print('kurtosis G: {:.2f}'.format(kurtosis_Green))
    print('kurtosis B: {:.2f}'.format(kurtosis_Blue))

    # Compute the probability distribution of each color channel
    hist_b = cv.calcHist([b], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_g = cv.calcHist([g], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_r = cv.calcHist([r], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])

    # Compute the entropy of each color channel
    entropy_B = entropy(hist_b, base=2)
    entropy_G = entropy(hist_g, base=2)
    entropy_R = entropy(hist_r, base=2)

    entropy_Blue = float(entropy_B[0])
    entropy_Green = float(entropy_G[0])
    entropy_Red = float(entropy_R[0])

    print('\nentropy R: {:.2f}'.format(entropy_Red))
    print('entropy G: {:.2f}'.format(entropy_Green))
    print('entropy B: {:.2f}'.format(entropy_Blue))

    # HSV space Color
    print(
        "-----------------------------------------------------------------------------------------------------------\n"
        "HSV Color Feature Extraction :\n")

    hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsv_array = np.array(hsv_img)

    # Split the image into color channels
    h, s, v = cv.split(hsv_img)

    # Calculate the mean of each color component (HSV)
    mean_hsv = np.mean(hsv_array, axis=(0, 1))
    MeanHue = mean_hsv[0]
    MeanSaturation = mean_hsv[1]
    MeanValue = mean_hsv[2]

    print('Mean H: {:.2f}'.format(MeanHue))
    print('Mean S: {:.2f}'.format(MeanSaturation))
    print('Mean V: {:.2f}'.format(MeanValue))

    # Calculate the standard deviation of each color component (HSV)
    std_dev = np.std(hsv_array, axis=(0, 1))
    std_Hue = std_dev[0]
    std_Saturation = std_dev[1]
    std_Value = std_dev[2]

    print('\nStandard Deviation Hue: {:.2f}'.format(std_Hue))
    print('Standard Deviation Saturation: {:.2f}'.format(std_Saturation))
    print('Standard Deviation Value: {:.2f}'.format(std_Value))

    # Calculate the skewness of each color component (HSV)
    skew_Hue = skew(h.flatten())
    skew_Saturation = skew(s.flatten())
    skew_Value = skew(v.flatten())

    print('\nSkewness Hue: {:.2f}'.format(skew_Hue))
    print('Skewness Saturation: {:.2f}'.format(skew_Saturation))
    print('Skewness Value: {:.2f}'.format(skew_Value))

    # Calculate the kurtosis of each color component (HSV)
    kurtosis_Hue = kurtosis(h.flatten())
    kurtosis_Saturation = kurtosis(s.flatten())
    kurtosis_Value = kurtosis(v.flatten())

    print('\nKurtosis Hue: {:.2f}'.format(kurtosis_Hue))
    print('Kurtosis Saturation: {:.2f}'.format(kurtosis_Saturation))
    print('Kurtosis Value: {:.2f}'.format(kurtosis_Value))

    # Compute the probability distribution of each color channel
    hist_h = cv.calcHist([h], [0], None, [180], [0, 180]) / (img.shape[0] * img.shape[1])
    hist_s = cv.calcHist([s], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_v = cv.calcHist([v], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])

    # Compute the entropy of each color channel
    entropy_h = entropy(hist_h, base=2)
    entropy_s = entropy(hist_s, base=2)
    entropy_v = entropy(hist_v, base=2)

    entropy_Hue = float(entropy_h[0])
    entropy_Saturation = float(entropy_s[0])
    entropy_Value = float(entropy_v[0])

    print('\nentropy Hue: {:.2f}'.format(entropy_Hue))
    print('entropy Saturation: {:.2f}'.format(entropy_Saturation))
    print('entropy Value: {:.2f}'.format(entropy_Value))

    # LAB Space Color
    print(
        "-----------------------------------------------------------------------------------------------------------\n"
        "LAB Color Feature Extraction :\n")

    LAB_img = cv.cvtColor(img, cv.COLOR_BGR2Lab)
    LAB_array = np.array(LAB_img)

    # Split the image into LAB color channels
    l, a, b = cv.split(LAB_img)

    # Calculate the mean of each color component (LAB)
    mean_LAB = np.mean(LAB_array, axis=(0, 1))
    MeanL = mean_LAB[0]
    MeanA = mean_LAB[1]
    MeanB = mean_LAB[2]

    print('Mean L: {:.2f}'.format(MeanL))
    print('Mean A: {:.2f}'.format(MeanA))
    print('Mean B: {:.2f}'.format(MeanB))

    # Calculate the standard deviation of each color component (LAB)
    std_dev = np.std(LAB_array, axis=(0, 1))
    std_L = std_dev[0]
    std_A = std_dev[1]
    std_B = std_dev[2]

    print('\nStandard Deviation Hue: {:.2f}'.format(std_L))
    print('Standard Deviation Saturation: {:.2f}'.format(std_A))
    print('Standard Deviation Value: {:.2f}'.format(std_B))

    # Calculate the skewness of each color component (LAB)
    skew_L = skew(l.flatten())
    skew_A = skew(a.flatten())
    skew_B = skew(b.flatten())

    print('\nSkewness L: {:.2f}'.format(skew_L))
    print('Skewness A: {:.2f}'.format(skew_A))
    print('Skewness B: {:.2f}'.format(skew_B))

    # Calculate the kurtosis of each color component (LAB)
    kurtosis_L = kurtosis(l.flatten())
    kurtosis_A = kurtosis(a.flatten())
    kurtosis_B = kurtosis(b.flatten())

    print('\nKurtosis L: {:.2f}'.format(kurtosis_L))
    print('Kurtosis A: {:.2f}'.format(kurtosis_A))
    print('Kurtosis B: {:.2f}'.format(kurtosis_B))

    # Compute the probability distribution of each color channel
    hist_l = cv.calcHist([l], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_a = cv.calcHist([a], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_b = cv.calcHist([b], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])

    # Compute the entropy of each color channel
    entropy_l = entropy(hist_l, base=2)
    entropy_a = entropy(hist_a, base=2)
    entropy_b = entropy(hist_b, base=2)

    entropy_L = float(entropy_l[0])
    entropy_A = float(entropy_a[0])
    entropy_B = float(entropy_b[0])

    print('\nentropy L: {:.2f}'.format(entropy_L))
    print('entropy A: {:.2f}'.format(entropy_A))
    print('entropy B: {:.2f}'.format(entropy_B))

    # YCC space Color
    print(
        "-----------------------------------------------------------------------------------------------------------\n"
        "YCC Color Feature Extraction :\n")

    YCC_img = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
    YCC_array = np.array(YCC_img)

    # Split the image into color channels
    yb, cb, cr = cv.split(YCC_img)

    # Calculate the mean of each color component (YCC)
    mean_YCC = np.mean(YCC_array, axis=(0, 1))
    MeanYB = mean_YCC[0]
    MeanCB = mean_YCC[1]
    MeanCR = mean_YCC[2]

    print('Mean Y: {:.2f}'.format(MeanYB))
    print('Mean CR: {:.2f}'.format(MeanCB))
    print('Mean CB: {:.2f}'.format(MeanCR))

    # Calculate the standard deviation of each color component (YCC)
    std_dev = np.std(YCC_array, axis=(0, 1))
    std_YB = std_dev[0]
    std_CB = std_dev[1]
    std_CR = std_dev[2]

    print('\nStandard Deviation Y: {:.2f}'.format(std_YB))
    print('Standard Deviation CB: {:.2f}'.format(std_CB))
    print('Standard Deviation CR: {:.2f}'.format(std_CR))

    # Calculate the skewness of each color component (YCC)
    skew_YB = skew(yb.flatten())
    skew_CB = skew(cb.flatten())
    skew_CR = skew(cr.flatten())

    print('\nSkewness Y: {:.2f}'.format(skew_YB))
    print('Skewness Cb: {:.2f}'.format(skew_A))
    print('Skewness Cr: {:.2f}'.format(skew_B))

    # Calculate the kurtosis of each color component (YCC)
    kurtosis_YB = kurtosis(yb.flatten())
    kurtosis_CB = kurtosis(cb.flatten())
    kurtosis_CR = kurtosis(cr.flatten())

    print('\nKurtosis Y: {:.2f}'.format(kurtosis_YB))
    print('Kurtosis Cb: {:.2f}'.format(kurtosis_CB))
    print('Kurtosis Cr: {:.2f}'.format(kurtosis_CR))

    # Compute the probability distribution of each color channel
    hist_yb = cv.calcHist([yb], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_cb = cv.calcHist([cb], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_cr = cv.calcHist([cr], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])

    # Compute the entropy of each color channel
    entropy_yb = entropy(hist_yb, base=2)
    entropy_cb = entropy(hist_cb, base=2)
    entropy_cr = entropy(hist_cr, base=2)

    entropy_YB = float(entropy_yb[0])
    entropy_CB = float(entropy_cb[0])
    entropy_CR = float(entropy_cr[0])

    print('\nentropy Y: {:.2f}'.format(entropy_YB))
    print('entropy CB: {:.2f}'.format(entropy_CB))
    print('entropy CR: {:.2f}'.format(entropy_CR))

    # XYZ Space Color
    print(
        "-----------------------------------------------------------------------------------------------------------\n"
        "XYZ Color Feature Extraction :\n")

    XYZ_img = cv.cvtColor(img, cv.COLOR_BGR2XYZ)
    XYZ_array = np.array(XYZ_img)

    # Split the image into color channels
    x, y, z = cv.split(XYZ_img)

    mean_XYZ = np.mean(XYZ_array, axis=(0, 1))
    MeanX = mean_XYZ[0]
    MeanY = mean_XYZ[1]
    MeanZ = mean_XYZ[2]

    print('Mean X: {:.2f}'.format(MeanX))
    print('Mean Y: {:.2f}'.format(MeanY))
    print('Mean Z: {:.2f}'.format(MeanZ))

    # Calculate the standard deviation of each color component (XYZ)
    std_dev = np.std(XYZ_array, axis=(0, 1))
    std_X = std_dev[0]
    std_Y = std_dev[1]
    std_Z = std_dev[2]

    print('\nStandard Deviation X: {:.2f}'.format(std_X))
    print('Standard Deviation Y: {:.2f}'.format(std_Y))
    print('Standard Deviation Z: {:.2f}'.format(std_Z))

    # Calculate the skewness of each color component (XYZ)
    skew_X = skew(x.flatten())
    skew_Y = skew(y.flatten())
    skew_Z = skew(z.flatten())

    print('\nSkewness X: {:.2f}'.format(skew_X))
    print('Skewness Y: {:.2f}'.format(skew_Y))
    print('Skewness Z: {:.2f}'.format(skew_Z))

    # Calculate the kurtosis of each color component (YCC)
    kurtosis_X = kurtosis(x.flatten())
    kurtosis_Y = kurtosis(y.flatten())
    kurtosis_Z = kurtosis(z.flatten())

    print('\nKurtosis X: {:.2f}'.format(kurtosis_X))
    print('Kurtosis Y: {:.2f}'.format(kurtosis_Y))
    print('Kurtosis Z: {:.2f}'.format(kurtosis_Z))

    # Compute the probability distribution of each color channel
    hist_x = cv.calcHist([x], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_y = cv.calcHist([y], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])
    hist_z = cv.calcHist([z], [0], None, [256], [0, 256]) / (img.shape[0] * img.shape[1])

    # Compute the entropy of each color channel
    entropy_x = entropy(hist_x, base=2)
    entropy_y = entropy(hist_y, base=2)
    entropy_z = entropy(hist_z, base=2)

    entropy_X = float(entropy_x[0])
    entropy_Y = float(entropy_y[0])
    entropy_Z = float(entropy_z[0])

    print('\nentropy X: {:.2f}'.format(entropy_X))
    print('entropy Y: {:.2f}'.format(entropy_Y))
    print('entropy Z: {:.2f}'.format(entropy_Z))

    print(
        "-----------------------------------------------------------------------------------------------------------\n"
        "Wavelet transform 1 Level db4 :\n")
    coefficient = pywt.dwt2(yb, 'db4')

    # Get the approximation coefficients (LL)
    LL, (LH, HL, HH) = coefficient
    # Take the mean of the LL coefficients
    mean_LL = np.mean(LL)
    print('Mean of wavelet transform: {:.2f}'.format(mean_LL))

    print(
          "*******************************************************************************************************\n")
