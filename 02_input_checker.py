#checks user choice is 'interger', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:
        
        response = "file type (interger / text / image): ".lower()
        
        if response == "text" or response =="t":
            return response
         
        else:
            print("Please choose a valid file type!")
            print()


#MAin rotine goes here
data_type = user_choice