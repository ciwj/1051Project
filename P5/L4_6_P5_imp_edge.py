import math
from Cimpl import *

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.


def detect_edges_better(oldImage: Image, threshold: int):
    """
    An improved version of the detect_edges function.
    Takes a Cimpl.Image object and a positive integer between 0-255,
    returns a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>> img1 = detect_edges_better(img, 200)
    >>> img2 = detect_edges_better(img, 100)
    """
    image = create_image(get_width(oldImage) + 1, get_height(oldImage) + 1) #Pads image
    image2 = copy(oldImage)
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    #Copy image over
    for x, y, col in oldImage:
        set_color(image, x, y,  col)
    
    #Make image grayscale
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) / 3
        brightPixel = create_color(brightness, brightness, brightness)
        set_color(image, x, y, brightPixel)
    
    #Tests for contrast and sets colour accordingly
    for x in range(get_width(oldImage)):
        for y in range(get_height(oldImage)):
            r2, g2, b2 = get_color(image, x, y + 1)
            r3, g3, b3 = get_color(image, x + 1, y)
            brightness = r
            brightnessDown = r2
            brightnessRight = r3
            diffDown = abs(brightness - brightnessDown)
            diffRight = abs(brightness - brightnessRight)
            if (diffRight > threshold) or (diffDown > threshold):
                set_color(image2, x, y, black)
            else:
                set_color(image2, x, y, white)
    
    show(image2)
    return image2
