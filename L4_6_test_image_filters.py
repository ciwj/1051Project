from Cimpl import *
from L4_6_P4_image_filters import *

def test_red(oldImage):
    """
    Tests the red_channel function. Takes an image and returns True if the green and blue channels aren't present, returns False if there is any green or blue in the image. doctest examples are assuming oldImage has blue and green in them.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>> test_red(red_channel(oldImage))
    Image passed.
    >>> test_red(oldImage)
    Image failed.
    """
    image = copy(oldImage)
    isCorrect = True
    for pixel in image:
            x, y, (r, g, b) = pixel
            if not g == b == 0:
                isCorrect = False
    return isCorrect
        
def test_green(new_image):
    """ Name: Navin Kangal
    Student#: 101140794
    Team: L4-6
    Functions test whether or not there is blue or red still in any pixel in the picture.
    If there is blue or red in any pixel the program will return "Image failed test" if
    the image only has green in all of its pixels it will return "Image passed test".
    """
    for pixel in (new_image):
        x, y, (r, g, b) = pixel
        if r == 0 and b == 0:
            return("Image passed test")
        if r in pixel != 0 and b in pixel !=0:
            return("Image failed test")
        
def test_blue(new_image):
    """tests function to see if only blue channel is present; prints 'failed' if test failed and 'passed' if test passed. Created by Callum Ullrich.
    """
    chillin = True
    for pixel in new_image:
        x, y, (r, g, b) = pixel 
        if not r == 0 and g == 0:
            chillin = False
    return chillin
        
def test_combine(origImage, newImage):
    """
    Tests the combine() function by comparing the original image to the one that has been run through the combine() function. Takes two images, returns a message printing either saying passed or failed.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    """
    isCorrect = True
    for pixel1 in origImage:
        x, y, (r1, g1, b1) = pixel1
        pixel2 = get_color(newImage, x, y)
        r2, g2, b2 = pixel2
        if not (r1 == r2 and g1 == g2 and b1 == b2):
            isCorrect = False
    return isCorrect

def test_extreme_contrast(new_image):
    """
    Navin Kangal
    101140798
    The function test whether or not each colour is at 0 or 255. If a pixel has a number other than 0 or 255 the function will return "Image failed test"
    """
    test = True
    for x, y, ( r, g, b) in new_image:
        red = (r==0 or r==255)
        green = (g==0 or g==255)
        blue = (b==0 or b==255)
        if not (red and green and blue):
            test=False       
    return test

def test_sepia(image):
    """
    Tests the sepia() filter. Returns True if it passes, False if otherwise. Takes a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    """
    isCorrect = True
    
    filtered_image = sepia(image)
    for x, y, (r1, g1, b1) in image:
        brightness = (r1 + g1 + b1) / 3
        (r2, g2, b2) = get_color(filtered_image, x, y)
        if r2 < brightness and b2 > brightness:
            isCorrect = False
    return isCorrect

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