from Cimpl import *

image = load_image(choose_file())


def test_extreme_contrast(new_image: Image) ->Image:
    """
    Navin Kangal
    101140798
    The function test whether or not each colour
    is at 0 or 255. If a pixel has a number other
    than 0 or 255 the function will return "Image
    failed test"
    """
    test = True
    for x, y, ( r, g, b) in new_image:
        red = (r == 0 or r == 255)
        green = (g == 0 or g == 255)
        blue = ( b == 0 or b == 255)
        if not (red and green and blue):
            test = False
    if test == True:
        print("Image passsed test")
    if test == False:
        print("Image failed test")
