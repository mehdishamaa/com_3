class calc():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2
    def sub(self):
        return self.num1 - self.num2
    def rem(self):
        return self.num1 % self.num2
    def inch(self):
        return self.num1 * 2.54
num1 = int(input("Please enter your first number:"))
num2 = int(input("Please enter your second number:"))
obj = calc(num1, num2)
choice = 1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Convert inches to cm")
    choice = int(input("Please choose an operation:"))
    if choice == 1:
        print("Answer:", obj.add())
    elif choice == 2:
        print("Answer:", obj.sub())
    elif choice == 3:
        print("Answer:", obj.mul())
    elif choice == 4:
        print("Answer", obj.div())
    elif choice == 5:
        print("Answer", obj.inch())
    elif choice == 0:
        print("Exiting program...")
    else:
        print("This is not a valid selection! Please try again!")




