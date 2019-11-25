import Cimpl
import L4_6_image_filters

# Milestone 2, P5. Group L4-6.
# Submitted 24/11/19


def test_red() -> bool:
    """
    Tests the red_channel function.
    Takes an image and returns True if the green and blue channels aren't
    present, returns False if there is any green or blue in the image.
    doctest examples are assuming oldImage has blue and green in them.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>> test_red(red_channel(oldImage))
    Image passed.
    >>> test_red(oldImage)
    Image failed.
    Cases:
    (0, 0, 0)       -> (0, 0, 0)
    (128, 128, 128) -> (128, 0, 0)
    (255, 255, 255) -> (255, 0, 0)
    (0, 255, 0)     -> (0, 0, 0)
    (255, 0, 0)     -> (255, 0, 0)
    """
    is_correct = True
    img = create_image(5, 1) #Creates an image with the following colours
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(128, 128, 128))
    set_color(img, 2, 0,  create_color(255, 255, 255))
    set_color(img, 3, 0,  create_color(0, 255, 0))
    set_color(img, 4, 0,  create_color(255, 0, 0))
    
    expect = create_image(5, 1) #Creates an image with the following colours
    set_color(expect, 0, 0,  create_color(0, 0, 0))
    set_color(expect, 1, 0,  create_color(128, 0, 0))
    set_color(expect, 2, 0,  create_color(255, 0, 0))
    set_color(expect, 3, 0,  create_color(0, 0, 0))
    set_color(expect, 4, 0,  create_color(255, 0, 0))
    
    actual = red_channel(img)
    
    for x, y, colour1 in expect: #checks if the coulours are what they should be after the filter has run
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return is_correct


def test_combine()-> bool:
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
    is_correct = True
    
    img1 = create_image(4, 1)#Creates an image
    img2 = create_image(4, 1)#Creates an image
    img3 = create_image(4, 1)#Creates an image
    expect = create_image(4, 1)#Creates an image
    
    #Adds pixels
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
    
    #Compares expected to actual
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)    
    
    return is_correct


def test_sepia() -> bool:
    """
    Tests the sepia() filter. Returns True if it passes, False if otherwise.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    Test cases:
    (0, 0, 0) -> (0, 0, 0)
    (128, 128, 128) -> (147, 128, 109)
    (200, 200, 200) -> (216, 200, 186)
    """
    is_correct = True
    
    #Creates before img
    img = create_image(3, 1)
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(128, 128, 128))
    set_color(img, 2, 0,  create_color(200, 200, 200))
    
    #Creates expected img
    expect = create_image(3, 1)
    set_color(expect, 0, 0,  create_color(0, 0, 0))
    set_color(expect, 1, 0,  create_color(147, 128, 108))
    set_color(expect, 2, 0,  create_color(216, 200, 186))
    
    actual = sepia(img)
    
    #Compares pixels
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return is_correct


def test_three_tone():
    """
    Tests the three_tone() function. Returns True if successful,
    otherwise returns False.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>> three_toned_img = three_tone(img, "white", "black", "red")
    Cases:
    (0, 0, 0) -> (0, 0, 0)
    (128, 0, 255) -> (0, 0, 0)
    (255, 128, 200) -> (255, 0, 0)
    (0, 200, 127) -> (255, 0, 0)
    """
    
    #Creates before & expected img
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
    
    #Compares expected to actual
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
            return False
    
    return True


def test_two_tone():
    """
    Tests the two_tone() function.
    Returns True if successful, otherwise returns False.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>> two_toned_img = two_tone(img, "black", "white")
    Test cases:
    (0, 0, 0) -> (0, 0, 0)
    (128, 128, 128) -> (255, 255, 255)
    (64, 233, 11) -> (0, 0, 0)
    (200, 90, 140) -> (255, 255, 255)
    """
    
    is_correct = True
    
    #Creates before & expected img
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
    
    #Compares expected to actual img
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
    
    return is_correct


