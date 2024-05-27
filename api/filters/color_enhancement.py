from .convolution import apply_convolution
import numpy as np

def apply_color_enhancement_filter(image_path):
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ], dtype=np.float32)
    return apply_convolution(image_path, kernel)
