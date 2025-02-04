class Student:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = first + "." + last + "@pythonlearning.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def uppercase(self):
        self.first = self.first.upper()
        self.last = self.last.upper()
    

s1 = Student('Gregorio', 'Loriguillo')
print(s1.fullname())
#del s1.first
print(s1.first)

s2 = Student('John', 'Doe')
print(s2.fullname())
s2.uppercase()
print(s2.fullname())
print(s2.first)