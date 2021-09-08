#Functions go here

#Put series of symbols at sart and end of text
def statement_generator(text, decoration):

    #make string with 5 characters
    ends = decoration * 5

    #add decoration to sart of the statement
    statement ="{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

#Checks user choice is int, text or img
def user_choice():
    #list of valid responces
    text_ok = [ "text","t","txt" ]
    interger_ok = ["integer", "int", "#", "number"]
    image_ok = ["image","p", "img", "pix", "picture", "pic",]



    valid = False
    while not valid:
        
        response = input("File type (interger / text / image): ").lower()
        
        if response in text_ok:
            return "text"

        elif response in interger_ok:
            return "integer"

        elif response in image_ok:
            return "image" 
        
        elif response == "i":
            want_integer = input("press <enter> for an interger or any key for a image")
            if want_integer =="":
                return "interger"
            else:
                return "image"
        
        else:
            print()
            print("Please choose a valid file type!")
            print()

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

# calculates # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string...
    var_text = input("Enter some text: ")

    # calculate # of bits (lenth of a string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # output answer with working
    print()
    print("\'{}\' has {} characters ..". format(var_text, var_length))
    print("# of bits is {} x 8".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_text))
    print()

    return ""

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

# converst decimal to bianary and states how
# many bits are neeeded to represent the origanal intieger
def int_bits():


    # get integer
    var_integer = num_check("Please enter an integer: ",0)



    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))

    return ""

# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print("Please choose a data type (image/ text / integer)")
    print()
    print("This program assumes that images are being represented in 24 bit colour (ie:24 bits per pixel). For , we assume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return

# maine rotine goes here

#Heading
statement_generator("Bit calculator for Integers, Text & Images", "-")

#Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time =="":
    instructions()

# Loop to alow putiple calculations
keep_going = ""
while keep_going == "":
    
    #ask the user for the file type
    data_type= user_choice()
    print()
    print("you chose", data_type)
    print()

    # For integers, ask for integer
    if data_type=="integer":
        int_bits()
    
    
    #For images, ask for width and hight
    # (must be untegers more than/ equal to 1)
    elif data_type == "image":
        image_bits()
    
    # For text, ask for a string
    else:
       text_bits()

    print()
    keep_going = input ("Press <enter> to continue or any key to quit")
    print()
