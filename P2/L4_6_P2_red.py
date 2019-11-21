from Cimpl import *

def red_channel(oldImage):
    """
    Takes an image, and sets the green and blue channels to 0. Returns an image with only the red channel present.
    Parameter is a Cimpl.Image object and a Cimpl.Image object is returned.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    """
     
    image = copy(oldImage)
    for pixel in image:
        x, y, (r, g, b) = pixel
        newColor = create_color(r, 0, 0)
        set_color(image, x, y, newColor)
        show(oldImage)
    show(image)
    return image

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
    if isCorrect:
        print("Image passed.")
    else:
        print("Image failed.")