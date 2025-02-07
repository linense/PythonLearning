class Employee:
    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_total_pay(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, name):
        pass
    def get_total_pay(self, salary):
        self.__salary = salary

class ContractEmployee(Employee):
    def __init__(self, name):
        pass

    def get_total_pay(self, salary):
        self.__salary = salary

e = Employee("Georg")
print(e.get_name())
e.set_name("Javi")
print(e.get_name())
f = FulltimeEmployee("Vollzeit")
c = ContractEmployee("Teilzeit")
f.get_total_pay(500)
print(f.get_total_pay(500))
c.get_total_pay(300)
print(c.get_total_pay(300))
