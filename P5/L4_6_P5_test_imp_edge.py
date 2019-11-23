from Cimpl import *
import math
from L4_6_P5_imp_edge import *

#Milstone 2, P5. Group L4-6
#Submitted 20/11/19, created by Navin Kangal



def test_imp_edge():
    """
    By: Navin Kangal
    Student#: 101140794
    The function test the pixels in detect_edges_better to see if they are correct.
    Cases:
    detect_edges_better(image, 200)
    
         Pixel             Under            Right              Result
       (0, 0, 0)    +  (255, 0, 255) + (210, 200, 240) -->    (0, 0, 0)
       
    (210, 200, 240) +  (50, 40, 30)  +   (7, 56, 255)  --> (255, 255, 255)
    
     (7, 56, 255)   + (94, 213, 130) + (188, 216, 255) --> (255, 255, 255)
     
    """
    isCorrect = True
    img = create_image(4, 2)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(210, 200, 240))
    set_color(img, 2, 0,  create_color(7, 56, 255))
    set_color(img, 3, 0,  create_color(188, 216, 255))
    set_color(img, 0, 1,  create_color(255, 255, 255))
    set_color(img, 1, 1,  create_color(50, 40, 30))
    set_color(img, 2, 1,  create_color(94, 213, 130))
    set_color(img, 3, 1,  create_color(0, 0, 0))
    
    
    expect = create_image(4, 2)
    
    set_color(expect, 0, 0,  create_color(255, 255, 255))
    set_color(expect, 1, 0,  create_color(0, 0, 0))
    set_color(expect, 2, 0,  create_color(255, 255, 255))
    set_color(expect, 3, 0,  create_color(0, 0, 0))
    set_color(expect, 0, 1,  create_color(0, 0, 0))
    set_color(expect, 1, 1,  create_color(255, 255, 255))
    set_color(expect, 2, 1,  create_color(0, 0, 0))
    set_color(expect, 3, 1,  create_color(255, 255, 255))
    
    img = detect_edges_better(img, 200)
    
    for x, y, colour1 in expect:
        colour2 = get_color(img, x, y)
        if (colour1 != colour2):
            isCorrect = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1) 
            
        return isCorrect