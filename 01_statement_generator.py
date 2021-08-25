#functions go here

#Put series of symbols at sart and end of text
def statement_generator(text, decoration):

    #make string with 5 characters
    ends = decoration * 5

    #add decoration to sart of the statement
    statement ="{}  {}  {}".formant(ends, text, ends)

    print()
    print(statement)
    print()

    return ""

# maine rotine goes here
statement_generator("hello world", "-")
