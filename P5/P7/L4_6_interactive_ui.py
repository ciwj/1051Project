import string
from Cimpl import load_image, choose_file, save_as
from L4_6_image_filters import *

dont_quit = True
image_loaded = False


def quit():
    print("\nTerminating program.\n")
    return False, True, None


def load_img():
    image_loaded = True
    image = load_image(choose_file())
    show(image)
    return True, True, image


def save_img():
    save_as(image)
    return True, True, image


def horizontal():
    newImage = flip_horizontal(image)
    return True, True, newImage


def vertical():
    newImage = flip_vertical(image)
    return True, True, newImage


def xtreme_contrast():
    newImage = extreme_contrast(image)
    return True, True, newImage

def tint_sepia():
    newImage = sepia(image)
    return True, True, newImage


def posterized_img():
    newImage = posterize(image)
    return True, True, newImage


def two_toned_img():
    colour1 = input("Input colour 1: ")
    colour2 = input("Input colour 2: ")
    newImage = two_tone(image, colour1, colour2)
    return True, True, newImage

def three_toned_img():
    colour1 = input("Input colour 1: ")
    colour2 = input("Input colour 2: ")
    colour3 = input("Input colour 3: ")
    newImage = three_tone(image, colour1, colour2, colour3)    
    return True, True, newImage

def edge():
    thres = int(input("Input threshold: "))
    newImage = detect_edges(image, thres)
    return True, True, newImage

def imp_edge():
    thres = int(input("Input threshold: "))
    newImage = detect_edges_better(image, thres)
    return True, True, newImage


function_dict = {'Q': quit, 'L': load_img, 'S': save_img, 'H': horizontal, 'X': xtreme_contrast, '2': two_toned_img, '3': three_toned_img, 'T': tint_sepia, 'P': posterized_img, 'E': edge, 'I': imp_edge, 'V': vertical}

# Main loop
while dont_quit:

    print("L)oad image    S)ave-as")
    print("2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize")
    print("E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip")
    command = str.upper(input("Q)uit\n\n: "))  # Ask for command input

    if command in function_dict:  # If command exists, test if there is an image
        if image_loaded or function_dict[command] == quit or function_dict[command] == load_img:
            dont_quit, image_loaded, image = function_dict[command]()
        else:
            print("\nNo image loaded.\n")
    else:  # Otherwise show there is no such command
        print("\nNo such command.\n")
