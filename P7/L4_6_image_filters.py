import math
from Cimpl import show, get_color, set_color, create_color, copy, Image, get_height, get_width, create_image

# Milestone 2, P5. Group L4-6.
# Submitted 27/11/19. Created by Zeyad Bakr, Callum Ullrich and Navin Kangal.


def combine(image1: Image, image2: Image, image3: Image) -> Image:
    """
    Takes 3 images, each containing only the red, blue, and green channels.
    Returns an image containing the 3 images, combined.
    Images must be the same size.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>>img = combine(redimg, blueimg, greenimg)
    """
    for pixel1 in image1:  # Adds the colours of each pixel together
        x, y, (r1, g1, b1) = pixel1
        pixel2 = get_color(image2, x, y)
        pixel3 = get_color(image3, x, y)
        r2, g2, b2 = pixel2
        r3, g3, b3 = pixel3
        colour = create_color(r1 + r2 + r3, g1 + g2 + g3, b1 + b2 + b3)
        set_color(image1, x, y, colour)
    show(image1)  # Show's the combined image
    return image1


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
        set_color(new_image, x, y, new_colour)

    show(new_image)


def red_channel(oldImage: Image) -> Image:
    """
    Takes an image, and sets the green and blue channels to 0.
    Returns an image with only the red channel present.
    Parameter is a Cimpl.Image object and a Cimpl.Image object is returned.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>>red_image = red_channel(img)
    >>>red_image2 = red_channel(img2)
    """
    image = copy(oldImage)  # Makes a copy of the uploded image and calls it image

    for pixel in image:  # For loop changes the coulour of each pixel to only its red component
        x, y, (r, g, b) = pixel
        newColor = create_color(r, 0, 0)
        set_color(image, x, y, newColor)

    show(image)  # Show's the filtered image
    return image


def _adjust_component(comp: int) -> int:
    """
    Takes a pixel's red, green or blue component and determines what range it falls under.
    Based on this, it'll return 31, 95, 159, or 223.
    Comp should be between 0 and 255, inclusive.
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
    Takes an image and posterizes it, with the quadrants being:
    0-63, 64, 127, 128-191, 192-255. Takes and returns a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student #: 101142932, Group L4-6
    >>> posterized_img = posterize(img)
    """
    image = copy(oldImage)

    # Go through every pixel, set colour to the result from _adjust_component
    for pixel in image:
        x, y, (r, g, b) = pixel
        colour = create_color(_adjust_component(r), _adjust_component(g), _adjust_component(b))
        set_color(image, x, y, colour)

    show(image)
    return image


def flip_horizontal(oldImage: Image) -> Image:
    """
    Takes a Cimpl.Image object and returns another
    Cimpl.Image object with the image horizontally flipped.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>> flip1 = flip_horizontal(img)
    >>> flip2 = flip_horizontal(img2)
    """
    image = copy(oldImage)

    # Sets pixel at (x, y) to the opposite x value
    for x, y, col in oldImage:
        set_color(image, x, get_height(image) - (y + 1), col)

    show(image)
    return image


def detect_edges_better(oldImage: Image, threshold: int):
    """
    An improved version of the detect_edges function.
    Takes a Cimpl.Image object and a positive integer between 0-255,
    returns a Cimpl.Image object.
    Created by Zeyad Bakr.
    Student # 101142932, Group L4-6.
    >>> img1 = detect_edges_better(img, 200)
    >>> img2 = detect_edges_better(img, 100)
    """
    image = create_image(get_width(oldImage) + 1, get_height(oldImage) + 1)  # Pads image
    image2 = copy(oldImage)

    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)

    # Copy image over
    for x, y, col in oldImage:
        set_color(image, x, y, col)

    # Make image grayscale
    for x, y, (r, g, b) in image:
        brightness = (r + g + b) / 3
        brightPixel = create_color(brightness, brightness, brightness)
        set_color(image, x, y, brightPixel)

    # Tests for contrast and sets colour accordingly
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
                set_color(image2, x, y, black)
            else:
                set_color(image2, x, y, white)

    show(image2)
    return image2


