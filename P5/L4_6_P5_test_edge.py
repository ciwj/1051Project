from Cimpl import *
from L4_6_P5_edge import *

def test_edge():
    """
    Tests the edge_detection() function. Returns True if it passes, False otherwise.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6
    Cases:
    >>> edge_detection(image, 128)
    Top pixel     Bottom pixel      Result
    (0, 0, 0)       + (255, 255, 255) -> (0, 0, 0)
    (0, 0, 0)       + (53, 64, 100)   -> (255, 255, 255)
    (124, 132, 122) + (0, 66, 0)      -> (0, 0, 0)
    """
    
    img = create_image(3, 2)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(0, 0, 0))
    set_color(img, 2, 0,  create_color(124, 132, 122))
    set_color(img, 0, 1,  create_color(255, 255, 255))
    set_color(img, 1, 1,  create_color(53, 64, 100))
    set_color(img, 2, 1,  create_color(0, 66, 0))
    
    expect = create_image(3, 2)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(255, 255, 255))
    set_color(img, 2, 0,  create_color(0, 0, 0))
    set_color(img, 0, 1,  create_color(255, 255, 255))
    set_color(img, 1, 1,  create_color(0, 0, 0))
    set_color(img, 2, 1,  create_color(0, 0, 0))
    
    actual = edge_detection(img, 128)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            isCorrect = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return isCorrect    