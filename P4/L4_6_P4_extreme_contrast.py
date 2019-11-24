from Cimpl import *

image = load_image(choose_file())


def extreme_contrast(image: Image) ->Image:
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
    return test_extreme_contrast(new_image)
