from Cimpl import *
from L4_6_P2_blue import *

def test_blue(new_image):
    """tests function to see if only blue channel is present; prints 'failed' if test failed and 'passed' if test passed. Created by Callum Ullrich.
    """
    chillin = True
    for pixel in new_image:
        x, y, (r, g, b) = pixel 
        if not r == 0 and g == 0:
            chillin = False
    return chillin