from Cimpl import *
from L4_6_P4_posterize import posterize, _adjust_component

def test_posterize():
    """
    Tests the posterize() function. Returns True if it passes, returns False otherwise.
    Created by Callum Ullrich.
    Student # 101148042, Group L4-6
    >>>test_posterize()
    True
    >>>test_posterize()
    False
    Cases:
    (67, 190, 0)    -> (95, 159, 31)
    (128, 143, 222) -> (159, 159, 223)
    (2, 255, 88)    -> (31, 223, 95)
    (230, 230, 12)  -> (223, 223, 31)
    (140, 190, 40)  -> (159, 159, 31)
    """
    
    isCorrect = True
    img = create_image(1, 5)
    
    set_color(img, 0, 0,  create_color(67, 190, 0))
    set_color(img, 0, 1,  create_color(128, 143, 222))
    set_color(img, 0, 2,  create_color(2, 255, 88))
    set_color(img, 0, 3,  create_color(230, 230, 12))
    set_color(img, 0, 4,  create_color(140, 190, 40))
    
    expect = create_image(1, 5)
    
    set_color(expect, 0, 0,  create_color(95, 159, 31))
    set_color(expect, 0, 1,  create_color(159, 159, 223))
    set_color(expect, 0, 2,  create_color(31, 223, 95))
    set_color(expect, 0, 3,  create_color(223, 223, 31))
    set_color(expect, 0, 4,  create_color(159, 159, 31))
    
    actual = posterize(img)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            isCorrect = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return isCorrect

def test_adjust():
    """
    Tests the _adjust_component() function. Returns True if it passes, returns False otherwise.
    Created by Callum Ullrich.
    Student # 101148042, Group L4-6
    >>>test_adjust()
    True
    >>>test_adjust()
    False
    Cases:
    (255, 12, 100, 170) -> (223, 31, 95, 159)
    """    
    values = (255, 12, 100, 170) 
    expect = (223, 31, 95, 159)
    
    actual = (_adjust_component(values[0]), _adjust_component(values[1]), _adjust_component(values[2]), _adjust_component(values[3]))
    
    if actual == expect:
        return True
    else:
        return False
    