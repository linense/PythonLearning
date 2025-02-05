class Competition:
    participants = [] # Class variable
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize

debate = Competition('Debate', 500)
#print(debate.participants)
essay = Competition('Essay', 400)


Competition.participants.append('John')
Competition.participants.append('Alice')
print(Competition.participants)
print(debate.participants)
print(essay.participants)
debate.participants.append('Lily')
print(debate.participants)
print(essay.participants)
print(Competition.__dict__)