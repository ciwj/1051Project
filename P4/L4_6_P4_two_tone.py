from Cimpl import *

# Assumption: There is a image stored in the same folder as this script
#  with the given name
FILENAME = choose_file()

original_image = load_image(FILENAME)

new_image = copy(original_image)



def two_tone(original_image, colour1: str, colour2: str):
    """Takes an image, calculates the average value of the red, green, and blue colour channels. Returns a two tone image with the brightness values higher than 127 set to one colour and lower or equal to 127 set to another colour. Parameter is a Cimpl.Image object and two strings that are accepted colour names. Accepted cololurs include black, white, red, lime, blue, yellow, cyan, magenta, and gray. A Cimpl.Image object is returned. Created by Callum Ullrich.
    """
    if colour1 == "black":
        rr = 0
        gg = 0
        bb = 0
    if colour1 == "white":
        rr = 255
        gg = 255
        bb = 255
    if colour1 == "red":
        rr = 255
        gg = 0
        bb = 0
    if colour1 == "lime":
        rr = 0
        gg = 255
        bb = 0
    if colour1 == "blue":
        rr = 0
        gg = 0
        bb = 255
    if colour1 == "yellow":
        rr = 255
        gg = 255
        bb = 0
    if colour1 == "cyan":
        rr = 0
        gg = 255
        bb = 255
    if colour1 == "magenta":
        rr = 0
        gg = 255
        bb = 0
    if colour1 == "gray":
        rr = 128
        gg = 128
        bb = 128
        
    if colour2 == "black":
        rrr = 0
        ggg = 0
        bbb = 0
    if colour2 == "white":
        rrr = 255
        ggg = 255
        bbb = 255
    if colour2 == "red":
        rrr = 255
        ggg = 0
        bbb = 0
    if colour2 == "lime":
        rrr = 0
        ggg = 255
        bbb = 0
    if colour2 == "blue":
        rrr = 0
        ggg = 0
        bbb = 255
    if colour2 == "yellow":
        rrr = 255
        ggg = 255
        bbb = 0
    if colour2 == "cyan":
        rrr = 0
        ggg = 255
        bbb = 255
    if colour2 == "magenta":
        rrr = 0
        ggg = 255
        bbb = 0
    if colour2 == "gray":
        rrr = 128
        ggg = 128
        bbb = 128

    for pixel in original_image:     
        x, y, (r, g, b) = pixel 
        if 0 <= ((r + g + b) / 3) <= 127:
            new_colour = create_color(rr, gg, bb) 
            set_color (new_image, x, y, new_colour)
        if 128 <= ((r + g + b) / 3) <= 255:
            new_colour = create_color(rrr, ggg, bbb) 
            set_color (new_image, x, y, new_colour)
   
    show( original_image ) 
    show( new_image )