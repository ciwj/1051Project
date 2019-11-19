from Cimpl import *
import math

image = load_image(choose_file())

def edge_detection(image, T):
    """
    By: Navin Kangal
    Student#: 101140794
    The function determines the contrast between a pixel and the pixel below it. If the contrrast is greater than the threshold set by the user the pixel turns black. If it is lower it turns white.
    """
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) / 3
        brightPixel = create_color(brightness, brightness, brightness)
        set_color(image, x, y, brightPixel)
        
    for x in range(get_width(image)):
        for y in range(get_height(image)):
            r2, g2, b2 = get_color(image, x, y)
            brightness = r
            brightnessDown = r2
            contrast = abs(brightness - brightnessDown)
            if (contrast > T):
                set_color(image, x, y, black)
            else:
                set_color(image, x, y, white)
    
    show(image)
    return image