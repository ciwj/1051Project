from Cimpl import *
from L4_6_P2_combine import *

def test_combine(origImage, newImage):
    """
    Tests the combine() function by comparing the original image to the one that has been run through the combine() function. Takes two images, returns a message printing either saying passed or failed.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    """
    isCorrect = True
    for pixel1 in origImage:
        x, y, (r1, g1, b1) = pixel1
        pixel2 = get_color(newImage, x, y)
        r2, g2, b2 = pixel2
        if not (r1 == r2 and g1 == g2 and b1 == b2):
            isCorrect = False
    return isCorrect