def three_tone(original_image, colour1: str, colour2: str, colour3: str):
    """Takes an image, calculates the average value of the red, green, and blue colour channels. Returns a three tone image with the brightness values higher than 170 set to one colour, between 170 and 80 to another colour, and lower or equal to 80 set to another colour. Parameter is a Cimpl.Image object and three strings that are accepted colour names. Accepted cololurs include black, white, red, lime, blue, yellow, cyan, magenta, and gray. A Cimpl.Image object is returned. Created by Callum Ullrich.
    """
    colour_dict = {"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0), "lime": (0, 255, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0), "cyan": (0, 255, 255), "magenta": (255, 0, 255), "gray": (128, 128, 128)}

    colour1 = colour_dict[colour1]
    colour2 = colour_dict[colour2]
    colour3 = colour_dict[colour3]

    new_image = copy(original_image)

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        if 0 <= ((r + g + b) / 3) <= 84:
            new_colour = create_color(colour1[0], colour1[1], colour1[2])
            set_color(new_image, x, y, new_colour)
        if 85 <= ((r + g + b) / 3) <= 170:
            new_colour = create_color(colour2[0], colour2[1], colour2[2])
            set_color(new_image, x, y, new_colour)
        if 171 <= ((r + g + b) / 3) <= 255:
            new_colour = create_color(colour3[0], colour3[1], colour3[2])
            set_color(new_image, x, y, new_colour)

    show(new_image)
    return new_image


def two_tone(original_image: Image, colour1: str, colour2: str):
    """Takes an image, calculates the average value of the red, green, and blue colour channels. Returns a two tone image with the brightness values higher than 127 set to one colour and lower or equal to 127 set to another colour. Parameter is a Cimpl.Image object and two strings that are accepted colour names. Accepted cololurs include black, white, red, lime, blue, yellow, cyan, magenta, and gray. A Cimpl.Image object is returned. Created by Callum Ullrich.
    """
    colour_dict = {"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0), "lime": (0, 255, 0), "blue": (0, 0, 255), "yellow": (255, 255, 0), "cyan": (0, 255, 255), "magenta": (255, 0, 255), "gray": (128, 128, 128)}

    colour1 = colour_dict[colour1]
    colour2 = colour_dict[colour2]
    new_image = copy(original_image)

    for pixel in original_image:
        x, y, (r, g, b) = pixel
        if 0 <= ((r + g + b) / 3) <= 127:
            new_colour = create_color(colour1[0], colour1[1], colour1[2])
            set_color(new_image, x, y, new_colour)
        if 128 <= ((r + g + b) / 3) <= 255:
            new_colour = create_color(colour2[0], colour2[1], colour2[2])
            set_color(new_image, x, y, new_colour)

    show(new_image)
    return new_image


def flip_vertical(oldImage: Image):
    """
    Takes a Cimpl.Image object and returns 
    another Cimpl.Image object with the image 
    vertically flipped.
    Created by Callum Ullrich.
    Student # 101148042, Group L4-6.
    >>> flip1 = flip_vertical(img)
    >>> flip2 = flip_vertical(img2)
    """
    image = copy(oldImage)

    for x, y, col in oldImage:
        set_color(image, get_width(image) - (x + 1), y, col)

    show(image)
    return image


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
        new_colour = create_color(0, g, 0)  # Leaves only the green in the pixel
        set_color(new_image, x, y, new_colour)
    show(new_image)
    return test_green(new_image)


def extreme_contrast(image: Image) -> Image:
    """
    Navin Kangal
    101140798
    The function takes an image and makes each colour in each pixel either 0 or 255 to create an extreme contrast.
    """
    new_image = copy(image)
    for x, y, (r, g, b) in image:
        red = r
        green = g
        blue = b
        if 0 <= r <= 127:
            red = 0
        if 128 <= r <= 255:
            red = 255
        if 0 <= g <= 127:
            green = 0
        if 128 <= g <= 255:
            green = 255
        if 0 <= b <= 127:
            blue = 0
        if 128 <= b <= 255:
            blue = 255
        new_colour = create_color(red, green, blue)
        set_color(new_image, x, y, new_colour)
    show(new_image)
    return new_image


def sepia(image: Image) -> Image:
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
        if g < 63:
            new_colour = create_color(r * 1.1, g, b * 0.9)
            set_color(new_image, x, y, new_colour)
        if 63 <= g <= 191:
            new_colour = create_color(r * 1.15, g, b * 0.85)
            set_color(new_image, x, y, new_colour)
        if g > 191:
            new_colour = create_color(r * 1.08, g, b * 0.93)
            set_color(new_image, x, y, new_colour)
    show(new_image)
    return(new_image)


def detect_edges(oldImage: Image, threshold: int):
    """
    By: Navin Kangal
    Student#: 101140794
    The function determines the contrast between
    a pixel and the pixel below it. If the contrrast
    is greater than the threshold set by the user the
    pixel turns black. If it is lower it turns white.
    """
    image = create_image(get_width(oldImage), get_height(oldImage) + 1)
    
    black = create_color(0, 0, 0)
    white = create_color(255, 255, 255)
    
    for x, y, col in oldImage:
        set_color(image, x, y, col)
    
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
