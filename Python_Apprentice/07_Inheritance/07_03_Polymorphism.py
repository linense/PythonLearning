class Hominidae():
    def communication(self):
        print("They use auditory calls and visual cues.")

    def walk(self):
        print("They are knuckle-walkers, used to hang and swing from one tree to another.")

class Human(Hominidae):
    def communication(self):
        print("They use language to communicate.")
    
    def walk(self):
        print("They are bipeds.")

class Gorilla(Hominidae):
    def communication(self):
        print("They use twenty-five distinct vocalizations to communicate.")
    
    def walk(self):
        print("They are knuckle-walkers.")

hominidae_1 = Hominidae() # Base class
human_1 = Human()
gorrilla_1 = Gorilla()

hominidae_1.communication()
human_1.communication()
gorrilla_1.communication()

gorrilla_1.walk()