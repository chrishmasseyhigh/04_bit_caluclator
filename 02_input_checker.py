#checks user choice is 'interger', 'text' or 'image'
def user_choice():
    #list of valid responces
    text_ok = [ "text","t","txt" ]
    interger_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]



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


#Main rotine goes here
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print()
    print("you chose", data_type)
    print()