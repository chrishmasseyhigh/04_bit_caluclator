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


#MAin rotine goes here
data_type = user_choice()
print()

print("you chose", data_type)

print()