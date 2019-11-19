from Cimpl import *
from L4_6_P4_twotonethreetone import three_tone

def test_three_tone():
    """
    Tests the three_tone() function. Returns True if successful, otherwise returns False
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    Cases:
    (0, 0, 0) -> (0, 0, 0)
    (128, 0, 255) -> (0, 0, 0)
    (255, 128, 200) -> (255, 0, 0)
    (0, 200, 127) -> (255, 0, 0)
    """
    
    img = create_image(4, 1)
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(128, 0, 255))
    set_color(img, 2, 0,  create_color(255, 128, 200))
    set_color(img, 0, 0,  create_color(0, 200, 127))
    
    expect = create_image(4, 1)
    set_color(expect, 0, 0,  create_color(0, 0, 0))
    set_color(expect, 1, 0,  create_color(0, 0, 0))
    set_color(expect, 2, 0,  create_color(255, 0, 0))
    set_color(expect, 3, 0,  create_color(255, 0, 0))
    
    actual = three_tone(img, "white", "black", "red")
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
            return False
    
    return True   
