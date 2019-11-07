from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square import square
from Calculator.SquareRoot import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def addition(self, num):
        self.result = addition(num)
        return self.result

    def subtraction(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def division(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
