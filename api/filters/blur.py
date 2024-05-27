from .convolution import apply_convolution
import numpy as np

def apply_blur_filter(image_path):
    kernel = np.array([
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ], dtype=np.float32)
    return apply_convolution(image_path, kernel)
