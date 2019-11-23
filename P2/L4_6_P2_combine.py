from Cimpl import *

# Milestone 2, P5. Group L4-6.
# Submitted 20/11/19, created by Zeyad Bakr.


def combine(image1: Image, image2: Image, image3: Image) ->Image:
    """
    Takes 3 images, each containing only the red, blue, and green channels.
    Returns an image containing the 3 images, combined.
    Images must be the same size.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>>img = combine(redimg, blueimg, greenimg)
    """
    for pixel1 in image1: #Adds the colours of each pixel together
        x, y, (r1, g1, b1) = pixel1
        pixel2 = get_color(image2, x, y)
        pixel3 = get_color(image3, x, y)
        r2, g2, b2 = pixel2
        r3, g3, b3 = pixel3
        colour = create_color(r1 + r2 + r3, g1 + g2 + g3, b1 + b2 + b3)
        set_color(image1, x, y, colour)
    show(image1) #Show's the combined image
    return image1
