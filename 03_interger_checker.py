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

#Main rotine goes here

keep_going = ""
while keep_going == "":
    print()

     #Checks integer
    var_integer=num_check("Please enter a integer: ", 0)
    print()

    #Checks width
    width=num_check("please enter the width:", 1)
    print()

    #Checks hight
    height=num_check("Please enter the hight:",1)
    print()