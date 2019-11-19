from Cimpl import *
from L4_6_P4_sepia import *

def test_sepia():
    """
    Tests the sepia() filter. Returns True if it passes, False if otherwise.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    Test cases:
    (0, 0, 0) -> (0, 0, 0)
    (128, 128, 128) -> (147, 128, 109)
    (200, 200, 200) -> (216, 200, 186)
    """
    isCorrect = True
    
    img = create_image(3, 1)
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(128, 128, 128))
    set_color(img, 2, 0,  create_color(200, 200, 200))
    
    expect = create_image(3, 1)
    set_color(expect, 0, 0,  create_color(0, 0, 0))
    set_color(expect, 1, 0,  create_color(147, 128, 108))
    set_color(expect, 2, 0,  create_color(216, 200, 186))
    
    actual = sepia(img)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            isCorrect = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return isCorrect 
