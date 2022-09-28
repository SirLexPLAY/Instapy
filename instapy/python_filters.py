"""pure Python implementation of image filters"""

import numpy as np
from PIL import Image


def python_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """
    gray_image = np.empty_like(image)
    
    R_weight, G_weight, B_weight = 0.21, 0.72, 0.07

    # iterate through the pixels, and apply the grayscale transform
    for i, x in enumerate(image):
        for j, y in enumerate(x):
            R = y[0]*R_weight
            G = y[1]*G_weight
            B = y[2]*B_weight
            gray = R+G+B
            gray_image[i][j] = np.array([gray, gray, gray])
    gray_image = gray_image.astype("uint8")    

    return gray_image


def python_color2sepia(image: np.array) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
    Returns:
        np.array: sepia_image
    """
    sepia_image = np.empty_like(image)
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    # Iterate through the pixels
    # applying the sepia matrix
    for i, x in enumerate(image):
        for j, y in enumerate(x):
            R = y[0]*sepia_matrix[0][0] + y[1]*sepia_matrix[0][1] + y[2]*sepia_matrix[0][2]
            G = y[0]*sepia_matrix[1][0] + y[1]*sepia_matrix[1][1] + y[2]*sepia_matrix[1][2]
            B = y[0]*sepia_matrix[2][0] + y[1]*sepia_matrix[2][1] + y[2]*sepia_matrix[2][2]
            
            if R > 255:
                R = 255
            if G > 255:
                G = 255
            if B > 255:
                B = 255

            sepia_image[i][j][0] = R 
            sepia_image[i][j][1] = G 
            sepia_image[i][j][2] = B 
    
    # Return image
    # don't forget to make sure it's the right type!
    return sepia_image
