class Competition:
    raise_amount = 1.04 # This is a class variable
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize
    
    def raise_prize(self):
        self.prize = int(self.prize) * self.raise_amount

debate = Competition('Debate', 500)
print(debate.raise_amount) 
print(Competition.raise_amount)

essay = Competition('Essay', 500)
print(essay.prize)

simulation = Competition('Simulation', 100)
simulation.raise_prize
print(simulation.__dict__)
print(simulation.prize)

racing = Competition('Racing', 1000)
racing.raise_amount