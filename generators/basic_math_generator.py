#module taking responsibility for basic math riddles
import operator as op
import typing as t
import random as rd
from random import randint, choice 
from operator import mul, sub, add, truediv

MINIMUM_NUMER = 1
MAX_ADDITION_NUMER = 100
MAX_MULTIPLICATION_NUMBER = 12
MAX_SUBTRACTION_NUMBER = 100

class BasicMathGenerator:

    def __init__(self) -> None:
        pass

    def choosed_riddle(self) -> tuple[str,int]:
        """Choosing random riddle to return."""
        choosed_riddle = choice([self.riddle_multiplication, self.riddle_addition, self.riddle_subtraction])
        return choosed_riddle()

    def riddle_addition(self) -> tuple[str,int]:
        add_x:int = rd.randint(MINIMUM_NUMER, MAX_ADDITION_NUMER)
        add_y:int = rd.randint(MINIMUM_NUMER, MAX_ADDITION_NUMER)
        riddle_question:str = f"{add_x} + {add_y}"
        correct_answer:int = op.add(add_x,add_y)
        return riddle_question, correct_answer

    def riddle_subtraction(self) -> tuple[str,int]:
        sub_x:int = rd.randint(MINIMUM_NUMER, MAX_SUBTRACTION_NUMBER) # 13 gówno kurwa jebane gówno dupa
        sub_y:int = rd.randint(MINIMUM_NUMER, MAX_SUBTRACTION_NUMBER) # 63

        if sub_x <= sub_y:
            riddle_question:str = f"{sub_y} - {sub_x}"
            correct_answer:int = op.sub(sub_y,sub_x)
            return riddle_question, correct_answer
        else:
            riddle_question:str = f"{sub_x} - {sub_y}"
            correct_answer:int = op.sub(sub_x,sub_y)
            return riddle_question, correct_answer


    
    def riddle_multiplication(self) -> tuple[str, int]:

        mul_x:int = rd.randint(MINIMUM_NUMER,MAX_MULTIPLICATION_NUMBER)
        mul_y:int = rd.randint(MINIMUM_NUMER,MAX_MULTIPLICATION_NUMBER)
        riddle_question:str = f"{mul_x} * {mul_y}"
        correct_answer:int = op.mul(mul_x, mul_y)
        return riddle_question, correct_answer
    
    def riddle_division(self) -> None:
        pass