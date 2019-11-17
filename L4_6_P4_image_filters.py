from Cimpl import *

#image = load_image(choose_file())

def red_channel(oldImage):
    """
    Takes an image, and sets the green and blue channels to 0. Returns an image with only the red channel present.
    Parameter is a Cimpl.Image object and a Cimpl.Image object is returned.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    """
    
    image = copy(oldImage)
    for pixel in image:
        x, y, (r, g, b) = pixel
        newColor = create_color(r, 0, 0)
        set_color(image, x, y, newColor)

    show(image)
    return image

def green_channel(image):
    """ Name: Navin Kangal
    Student#: 101140794
    Team: L4-6
    The  function will take the image uploded and remove the blue and red components of each pixel.
    It will then return the original image and the new image with the green filter applied.
    """    
    new_image = copy(image)
    for pixel in image:
        x, y, (r, g, b) = pixel 
        new_colour = create_color(0,g,0)  # Leaves only the green in the pixel
        set_color (new_image, x, y, new_colour)
    
    show(new_image)
    return new_image # changed so the image would be returned - Z

def blue_channel(original_image):
    """Takes an image, and sets the green and red channels to 0. Returns an image with only the blue channel present. Parameter is a Cimpl.Image object and a Cimpl.Image object is returned. Created by Callum Ullrich.
    """
    new_image = copy(original_image) # Added this line - Z
    for pixel in original_image:
        x, y, (r, g, b) = pixel 
        new_colour = create_color(0,0,b)  # Set the pixels to only the blue channels
        set_color(new_image, x, y, new_colour)
    
    show(new_image)
    return new_image # added so the image would be returned - Z

def combine(image1, image2, image3):
    """
    Takes 3 images, each containing only the red, blue, and green channels. Returns an image containing the 3 images, combined. Images must be the same size.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    """
    for pixel1 in image1:
        x, y, (r1, g1, b1) = pixel1
        pixel2 = get_color(image2, x, y)
        pixel3 = get_color(image3, x, y)
        r2, g2, b2 = pixel2
        r3, g3, b3 = pixel3
        colour = create_color(r1 + r2 + r3, g1 + g2 + g3, b1 + b2 + b3)
        set_color(image1, x, y, colour)
    show(image1)
    return image1

def _adjust_component(comp: int) -> int:
    """
    Takes a pixel's red, green or blue component and determines what range it falls under. Based on this, it'll return 31, 95, 159, or 223. Comp should be between 0 and 255, inclusive.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>> _adjust_component(63)
    31
    >>> _adjust_component(243)
    223
    >>> _adjust_component(64)
    95
    """
    if comp <= 63:
        return 31
    elif comp <= 127:
        return 95
    elif comp <= 191:
        return 159
    else:
        return 223

def posterize(oldImage):
    """
    Takes an image and posterizes it, with the quadrants being 0-63, 64, 127, 128-191, 192-255. Takes and returns a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    """
    image = copy(oldImage)
    for pixel in image:
        x, y, (r, g, b) = pixel
        colour = create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b))
        set_color(image, x, y, colour)
    show(image)
    return image

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
    
    new_image = copy(original_image) # added - Z
    
    for pixel in original_image:     
        x, y, (r, g, b) = pixel 
        if 0 <= ((r + g + b) / 3) <= 127:
            new_colour = create_color(rr, gg, bb) 
            set_color(new_image, x, y, new_colour)
        if 128 <= ((r + g + b) / 3) <= 255:
            new_colour = create_color(rrr, ggg, bbb) 
            set_color (new_image, x, y, new_colour)
   
    show(new_image)
    return new_image # added - Z
    
def three_tone(original_image, colour1: str, colour2: str, colour3:str):
    """Takes an image, calculates the average value of the red, green, and blue colour channels. Returns a three tone image with the brightness values higher than 170 set to one colour, between 170 and 80 to another colour, and lower or equal to 80 set to another colour. Parameter is a Cimpl.Image object and three strings that are accepted colour names. Accepted cololurs include black, white, red, lime, blue, yellow, cyan, magenta, and gray. A Cimpl.Image object is returned. Created by Callum Ullrich.
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
    
    if colour3 == "black":
        rrrr = 0
        gggg = 0
        bbbb = 0
    if colour3 == "white":
        rrrr = 255
        gggg = 255
        bbbb = 255
    if colour3 == "red":
        rrrr = 255
        gggg = 0
        bbbb = 0
    if colour3 == "lime":
        rrrr = 0
        gggg = 255
        bbbb = 0
    if colour3 == "blue":
        rrrr = 0
        gggg = 0
        bbbb = 255
    if colour3 == "yellow":
        rrrr = 255
        gggg = 255
        bbbb = 0
    if colour3 == "cyan":
        rrrr = 0
        gggg = 255
        bbbb = 255
    if colour3 == "magenta":
        rrrr = 0
        gggg = 255
        bbbb = 0
    if colour3 == "gray":
        rrrr = 128
        gggg = 128
        bbbb = 128

    new_image = copy(original_image) # added - Z

    for pixel in original_image:     
        x, y, (r, g, b) = pixel 
        if 0 <= ((r + g + b) / 3) <= 84:
            new_colour = create_color(rr, gg, bb) 
            set_color (new_image, x, y, new_colour)
        if 85 <= ((r + g + b) / 3) <= 170:
            new_colour = create_color(rrr, ggg, bbb) 
            set_color (new_image, x, y, new_colour)
        if 171 <= ((r + g + b) / 3) <= 255:
            new_colour = create_color(rrrr, gggg, bbbb) 
            set_color (new_image, x, y, new_colour)
   
    show(new_image) # show new image - Z
    return new_image # added the return statement - Z


def sepia(image):
    """ 
    Navin Kangal
    101140794
    The function takes an image and then makes it graysale.
    The function then applies the sepia filter and returns the new image.
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

def extreme_contrast(image):
    """ 
    Navin Kangal
    101140798
    The function takes an image and makes each colour in each pixel either 0 or 255 to create an extreme contrast.
    """
    new_image= copy(image)
    for x, y, ( r, g, b) in image:
        red = r
        green = g
        blue = b
        if 0<=r<=127:
            red = 0           
        if 128<=r<=255:
            red = 255          
        if 0<=g<=127:
            green = 0           
        if 128<=g<=255:
            green = 255
        if 0<=b<=127:
            blue = 0            
        if 128<=b<=255:
            blue = 255
        new_colour = create_color(red, green, blue)
        set_color (new_image, x, y, new_colour)        
    show(new_image)
    return new_image

"""
red_image = red_channel(image)
green_image = green_channel(image)
blue_image = blue_channel(image)
combined_image = combine(red_image, green_image, blue_image)
posterized_image = posterize(image)
two_toned_image = two_tone(image, "magenta", "yellow")
three_toned_image = three_tone(image, "red", "lime", "blue")
sepia_image = sepia(image)
extreme_contrast_image = extreme_contrast(image)
"""
