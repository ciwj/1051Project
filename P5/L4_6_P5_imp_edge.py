from Cimpl import *
import math

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.

def detect_edges_better(oldImage, threshold):
    """
    An improved version of the detect_edges function. Takes a Cimpl.Image object and a positive integer between 0-255, returns a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    """
    image = create_image(get_width(oldImage) + 1, get_height(oldImage) + 1)
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for x, y, col in oldImage:
        set_color(image, x, y,  col)
    
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) / 3
        brightPixel = create_color(brightness, brightness, brightness)
        set_color(image, x, y, brightPixel)
    
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
                set_color(oldImage, x, y, black)
            else:
                set_color(oldImage, x, y, white)
    
    show(oldImage)
    return oldImage
