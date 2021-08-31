#functions go here


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

# cheeks user choice is int, text or img
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

# maine rotine goes here
statement_generator("look stars", "*")

#Heading
statement_generator("Bit calculator for Integers, Text & Images", "-")

#Display instructions if user has not used the program before

# Loop to alow putiple calculations
keep_going = ""
while keep_going == "":
    #ask the user for the file type
    data_type= user_choice()
    print("you chose", data_type)

