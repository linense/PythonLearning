class Employee(object):
    def __init__(self, name, base_salary):
        self.__name = name
        self.__base_salary = base_salary
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_base_salary(self):
        return self.__base_salary
    
    def set_base_salary(self, base_salary):
        self.__base_salary = base_salary

    def get_total_pay(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus):
        Employee.__init__(self, name, base_salary)
        self.__bonus = bonus
    
    def get_total_pay(self):
        return self.get_base_salary() + self.__bonus

    def get_total_pay(self, salary):
        self.__salary = salary

class ContractEmployee(Employee):
    def __init__(self, name, base_salary, overtime_pay, overtime_hours):
        Employee.__init__(self, name, base_salary)
        self.__overtime_pay = overtime_pay
        self.__overtime_hours = overtime_hours

    def get_total_pay(self):
        return self.get_base_salary + self.__overtime_pay * self.__overtime_hours

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
