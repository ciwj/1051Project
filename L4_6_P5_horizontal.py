from Cimpl import *


def flip_horizontal(oldImage):
    """
    Takes a Cimpl.Image object and returns another Cimpl.Image object with the image horizontally flipped.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    """
    image = copy(oldImage)
    
    for x, y, col in oldImage:
        set_color(image, get_width(image) - (x + 1), y,  col)
    
    show(image)
    return image