def test_edge() -> bool:
    """
    Tests the edge_detection() function.
    Returns True if it passes, False otherwise.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6
    Cases:
    >>> test_edge()
    True
    >>>test_edge()
    False
    Top pixel     Bottom pixel      Result
    (0, 0, 0)       + (255, 255, 255) -> (255, 255, 255), (255, 255, 255)
    (0, 0, 0)       + (53, 64, 100)   -> (0, 0, 0), (255, 255, 255)
    (124, 132, 122) + (0, 66, 0)      -> (0, 0, 0), (255, 255, 255)
    """
    
    is_correct = True
    
    #Creates test and expected image
    img = create_image(3, 2)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 1, 0,  create_color(0, 0, 0))
    set_color(img, 2, 0,  create_color(124, 132, 122))
    set_color(img, 0, 1,  create_color(255, 255, 255))
    set_color(img, 1, 1,  create_color(53, 64, 100))
    set_color(img, 2, 1,  create_color(0, 66, 0))
    
    expect = create_image(3, 2)
    
    set_color(expect, 0, 0,  create_color(255, 255, 255))
    set_color(expect, 1, 0,  create_color(0, 0, 0))
    set_color(expect, 2, 0,  create_color(0, 0, 0))
    set_color(expect, 0, 1,  create_color(255, 255, 255))
    set_color(expect, 1, 1,  create_color(255, 255, 255))
    set_color(expect, 2, 1,  create_color(255, 255, 255))
    
    actual = detect_edges(img, 128)
    
    #Compares actual and expected pixels
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return is_correct


def test_vertical() -> bool:
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
    
    #Creates test and expected image
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
    
    #Compares actual and expected pixels
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return is_correct


def test_blue():
    """
    Tests function to see if only blue channel is present.
    Prints 'failed' if test failed and 'passed' if test passed. 
    Created by Callum Ullrich.
    """
    blue = True
    for pixel in new_image:
        x, y, (r, g, b) = pixel
        if not r == 0 and g == 0:
            chillin = False
    return blue


def test_green(new_image):
    """ Name: Navin Kangal
    Student#: 101140794
    Team: L4-6
    Functions test whether or not there is blue
    or red still in any pixel in the picture.
    If there is blue or red in any pixel the 
    program will return "Image failed test" if
    the image only has green in all of its pixels
    it will return "Image passed test".
    """
    for pixel in (new_image):
        x, y, (r, g, b) = pixel
        if r == 0 and b == 0:
            return("Image passed test")
        if r in pixel != 0 and b in pixel !=0:
            return("Image failed test")


def test_extreme_contrast(new_image: Image) ->Image:
    """
    Navin Kangal
    101140798
    The function test whether or not each colour
    is at 0 or 255. If a pixel has a number other
    than 0 or 255 the function will return "Image
    failed test"
    """
    test = True
    for x, y, ( r, g, b) in new_image:
        red = (r == 0 or r == 255)
        green = (g == 0 or g == 255)
        blue = ( b == 0 or b == 255)
        if not (red and green and blue):
            test = False
    if test == True:
        print("Image passsed test")
    if test == False:
        print("Image failed test")


def test_posterize():
    """
    Tests the posterize() function.
    Returns True if it passes.
    Returns False otherwise.
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


def test_flip_horizontal():
    """
    Tests the flip_horizontal() function.
    Returns True if it passes.
    Returns False otherwise.
    Created by Callum Ullrich.
    Student # 101148042, Group L4-6
    >>>test_flip_horizontal()
    True
    >>>test_flip_horizontal()
    False
    Cases:
    (0, 0, 0)       -> (255, 0, 0)
    (128, 128, 128) -> (0, 255, 0)
    (255, 255, 255) -> (255, 255, 255)
    (0, 255, 0)     -> (128, 128, 128)
    (255, 0, 0)     -> (0, 0, 0)
    """
    
    is_correct = True
    img = create_image(1, 5)
    
    set_color(img, 0, 0,  create_color(0, 0, 0))
    set_color(img, 0, 1,  create_color(128, 128, 128))
    set_color(img, 0, 2,  create_color(255, 255, 255))
    set_color(img, 0, 3,  create_color(0, 255, 0))
    set_color(img, 0, 4,  create_color(255, 0, 0))
    
    expect = create_image(1, 5)
    
    set_color(expect, 0, 0,  create_color(255, 0, 0))
    set_color(expect, 0, 1,  create_color(0, 255, 0))
    set_color(expect, 0, 2,  create_color(255, 255, 255))
    set_color(expect, 0, 3,  create_color(128, 128, 128))
    set_color(expect, 0, 4,  create_color(0, 0, 0))
    
    actual = flip_horizontal(img)
    
    for x, y, colour1 in expect:
        colour2 = get_color(actual, x, y)
        if (colour1 != colour2):
            is_correct = False
            print('Pixel failed: ', (x, y), 'is', colour2, 'not', colour1)
    
    return is_correct


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