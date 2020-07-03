
from MainAnimal import Animal            # Here we are importing the class from file 'Animal1'

class Humans(Animal):
    def __init__(self, gender, hunger, health, mood, employed):      # Here we add our new arguments
        super().__init__(gender, hunger, health)
        self.mood = mood
        self.employed = employed

    def meetfriends(self):
        self.mood + 5
        print("Human has met w# Here we are importing the class from file 'Animal1'ith friends and is feeling happier!")
        print(self.status())


bob = Humans("Male", 50, 30, 5, "Yes")
print(bob.time_passes())







