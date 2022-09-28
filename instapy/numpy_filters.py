"""numpy implementation of image filters"""

from typing import Optional
import numpy as np


def numpy_color2gray(image: np.array) -> np.array:
    """Convert rgb pixel array to grayscale

    Args:
        image (np.array)
    Returns:
        np.array: gray_image
    """

    # TODO: Den førstgenererte gray_image brukes ikke, men overskrives av et array av en lavere dimensjon
    gray_image = np.empty_like(image)
    R_weight, G_weight, B_weight = 0.21, 0.72, 0.07

    gray_scales = image[:,:,0]*R_weight + image[:,:,1]*G_weight + image[:,:,2]*B_weight

    gray_image[:,:,0] = gray_scales
    gray_image[:,:,1] = gray_scales
    gray_image[:,:,2] = gray_scales

    


    return gray_image
    #return gray_image


def numpy_color2sepia(image: np.array, k: Optional[float] = 1) -> np.array:
    """Convert rgb pixel array to sepia

    Args:
        image (np.array)
        k (float): amount of sepia filter to apply (optional)

    The amount of sepia is given as a fraction, k=0 yields no sepia while
    k=1 yields full sepia.

    (note: implementing 'k' is a bonus task,
    you may ignore it for Task 9)

    Returns:
        np.array: sepia_image
    """

    if not 0 <= k <= 1:
        # validate k (optional)
        raise ValueError(f"k must be between [0-1], got {k=}")

    sepia_image = np.empty_like(image)

    # define sepia matrix (optional: with `k` tuning parameter for bonus task 13)
    sepia_matrix = np.array([
        [ 0.393, 0.769, 0.189],
        [ 0.349, 0.686, 0.168],
        [ 0.272, 0.534, 0.131],
    ])

    # HINT: For version without adaptive sepia filter, use the same matrix as in the pure python implementation
    # use Einstein sum to apply pixel transform matrix
    # Apply the matrix filter
    # Check which entries have a value greater than 255 and set it to 255 since we can not display values bigger than 255
    sepia_image[:,:,:] = np.clip(np.einsum('ijc,wc->ijw', image, sepia_matrix), 0, 255)

    # Return image (make sure it's the right type!)
    return sepia_image
