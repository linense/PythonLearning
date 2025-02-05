class Dog:
    def __init__(self, name, breed):
        self.__name = name # underscores are a hack to make the variable private (Python does not prvent it, though)
        self.__breed = breed

    def print_details(self):
        print("My name is %s and I am a %s" % (self.__name, self.__breed))

    def change_name(self, name):
        self.__name = name

class NewDog:
    """ This is a class which defines a dog.
        This includes cute dogs as well as ferocious dogs
    """
    __species = 'canine'
    def __init__(self, name, breed):
        self.__name = name # underscores are a hack to make the variable private (Python does not prvent it, though)
        self.__breed = breed
        self.__tricks = []

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_breed(self):
        return self.__breed
    
    def set_breed(self, breed):
        self.__breed = breed

    def add_trick(self, trick):
        self.__tricks.append(trick)

    def print_details(self):
        print("My name is %s and I am a %s " % (self.__name, self.__breed,))
        print("Here are the tricks that I can do: ", self.__tricks)

dog1 = Dog("Moje", "Golden Retriever")
dog1.print_details()
dog1.change_name("Oba")
dog1.print_details()

dog2 = NewDog("Oba", "Labrador")
dog2.add_trick("roll over")
dog2.print_details()
dog2.set_breed("Schnauzer")
dog2.print_details()