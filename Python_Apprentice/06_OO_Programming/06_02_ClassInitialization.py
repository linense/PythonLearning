class Student:
    def __init__(self):
        print('Initialize called!') # Methods that start and end with __ are called "Special methods"

s1 = Student()

class newStudent:
    def __init__(self, name):
        self.name = name
        self.mail = name + "@pythonlearning.com"

ns1 = newStudent("Georg")
print(ns1.name)
print(ns1.mail)
