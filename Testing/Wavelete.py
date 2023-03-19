import numpy as np
import pywt
from PIL import Image

# Load image
img = Image.open('image.jpg')
img_array = np.array(img)

# Extract color channels
R = img_array[:,:,0]
G = img_array[:,:,1]
B = img_array[:,:,2]

# Set wavelet type and level
wavelet = 'db1'
level = 5

# Perform wavelet transform for each channel
coeffs_R = pywt.wavedec2(R, wavelet, level=level)
coeffs_G = pywt.wavedec2(G, wavelet, level=level)
coeffs_B = pywt.wavedec2(B, wavelet, level=level)

# Reconstruct image from wavelet coefficients
R_wavelet = pywt.waverec2(coeffs_R, wavelet)
G_wavelet = pywt.waverec2(coeffs_G, wavelet)
B_wavelet = pywt.waverec2(coeffs_B, wavelet)

# Combine channels to get the RGB wavelet image
img_wavelet = np.zeros_like(img_array)
img_wavelet[:,:,0] = R_wavelet
img_wavelet[:,:,1] = G_wavelet
img_wavelet[:,:,2] = B_wavelet

# Save wavelet image
Image.fromarray(np.uint8(img_wavelet)).save('image_wavelet.jpg')
