from instapy.python_filters import python_color2gray, python_color2sepia
from random import randint
from PIL import Image
import numpy as np


def test_color2gray(image):
    image = np.asarray(image)
    # run color2gray
    output = python_color2gray(image)
    # check that the result has the right shape, type
    assert image.shape == output.shape
    assert image.dtype == output.dtype
    # assert uniform r,g,b values
    for r in output:
        for c in r:
            assert c[0] == c[1] == c[2]


def test_color2sepia(image):
    image = np.asarray(image)
    # run color2sepia
    output = python_color2sepia(image)
    # check that the result has the right shape, type
    assert image.shape == output.shape
    assert image.dtype == output.dtype
    # verify some individual pixel samples
    # according to the sepia matrix
    sepia_matrix = [
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ]

    pixels = set()
    while len(pixels) < 100:
        pixels.add((randint(0, image.shape[0]), randint(0, image.shape[1])))

    for x,y in pixels:
        # Sample from image array
        R = int(image[x][y][0]*sepia_matrix[0][0] + image[x][y][1]*sepia_matrix[0][1] + image[x][y][2]*sepia_matrix[0][2])
        G = int(image[x][y][0]*sepia_matrix[1][0] + image[x][y][1]*sepia_matrix[1][1] + image[x][y][2]*sepia_matrix[1][2])
        B = int(image[x][y][0]*sepia_matrix[2][0] + image[x][y][1]*sepia_matrix[2][1] + image[x][y][2]*sepia_matrix[2][2])
        
        if R > 255:
            R = 255
        if G > 255:
            G = 255
        if B > 255:
            B = 255
        
        # Sample from output array
        R_out = output[x][y][0]
        G_out = output[x][y][1]
        B_out = output[x][y][2]

        assert R == R_out and G == G_out and B == B_out