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

s = Student('James', 3.8)
s.add_club("Yoga")
s.print_details()