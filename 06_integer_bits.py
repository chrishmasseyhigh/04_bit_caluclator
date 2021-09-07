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

# Main routine
int_bits()
