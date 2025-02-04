class Student:
    pass

class newStudent:
    name = ''
    score = 0
    active = True

print(type(Student))

student1 = Student()  # Create a new instance of type Student
student2 = Student()
student3 = {}
print(student1)
print(student2)
print(isinstance(student1, Student))
print(isinstance(student2, Student))
print(isinstance(student3, Student))
student1.name = "Michel"
student1.email = "michel@pythontraining.com"
print(student1.name)

newStudent1 = newStudent()
newStudent1.name = "John"
newStudent1.score = 80
newStudent1.active = False