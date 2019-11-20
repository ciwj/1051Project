
from Cimpl import *

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Callum Ullrich.

def flip_vertical(oldImage: Image):
    """
    Takes a Cimpl.Image object and returns another Cimpl.Image object with the image vertically flipped.
    Created by Callum Ullrich.
    Student # 101148042, Group L4-6.
    """
    image = copy(oldImage)
    
    for x, y, col in oldImage:
        set_color(image, x, get_height(image) - (y + 1),  col)
    
    show(image)
    return image