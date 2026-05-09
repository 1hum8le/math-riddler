#module taking responsibility for basic math riddles
import operator as op
import typing as t
import random as rd
from random import randint, choice 
from operator import mul, sub, add, truediv

MAX_MULTIPLICATION_NUMBER = 13

class BasicMathGenerator:

    def __init__(self) -> None:

        #generating random multiplication numbers
        self.max_mul_num = MAX_MULTIPLICATION_NUMBER

    def generate_riddle(self) -> None:
        """Generating numbers and type of a operation."""
        pass

    def riddle_addition(self) -> None:
        pass
    def riddle_subtraction(self) -> None:
        pass
    
    def riddle_multiplication(self) -> tuple[(int|int)] | t.Any:

        self.mul_x = rd.randint(1,MAX_MULTIPLICATION_NUMBER)
        self.mul_y = rd.randint(1,MAX_MULTIPLICATION_NUMBER)
        print(f"Find the solution to the equation: {self.mul_x} * {self.mul_y}")
        correct_answer = op.mul(self.mul_x,self.mul_y)
        answer = input()
        
        if answer == correct_answer:
            print("This is correct answer!")
        elif answer != correct_answer:
            print(f"The correct answer is {correct_answer}")
        

    def riddle_division(self) -> None:
        pass
    
    # def testing(self) -> t.Any:
    #     pass
        
print(BasicMathGenerator().riddle_multiplication())