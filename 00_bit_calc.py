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

# maine rotine goes here

#Heading
statement_generator("Bit calculator for Integers, Text & Images", "-")

#Display instructions if user has not used the program before

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
        var_integer = num_check("Enter an integer:", 0)

    # ( must be an integer more than / equal to 0)
    elif data_type == "image":
        print()
        image_width=num_check("Image width? ", 1)
        print()
        image_height=num_check("Image hight? ", 1)
        print()
    #For images, ask for width and hight
    # (must be untegers more than/ equal to 1)

    # For text, ask for a string



