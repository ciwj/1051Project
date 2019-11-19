from Cimpl import *

image = load_image(choose_file())

def sepia(image):
    """ 
    Navin Kangal
    101140794
    The function takes an image and then makes it graysale.
    The function then applys the sepia filter and returns the new image.
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) // 3        
        gray = create_color(brightness, brightness, brightness)
        set_color(new_image, x, y, gray)
    for x, y, (r, g, b) in new_image:
        if g<63:
            new_colour = create_color(r*1.1, g, b*0.9)
            set_color (new_image, x, y, new_colour)
        if 63<=g<=191:
            new_colour = create_color(r*1.15, g, b*0.85)
            set_color (new_image, x, y, new_colour)            
        if g>191:
            new_colour = create_color(r*1.08, g, b*0.93)
            set_color (new_image, x, y, new_colour)
    show(new_image)
    return(new_image)