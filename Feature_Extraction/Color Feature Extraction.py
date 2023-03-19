import cv2 as cv
import numpy as np
from scipy.stats import skew, kurtosis


img = cv.imread("Wheat_1.jpg")
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

print("--------------------------------------------------------------------------------------------------------------\n"
      "HSV Color Feature Extraction :\n")

hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hsv_array = np.array(hsv_img)

# Split the image into color channels
h, s, v = cv.split(hsv_img)

mean_hsv = np.mean(hsv_array, axis=(0, 1))
MeanH = mean_hsv[0]
MeanS = mean_hsv[1]
MeanV = mean_hsv[2]

print('Mean H: {:.2f}'.format(MeanH))
print('Mean S: {:.2f}'.format(MeanS))
print('Mean V: {:.2f}'.format(MeanV))

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

print('\nSkewness R: {:.2f}'.format(kurtosis_Hue))
print('Skewness G: {:.2f}'.format(kurtosis_Saturation))
print('Skewness B: {:.2f}'.format(kurtosis_Value))

print("--------------------------------------------------------------------------------------------------------------\n"
      "LAB Color Feature Extraction :\n")

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
      "YCC Color Feature Extraction :\n")

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
      "XYZ Color Feature Extraction :\n")

XYZ_img = cv.cvtColor(img, cv.COLOR_BGR2XYZ)
XYZ_array = np.array(XYZ_img)

mean_XYZ = np.mean(XYZ_array, axis=(0, 1))
MeanX = mean_XYZ[0]
MeanY2 = mean_XYZ[1]
MeanZ = mean_XYZ[2]

print('Mean X: {:.2f}'.format(MeanX))
print('Mean Y: {:.2f}'.format(MeanY2))
print('Mean Z: {:.2f}'.format(MeanZ))