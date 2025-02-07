class Competition:
    __raise_amount = 1.10

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def get_name(self):
        return self.__name
    
    def get_prize(self):
        return self.__prize
    
    def raise_prize(self):
        self.__prize = self.__prize * self.__raise_amount

class Sprint(Competition):
    pass

race = Competition('Race', 100)
#print(type(race))
#print(help(Competition))
#print(help(Sprint))
sprint = Sprint('100m', 700)
print(sprint.get_prize())
print(sprint.get_name())
sprint.raise_prize()
print(sprint.get_prize())