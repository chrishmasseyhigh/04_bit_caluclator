#checks input is a number more than zero
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "please enter a integer that is more than (or equal to) {}".format(low)
        error2= "please enter a integer that does not have decimal part / enter a number".format(low)
                                                                         
        try:
        
            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if response >= low:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error2)


# Finds # of bits for 24 bit colour
def image_bits():
    
    # Calculate pixels
    var_height = num_check("Image height? ", 0)
    print()
    var_width = num_check("Image width? ", 0)
    print()

    # Calculate width times hight
    num_pixels  = var_height*var_width

    # Calculate the total number of bits
    total_bits = num_pixels * 24

    # Show the calculations
    print()
    print("# Number of pixels, {} * {} = {}".format(var_height, var_width, num_pixels))
    
    print("# Number of bits, {} x 24 = {}".format(num_pixels, total_bits))
    print()
    
    return ""

#Main rotine goes here
image_bits()