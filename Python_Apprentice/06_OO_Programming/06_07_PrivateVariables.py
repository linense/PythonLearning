class Dog:
    def __init__(self, name, breed):
        self.__name = name # underscores are a hack to make the variable private (Python does not prvent it, though)
        self.__breed = breed

    def print_details(self):
        print("My name is %s and I am a %s" % (self.__name, self.__breed))

dog1 = Dog("Moje", "Golden Retriever")
dog1.print_details()
print(dog1.__dict__)