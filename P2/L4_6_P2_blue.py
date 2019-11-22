from Cimpl import *

# Assumption: There is a image stored in the same folder as this script
#  with the given name
FILENAME = choose_file()

original_image = load_image(FILENAME)

new_image = copy(original_image)


def blue_filter(original_image):
    """
    Takes an image, and sets the 
    green and red channels to 0. 
    Returns an image with only 
    the blue channel present. 
    Parameter is a Cimpl.Image object
    and a Cimpl.Image object is returned.
    Created by Callum Ullrich.
    """    
    
    for pixel in original_image:
        x, y, (r, g, b) = pixel 
        new_colour = create_color(0, 0, b)  # Set the pixels to only the blue channels
        set_color (new_image, x, y, new_colour)
   
    show( original_image )
    show( new_image )

