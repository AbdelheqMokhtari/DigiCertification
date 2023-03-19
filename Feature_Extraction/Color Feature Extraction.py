import cv2 as cv
import numpy as np
from scipy.stats import skew, kurtosis


img = cv.imread("Wheat_1.jpg")
print("\nRGB Color Feature Extraction :")
img_array = np.array(img)

# mean calculation
mean = np.mean(img_array, axis=(0, 1))
MeanB = mean[0]
MeanG = mean[1]
MeanR = mean[2]

print('Mean R: {:.2f}'.format(MeanR))
print('Mean G: {:.2f}'.format(MeanG))
print('Mean B: {:.2f}'.format(MeanB))

# standard deviation
std_dev = np.std(img_array, axis=(0, 1))
std_Blue = std_dev[0]
std_Green = std_dev[1]
std_Red = std_dev[2]

print('\nStandard Deviation R: {:.2f}'.format(std_Red))
print('Standard Deviation G: {:.2f}'.format(std_Green))
print('Standard Deviation B: {:.2f}'.format(std_Blue))

# skewness calculation
skew = skew(img_array, axis=(0, 1))
skew_Blue = skew[0]
skew_Green = skew[1]
skew_Red = skew[2]

print('\nSkewness R: {:.2f}'.format(skew_Red))
print('Skewness G: {:.2f}'.format(skew_Green))
print('Skewness B: {:.2f}'.format(skew_Blue))

# Calculate the kurtosis of each color component
kurtosis = kurtosis(img_array, axis=(0, 1))
kurtosis_Blue = kurtosis[0]
kurtosis_Green = kurtosis[1]
kurtosis_Red = kurtosis[2]

print('\nSkewness R: {:.2f}'.format(kurtosis_Red))
print('Skewness G: {:.2f}'.format(kurtosis_Green))
print('Skewness B: {:.2f}'.format(kurtosis_Blue))
print("--------------------------------------------------------------------------------------------------------------\n"
      "HSV Color Feature Extraction :")

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hsv_array = np.array(hsv_img)

mean_hsv = np.mean(hsv_array, axis=(0, 1))
MeanH = mean_hsv[0]
MeanS = mean_hsv[1]
MeanV = mean_hsv[2]

print('Mean H: {:.2f}'.format(MeanH))
print('Mean S: {:.2f}'.format(MeanS))
print('Mean V: {:.2f}'.format(MeanV))

print("--------------------------------------------------------------------------------------------------------------\n"
      "LAB Color Feature Extraction :")

LAB_img = cv.cvtColor(img, cv.COLOR_BGR2Lab)
LAB_array = np.array(LAB_img)

mean_LAB = np.mean(LAB_array, axis=(0, 1))
MeanL = mean_LAB[0]
MeanA = mean_LAB[1]
MeanB = mean_LAB[2]

print('Mean L: {:.2f}'.format(MeanL))
print('Mean A: {:.2f}'.format(MeanA))
print('Mean B: {:.2f}'.format(MeanB))

print("--------------------------------------------------------------------------------------------------------------\n"
      "YCC Color Feature Extraction :")

YCC_img = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
YCC_array = np.array(YCC_img)

mean_YCC = np.mean(YCC_array, axis=(0, 1))
MeanY = mean_YCC[0]
MeanCR = mean_YCC[1]
MeanCB = mean_YCC[2]

print('Mean L: {:.2f}'.format(MeanY))
print('Mean A: {:.2f}'.format(MeanCR))
print('Mean B: {:.2f}'.format(MeanCB))

print("--------------------------------------------------------------------------------------------------------------\n"
      "XYZ Color Feature Extraction :")

XYZ_img = cv.cvtColor(img, cv.COLOR_BGR2XYZ)
XYZ_array = np.array(XYZ_img)

mean_XYZ = np.mean(XYZ_array, axis=(0, 1))
MeanX = mean_XYZ[0]
MeanY2 = mean_XYZ[1]
MeanZ = mean_XYZ[2]

print('Mean X: {:.2f}'.format(MeanX))
print('Mean Y: {:.2f}'.format(MeanY2))
print('Mean Z: {:.2f}'.format(MeanZ))