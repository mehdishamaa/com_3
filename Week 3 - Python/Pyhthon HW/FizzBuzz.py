class FizzBuzz:
    def fizzbuzz(self):
        for n in range(1, 101):
            print(n)
            if n % 3 and n % 5 == 0:
                print("FizzBuzz")
            elif n % 3 == 0:
                print("Fizz")
            elif n % 5 == 0:
                print("Buzz")


TestFunction = FizzBuzz()
TestFunction.fizzbuzz()
