from Cimpl import *
from L4_6_P2_combine import combine

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.


def test_combine():
    """
    Tests the combine() function.
    Returns True if passed, False otherwise.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>>test_combine()
    True
    >>>test_combine()
    False
    Cases:
    (255, 0, 0) + (0, 100, 0) + (0, 0, 0) -> (255, 100, 0)
    (120, 0, 0) + (0, 0, 0) + (0, 0, 0) -> (120, 0, 0)
    (255, 0, 0) + (0, 255, 0) + (0, 0, 255) -> (255, 255, 255)
    (0, 0, 0) + (0, 0, 0) + (0, 0, 0) -> (0, 0, 0)
    """
    isCorrect = True
    
    img1 = create_image(4, 1)
    img2 = create_image(4, 1)
    img3 = create_image(4, 1)
    expect = create_image(4, 1)
    
    set_color(img1, 0, 0,  create_color(255, 0, 0))
    set_color(img1, 1, 0,  create_color(120, 0, 0))
    set_color(img1, 2, 0,  create_color(255, 0, 0))
    set_color(img1, 3, 0,  create_color(0, 0, 0))
    set_color(img2, 0, 0,  create_color(0, 100, 0))
    set_color(img2, 1, 0,  create_color(0, 0, 0))
    set_color(img2, 2, 0,  create_color(0, 255, 0))
    set_color(img2, 3, 0,  create_color(0, 0, 0))
    set_color(img3, 0, 0,  create_color(0, 0, 0))
    set_color(img3, 1, 0,  create_color(0, 0, 0))
    set_color(img3, 2, 0,  create_color(0, 0, 255))
    set_color(img3, 3, 0,  create_color(0, 0, 0))
    set_color(expect, 0, 0,  create_color(255, 100, 0))
    set_color(expect, 1, 0,  create_color(120, 0, 0))
    set_color(expect, 2, 0,  create_color(255, 255, 255))
    set_color(expect, 3, 0,  create_color(0, 0, 0))
    
    actual = combine(img1, img2, img3)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)    
    
    return isCorrect
