from Cimpl import *

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Callum Ullrich.

def flip_vertically(oldImage: Image):
    """
    Takes a Cimpl.Image object and returns another Cimpl.Image object with the image vertically flipped.
    Created by Callum Ullrich.
    Student # 101148042, Group L4-6.
    >>> flip1 = flip_vertical(img)
    >>> flip2 = flip_vertical(img2)
    """
    image = copy(oldImage)
    
    for x, y, col in oldImage:
        set_color(image, get_width(image) - (x + 1), y,  col)
    
    show(image)
    return image
