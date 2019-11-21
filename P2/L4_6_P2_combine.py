from Cimpl import *

def combine(image1, image2, image3):
    """
    Takes 3 images, each containing only the red, blue, and green channels. Returns an image containing the 3 images, combined. Images must be the same size.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    """
    for pixel1 in image1:
        x, y, (r1, g1, b1) = pixel1
        pixel2 = get_color(image2, x, y)
        pixel3 = get_color(image3, x, y)
        r2, g2, b2 = pixel2
        r3, g3, b3 = pixel3
        colour = create_color(r1 + r2 + r3, g1 + g2 + g3, b1 + b2 + b3)
        set_color(image1, x, y, colour)
    show(image1)
    return image1

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
    if isCorrect:
        print("Function passed.")
    else:
        print("Function failed.")