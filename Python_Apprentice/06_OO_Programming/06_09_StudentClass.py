class Student:
    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
        self.__clubs = set() # because a student can belong to a club just once
        self.__active = True
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def set_gpa(self, gpa):
        self.__gpa = gpa
    
    def add_club(self, club):
        self.__clubs.add(club)
    
    def remove_club(self, club):
        self.__clubs.remove(club)
    
    def set_active(self, active):
        self.__active = True
    
    def print_details(self):
        print("Student: ", self.__name)
        print(self.__gpa, self.__clubs, self.__active)

def get_students(student_details_list):
    students_list = []
    for student_details in student_details_list:
        if 'name' not in student_details or 'gpa' not in student_details:
            continue
        s = Student(student_details['name'], student_details['gpa'])

        if 'clubs' in student_details:
            for club in student_details['clubs']:
                s.add_club(club)

        if 'active' in student_details:
            s.set_active(student_details['active'])
        
        students_list.append(s)
    return students_list

s = Student('James', 3.8)
s.add_club("Yoga")
s.print_details()

student_details_list = [
    {'name': 'Nina', 'gpa': 3.6, 'clubs': ['tennis', 'chess']},
    {'name': 'Emily', 'gpa': 3.9, 'clubs': ['tennis'], 'active': False},
    {'name': 'Michael', 'gpa': 3.2, 'clubs': ['football', 'chess']},
    {'name': 'Joe', 'gpa': 3.9, 'is_honors_student': True}
]

students = get_students(student_details_list)
#print(students)
for student in students:
    student.print_details()