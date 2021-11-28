
class FizzBuzz:
    def func(self, num):
        if (num % 15) == 0:
            return "FizzBuzz"
        elif (num % 5) == 0:
            return "Buzz"
        elif (num % 3) == 0:
            return "Fizz"
        elif type(num) == int:
            return "\""+str(num)+"\""
        else:
            raise Exception("Error in FizzBuzz")