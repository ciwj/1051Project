from Cimpl import *
from L4_6_P4_image_filters import two_tone

def test_two_tone():
    """
    Tests the two_tone() function. Returns True if successful, otherwise returns False
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    Test cases:
    (0, 0, 0) -> (0, 0, 0)
    (128, 128, 128) -> (255, 255, 255)
    (64, 233, 11) -> (0, 0, 0)
    (200, 90, 140) -> (255, 255, 255)
    """
    
    isCorrect = True
    
    img = create_image(4, 1)
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(128, 128, 128))
    set_color(img, 2, 0,  create_color(64, 233, 11))
    set_color(img, 3, 0,  create_color(200, 90, 140))
    
    expect = create_image(4, 1)
    set_color(expect, 0, 0,  create_color(0, 0, 0))
    set_color(expect, 1, 0,  create_color(255, 255, 255))
    set_color(expect, 2, 0,  create_color(0, 0, 0))
    set_color(expect, 3, 0,  create_color(255, 255, 255))    
    
    actual = two_tone(img, "black", "white")
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            isCorrect = False
    
    return isCorrect