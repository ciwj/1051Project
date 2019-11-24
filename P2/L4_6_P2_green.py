from Cimpl import *

image = choose_file()
image = load_image(image)
new_image = copy(image)


def test_green(new_image):
    """ Name: Navin Kangal
    Student#: 101140794
    Team: L4-6
    Functions test whether or not there is 
    blue or red still in any pixel in the picture.
    If there is blue or red in any pixel the 
    program will return "Image failed test" if
    the image only has green in all of its 
    pixels it will return "Image passed test".
    """
    for pixel in (new_image):
        x, y, (r, g, b) = pixel
        if r == 0 and b == 0:
            return("Image passed test")
        if r in pixel != 0 and b in pixel !=0:
            return("Image failed test")


def green_filter(image):
    """ Name: Navin Kangal
    Student#: 101140794
    Team: L4-6
    The  function will take the image uploded and
    remove the blue and red components of each pixel.
    It will then return the original image and the 
    new image with the green filter applied.
    """    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel
        new_colour = create_color(0,g,0)  # Leaves only the green in the pixel
        set_color(new_image, x, y, new_colour)
    show(image)
    show(new_image)
    return test_green(new_image)
