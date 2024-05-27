from .convolution import apply_convolution
import numpy as np

def apply_edge_detection_filter(image_path):
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ], dtype=np.float32)
    return apply_convolution(image_path, kernel)
