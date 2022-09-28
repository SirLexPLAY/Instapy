import numpy as np
from PIL import Image
from numpy_filters import numpy_color2gray
from python_filters import python_color2gray
from numba_filters import numba_color2gray

filename = "rain.jpg"
pixels = np.asarray(Image.open(filename))

pixels = python_color2gray(pixels)

image = Image.fromarray(pixels).convert("RGB")
image.save("rain_grayscale.jpg")

"""
listen = list(range(4*6*3))

a = np.array(listen).reshape([4,6,3])
b = np.empty_like(a)

b = a[:,:,0] + a[:,:,1]+ a[:,:,2]

print(b)
"""