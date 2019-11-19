def posterize_test(image):
    """Tests image to see if image is posterized. Parameter should be posterize_test(posterize(load_image(choose_file()))) in order to select a posterized image. Prints "passed" if test passed and "failed" if test failed. Created by Callum Ullrich.
    """
    posterizedimage = copy(image)
    for pixel in posterizedimage:
        chillin = True
        (x, y, (r, g, b)) = pixel
        if r >= 0 and r <= 63 and r != 31:
            chillin = False 
        if r >= 64 and r <= 127 and r != 95:
            chillin = False       
        if r >= 128 and r <= 191 and r != 159:
            chillin = False         
        if r >= 192 and r <= 255 and r != 223:
            chillin = False 
      
        if g >= 0 and g <= 63 and g != 31:
            chillin = False 
        if g >= 64 and g <= 127 and g != 95:
            chillin = False       
        if g >= 128 and g <= 191 and g != 159:
            chillin = False         
        if g >= 192 and g <= 255 and g != 223:
            chillin = False 
            
        if b >= 0 and b <= 63 and b != 31: 
            chillin = False 
        if b >= 64 and b <= 127 and b != 95:
            chillin = False       
        if b >= 128 and b <= 191 and b != 159:
            chillin = False         
        if b >= 192 and b <= 255 and b != 223:
            chillin = False           
    if chillin == True:
        print ("passed")
    if chillin == False:
        print ("failed")
