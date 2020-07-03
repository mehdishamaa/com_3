class Animal():
    hunger_decrement = 6                                                       # This line creates the class
    def __init__(self, gender, hunger, health):            # This line initialises the function with initial attributes.
        self.gender = gender                               # here we are confirming the 3 attributes
        self.hunger = hunger
        self.health = health

    def time_passes(self):
        self.hunger + 5
        print(self.status())

    def status(self):                                      # Here we create a 'status' function, showing us all an animals vital signs
        return(self.gender, self.hunger, self.health, self.mood)


    def eat(self):
        self.hunger = self.hunger - self.hunger_decrement
        print("Animal has eaten!")
        print(self.status())


human = Animal("Male", 50, 100)                            # Here we create a sub class of animal called a 'human'
                                                           # We set their variables and can call them quickly using 'human.status'

                                                           # Here we are instructing the animal to eat, decreasing their hunger by 6 points





