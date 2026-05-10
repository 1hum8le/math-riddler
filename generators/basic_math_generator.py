#module taking responsibility for basic math riddles
import operator as op
import typing as t
import random as rd
from random import randint, choice 
from operator import mul, sub, add, truediv

MINIMUM_NUMER = 1

MAX_MULTIPLICATION_NUMBER = 12

class BasicMathGenerator:

    def __init__(self) -> None:
        pass

    def choosed_riddle(self) -> tuple[str,int]:
        """Choosing random riddle to return."""
        choosed_riddle = choice([self.riddle_multiplication])
        return choosed_riddle()

    def riddle_addition(self) -> None:
        pass
    def riddle_subtraction(self) -> None:
        pass
    
    def riddle_multiplication(self) -> tuple[str, int]:

        mul_x = rd.randint(MINIMUM_NUMER,MAX_MULTIPLICATION_NUMBER)
        mul_y = rd.randint(MINIMUM_NUMER,MAX_MULTIPLICATION_NUMBER)
        riddle_question:str = f"{mul_x} * {mul_y}"
        correct_answer:int = op.mul(mul_x, mul_y)
        return riddle_question, correct_answer
    
    def riddle_division(self) -> None:
        pass