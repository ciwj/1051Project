import string
from typing import Tuple
from Cimpl import load_image, choose_file, save_as
from L4_6_image_filters import *

dont_quit = True
image_loaded = False


def quit() -> Tuple[bool, bool, Image]:
    """
    Sets the dont_quit variable to False, ending the main loop, and prints as such.
    """
    print("\nTerminating program.\n")
    return False, True, None # Set dont_quit to False, ending the main loop


def load_img() -> Tuple[bool, bool, Image]:
    """
    Prompts the user to input an image. Returns the dont_quit variable as True, image_loaded as True, and the image chosen.
    """
    image = load_image(choose_file())
    show(image)
    return True, True, image


def save_img() -> Tuple[bool, bool, Image]:
    """
    Prompts the user to save the image. Returns the dont_quit variable as True, image_loaded as True, and the same image that was saved.
    """
    save_as(image)
    return True, True, image


def horizontal() -> Tuple[bool, bool, Image]:
    """
    Runs the flip_horizontal filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """
    newImage = flip_horizontal(image)
    return True, True, newImage


def vertical() -> Tuple[bool, bool, Image]:
    """
    Runs the flip_vertical filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    newImage = flip_vertical(image)
    return True, True, newImage


def xtreme_contrast() -> Tuple[bool, bool, Image]:
    """
    Runs the extreme_contrast filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    newImage = extreme_contrast(image)
    return True, True, newImage


def tint_sepia() -> Tuple[bool, bool, Image]:
    """
    Runs the sepia filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    newImage = sepia(image)
    return True, True, newImage


def posterized_img() -> Tuple[bool, bool, Image]:
    """
    Runs the posterize filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    newImage = posterize(image)
    return True, True, newImage


def two_toned_img() -> Tuple[bool, bool, Image]:
    """
    Runs the two_tone filter with yellow and cyan and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    colour1 = "yellow"
    colour2 = "cyan"
    newImage = two_tone(image, colour1, colour2)
    return True, True, newImage


def three_toned_img() -> Tuple[bool, bool, Image]:
    """
    Runs the three_tone filter with yellow, magenta, and cyan and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    colour1 = "yellow"
    colour2 = "magenta"
    colour3 = "cyan"
    newImage = three_tone(image, colour1, colour2, colour3)
    return True, True, newImage


def edge() -> Tuple[bool, bool, Image]:
    """
    Runs the detect_edges filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    thres = int(input("Input threshold: "))
    newImage = detect_edges(image, thres)
    return True, True, newImage


def imp_edge() -> Tuple[bool, bool, Image]:
    """
    Runs the detect_edges_better filter and returns the dont_quit variable as True, image_loaded as True, and the filtered image.
    """    
    thres = int(input("Input threshold: "))
    newImage = detect_edges_better(image, thres)
    return True, True, newImage


function_dict = {'Q': quit, 'L': load_img, 'S': save_img, 'H': horizontal, 'X': xtreme_contrast, '2': two_toned_img, '3': three_toned_img, 'T': tint_sepia, 'P': posterized_img, 'E': edge, 'I': imp_edge, 'V': vertical} # Dictionary relating the input command with their respective functions

# Main loop
while dont_quit:
    # Print main menu
    print("L)oad image    S)ave-as")
    print("2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize")
    print("E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip")
    command = str.upper(input("Q)uit\n\n: "))  # Ask for command input

    if command in function_dict:  # If command exists, test if there is an image
        if image_loaded or function_dict[command] == quit or function_dict[command] == load_img: # Only run command if an image is loaded, or if the function is load_image or quit
            # Run command, return appropriate return values - stop program, whether img is loaded, and the returned image
            dont_quit, image_loaded, image = function_dict[command]()
        else:
            print("\nNo image loaded.\n") # If no image is loaded, say so
    else:  # Otherwise show there is no such command
        print("\nNo such command.\n")
