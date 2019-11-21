from Cimpl import *
from L4_6_P2_red import *

def test_red(oldImage):
    """
    Tests the red_channel function. Takes an image and returns True if the green and blue channels aren't present, returns False if there is any green or blue in the image. doctest examples are assuming oldImage has blue and green in them.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>> test_red(red_channel(oldImage))
    Image passed.
    >>> test_red(oldImage)
    Image failed.
    """
    image = copy(oldImage)
    isCorrect = True
    for pixel in image:
            x, y, (r, g, b) = pixel
            if not g == b == 0:
                isCorrect = False
    return isCorrect