# Required arguments
def takeInput(a,b):
    c=a+b
    print("Sum of values is " + str(c))

# Keyword arguments
def takeMyInput(a,b):
    c=a+b
    print("Sum of values is " + str(c))

# Default argument
# Beware: After a default argument there must be no required argument
def takeDefArgument(a,b=10):
    "First line is just for commenting purposes! No # needed!"
    c=a+b
    print("Sum of values is " + str(c))    

takeInput(10,20)
takeMyInput(b=20,a=100)
takeDefArgument(10)