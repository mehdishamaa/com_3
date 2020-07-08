

# Above we are asking for user input to choose which operation we are going to use

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def mul(self, num1, num2):
        return num1 * num2

    def sub(self, num1, num2):
        return num1 - num2

    def div(self, num1, num2):
        return num1 / num2


calc = Calculator()