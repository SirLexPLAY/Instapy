"""numba-optimized filters"""
from numba import jit
import numpy as np

@jit
def numba_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)

    R_weight, G_weight, B_weight = 0.21, 0.72, 0.07

    # iterate through the pixels, and apply the grayscale transform
    for i in range(len(image)):
        for j in range(len(image[i])):
            R = image[i][j][0]*R_weight
            G = image[i][j][1]*G_weight
            B = image[i][j][2]*B_weight
            gray = R+G+B
            gray_image[i][j] = np.array([gray, gray, gray])
    gray_image = gray_image.astype("uint8")    
    
    return gray_image


def numba_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    # Iterate through the pixels
    # applying the sepia matrix

    ...

    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image


...
