from .blur import apply_blur_filter
from .edge_detection import apply_edge_detection_filter
from .color_enhancement import apply_color_enhancement_filter

def apply_filter(image_path, filter_type):
    if filter_type == 'blur':
        return apply_blur_filter(image_path)
    elif filter_type == 'edge':
        return apply_edge_detection_filter(image_path)
    elif filter_type == 'color':
        return apply_color_enhancement_filter(image_path)
    else:
        raise ValueError("Unknown filter type")
