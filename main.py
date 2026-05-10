# main module of the game
from generators.basic_math_generator import BasicMathGenerator
import datetime
import time
import math


class MathQuizGame:
    def __init__(self) -> None:
        self.generator = BasicMathGenerator()

    def main(self) -> None:
        print("To get a point - solve equation in 10s.")
        print("To exit the game - type 'quit'.\n")

        while True:
            try:
                riddle, correct_answer = self.generator.choosed_riddle()
                print(f"Find the solution to the equation: {riddle}")
                #start_timer = time.time()
                #testing print(start_timer)
                user_answer = input()
                #testing print(start_timer)
                if user_answer == "quit":
                    break
                if user_answer == "":
                    print(f"You need to give me SOME answer!\n The answer was: {correct_answer}\n")
                    time.sleep(2)
                elif int(user_answer) == correct_answer:
                    print(f"{riddle} = {user_answer}!\n Point for you!\n")
                    time.sleep(2)
                elif int(user_answer) != correct_answer:
                    print(f"The correct answer is {correct_answer}\n")
                    time.sleep(2)

            except Exception as e:
                print(f"This answer was unexpected.\n Error has accured: {e}")
                break

MathQuizGame().main()

