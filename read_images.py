# Check the resolution of captured "jpeg" and "png" images.

from PIL import Image
import numpy as np

# Open the image
img_jpg = Image.open('Captures/base_capture(jpeg).jpg')
img_png = Image.open('Captures/base_capture(png).png')

# Convert the image to a numpy array
img1_array = np.array(img_jpg)
img2_array = np.array(img_png)

print(img1_array.shape, img2_array.shape)
