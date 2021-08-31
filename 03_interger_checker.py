#checks input is a number more than zero
def num_check(question, low):
    valid = False
    while not valid:
        
        error = "please enter a integer that is more than"
        "(or equal to) {}".format(low)

                                                                         
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
            print(error)

