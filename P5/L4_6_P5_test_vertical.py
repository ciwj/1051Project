from Cimpl import *
from L4_6_P5_vertical import *

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.

def test_flip_vertical():
    """
    Tests the flip_vertical() function. Returns True if passed, False if failed.
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
    
    isCorrect = True
    img = create_image(1, 5)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 0, 1,  create_color(128, 128, 128))
    set_color(img, 0, 2,  create_color(255, 255, 255))
    set_color(img, 0, 3,  create_color(0, 255, 0))
    set_color(img, 0, 4,  create_color(255, 0, 0))
    
    expect = create_image(1, 5)
    
    set_color(img, 0, 0,  create_color(255, 0, 0))
    set_color(img, 0, 1,  create_color(0, 255, 0))
    set_color(img, 0, 2,  create_color(255, 255, 255))
    set_color(img, 0, 3,  create_color(128, 128, 128))
    set_color(img, 0, 4,  create_color(0, 0, 0))
    
    actual = flip_vertical(img)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            isCorrect = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return isCorrect    
