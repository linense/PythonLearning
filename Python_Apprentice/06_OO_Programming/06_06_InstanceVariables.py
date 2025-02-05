class Competition:
    def __init__(self, name, prize):
        self.name = name
        self.prize = prize
        self.participants = []
    
debate = Competition('Debate', 500)
print("Participants in the debate competition: " + str(debate.participants))
debate.participants.append('Alice')
print("Participants in the debate competition: " + str(debate.participants))

essay = Competition('Essay', 456)
print("Participants in the essay competition: " + str(essay.participants))
essay.participants.append('Michael')
print("Participants in the essay competition: " + str(essay.participants))
print(Competition.__dict__)