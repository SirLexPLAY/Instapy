from instapy.numba_filters import numba_color2gray, numba_color2sepia
import numpy as np
import numpy.testing as nt


def test_color2gray(image, reference_gray):
    image = np.asarray(image)
    # run color2gray
    output = numba_color2gray(image)
    nt.assert_allclose(output, reference_gray)


def test_color2sepia(image, reference_sepia):
    image = np.asarray(image)
    # run color2sepia
    output = numba_color2sepia(image)
    nt.assert_allclose(output, reference_sepia)
