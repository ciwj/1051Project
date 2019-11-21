from Cimpl import *
from L4_6_P5_vertical import flip_vertical

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.


def test_vertical():
    """
    Tests the flip_vertical() function.
    Returns True if passed, False if failed.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6
    >>>test_flip_vertical()
    True
    >>>test_flip_vertical()
    False
    Cases:
    (0, 0, 0)       -> (255, 0, 0)
    (128, 128, 128) -> (0, 255, 0)
    (255, 255, 255) -> (255, 255, 255)
    (0, 255, 0)     -> (128, 128, 128)
    (255, 0, 0)     -> (0, 0, 0)
    """
    
    is_correct = True
    img = create_image(5, 1)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(128, 128, 128))
    set_color(img, 2, 0,  create_color(255, 255, 255))
    set_color(img, 3, 0,  create_color(0, 255, 0))
    set_color(img, 4, 0,  create_color(255, 0, 0))
    
    expect = create_image(5, 1)
    
    set_color(expect, 0, 0,  create_color(255, 0, 0))
    set_color(expect, 1, 0,  create_color(0, 255, 0))
    set_color(expect, 2, 0,  create_color(255, 255, 255))
    set_color(expect, 3, 0,  create_color(128, 128, 128))
    set_color(expect, 4, 0,  create_color(0, 0, 0))
    
    actual = flip_vertical(img)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return is_correct
