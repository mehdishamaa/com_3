

# Above we are asking for user input to choose which operation we are going to use

class Calculator:

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

print("1. Addition");
print("2. Subtraction");
print("3. Multiplication");
print("4. Division");
print("5. Exit");
operation = int(input("Enter your choice: "));


num1 = int(input("Please enter your first number:"))
num2 = int(input("Please enter your second number:"))

if operation == 1:
    print("Result = ", Calculator.add());
elif operation == 2:
    print("Result = ", Calculator.sub());
elif operation == 3:
    print("Result = ", Calculator.mul());
elif operation == 4:
    print("Result = ", Calculator.div());
elif operation == 5:
    exit();
else:
    print("Wrong input..!!");

