from Cimpl import *
from L4_6_P2_green import *

def test_green(new_image):
    """ Name: Navin Kangal
    Student#: 101140794
    Team: L4-6
    Functions test whether or not there is blue or red still in any pixel in the picture.
    If there is blue or red in any pixel the program will return "Image failed test" if
    the image only has green in all of its pixels it will return "Image passed test".
    """
    for pixel in (new_image):
        x, y, (r, g, b) = pixel
        if r == 0 and b == 0:
            return("Image passed test")
        if r in pixel != 0 and b in pixel !=0:
            return("Image failed test")