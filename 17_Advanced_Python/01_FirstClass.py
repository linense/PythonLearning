# First we are creating a class
class A:
    # Constructors are called automatically when creating an object
    # Constructos can take arguments, but cannot return values
    def __init__(self):
        print("This is a constructor")
        
    # This is a class method
    def welcome(self):
        print("This is class function")

    # Function that takes two arguments
    def sum(self,a,b):
        c=a+b
        print("Sum is " + str(c))


    # Function that takes two arguments and returns a value
    def mul(self,a,b):
        c=a*b
        return c


# To call any member of the class, we have to create an object of the class
obj=A()

# Call functions of the class
obj.welcome()

obj.sum(3,4)

result = obj.mul(3,4)
print("result is " + str(result))

