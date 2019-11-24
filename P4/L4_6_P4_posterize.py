from Cimpl import *

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.


def _adjust_component(comp: int) -> int:
    """
    Takes a pixel's red, green or blue component and determines what range it falls under.
    Based on this, it'll return 31, 95, 159, or 223.
    Comp should be between 0 and 255, inclusive.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>> _adjust_component(63)
    31
    >>> _adjust_component(243)
    223
    >>> _adjust_component(64)
    95
    """
    if comp <= 63:
        return 31
    elif comp <= 127:
        return 95
    elif comp <= 191:
        return 159
    else:
        return 223


def posterize(oldImage):
    """
    Takes an image and posterizes it, with the quadrants being:
    0-63, 64, 127, 128-191, 192-255. Takes and returns a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>> posterized_img = posterize(img)
    """
    image = copy(oldImage)
    
    #Go through every pixel, set colour to the result from _adjust_component
    for pixel in image:
        x, y, (r, g, b) = pixel
        colour = create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b))
        set_color(image, x, y, colour)
    
    show(image)
    return image
