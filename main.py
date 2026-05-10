# main module of the game
from generators.basic_math_generator import BasicMathGenerator
import time
import os
import subprocess
import sys

class MathQuizGame:

    def __init__(self) -> None:
        self.generator = BasicMathGenerator() 
        self.clear_console()
        self.state = "START"

    def main(self) -> None:
            while True:
                if self.state == "START":

                    print("To get a Point - Solve Equation in 5s.")
                    print("Extra Point if you Solve it in 3s!")
                    print("To Exit The Game at any point type -> [quit] <-.\n")

                    print("Are you Ready?\n Type [start] to Begin!")
                    user_input = input()

                    if user_input == "quit":
                        self.clear_console()
                        print("\nQuiting the Game...")
                        time.sleep(1)
                        break

                    elif user_input != "start":
                        print(f"Well -> {user_input} <- that's not [start]\n")
                        time.sleep(3)
                        self.clear_console()

                    elif user_input == "start":
                        self.state = "GAME"
                        points = 0
                        riddle_count = 0
                        self.clear_console()

                elif self.state == "GAME":
                    try:    
                        # generating random basic math riddle
                        riddle, correct_answer = self.generator.choosed_riddle()
                        print(f"Find the solution to the equation: {riddle}")
                        riddle_count += 1

                        #colecting time on the beginning of riddle
                        start_time = int(time.time())
                        user_answer = input()
                        #time after user input
                        end_time = int(time.time())
                        answer_time = end_time - start_time

                        if str(user_answer) == "quit":
                            print("Exiting to Main Menu...")
                            time.sleep(1)
                            self.clear_console()
                            self.state = "START"

                        elif user_answer == "":
                            print(f"\n The answer was: {riddle} = {correct_answer}\n")
                            time.sleep(3)
                            self.clear_console()

                        elif int(user_answer) == correct_answer:
                            print(f"{riddle} = {user_answer}!\n That's correct asnwer!")                                    
                            if answer_time <= 3:
                                points +=3
                                print(f"\nFlasHhhH! That's what we call SPEEEEEEED.\n Get 2 points for that!")
                            elif answer_time <= 5:
                                points += 2
                                print(f"\nGrab a point for beeing quick.\n Your current points are: {points}.\n Keep it up!") 
                            elif answer_time <= 7:
                                print("\nCome on! You can do better then that!")
                                points += 1
                            elif answer_time <= 10:
                                print("\nIs it a joke? We have a lot of work to do...")
                            elif answer_time <= 15:
                                print("\nHopefully coffee is done.\n Shall we continue?")
                            time.sleep(3)
                            self.clear_console()

                        elif int(user_answer) != correct_answer:
                            print(f"\n {riddle} = {correct_answer} Incorrect! \n Prepare for next one!\n")
                            print(f"Your score at this point is {points} points.")
                            time.sleep(3)
                            self.clear_console()
                        
                        if riddle_count == 20:
                            self.clear_console()
                            print(f"You've got {points} / 60. Good Job!\n Keep it up!")
                            time.sleep(5)
                            self.clear_console()
                            self.state = "START"

                    except ValueError as e:
                        print(f"\n{riddle} = {correct_answer}\n")
                        print("Answer must be Number!")
                        if riddle_count > 0:
                            riddle_count -= 1
                        time.sleep(3)
                        self.clear_console()
    
    def clear_console(self) -> None:
        command = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(command, shell=True)


MathQuizGame().main()


