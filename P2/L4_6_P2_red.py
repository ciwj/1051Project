from Cimpl import *

# Milestone 1, P2. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.


def red_channel(oldImage):
    """
    Takes an image, and sets the green and blue channels to 0.
    Returns an image with only the red channel present.
    Parameter is a Cimpl.Image object and a Cimpl.Image object is returned.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>>red_image = red_channel(img)
    >>>red_image2 = red_channel(img2)
    """
    image = copy(oldImage)
    
    for pixel in image:
        x, y, (r, g, b) = pixel
        newColor = create_color(r, 0, 0)
        set_color(image, x, y, newColor)
    
    show(image)
    return image
