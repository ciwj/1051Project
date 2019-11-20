from Cimpl import *
import math

#Milestone 2, P5. Group L4-6
#Submitted 20/11/19, created by Navin Kangal

def detect_edges(oldImage: Image, threshold: int):
    """
    By: Navin Kangal
    Student#: 101140794
    The function determines the contrast between a pixel and the pixel below it. If the contrrast is greater than the threshold set by the user the pixel turns black. If it is lower it turns white.
    """
    image = create_image(get_width(oldImage), get_height(oldImage) + 1)
    
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
            brightness = r
            brightnessDown = r2
            diffDown = abs(brightness - brightnessDown)
            if (diffDown > threshold):
                set_color(oldImage, x, y, black)
            else:
                set_color(oldImage, x, y, white)
    
    show(oldImage)
    return oldImage

