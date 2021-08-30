#checks user choice is 'interger', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:
        
        response = input("File type (interger / text / image): ").lower()
        
        text_ok = [ "text","t","txt" ]
        if response in text_ok:
            return "text"
         
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