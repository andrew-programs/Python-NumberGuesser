from dataclasses import dataclass
from random import randint

# NumberGuesser Class
class NumberGuesser:
    def __init__(self, minNum: int, maxNum: int):
        self.minimum, self.maximum = minNum, maxNum
        self.correctNum = randint(minNum, maxNum)
    
    def guess(self, num: int) -> bool:
        if num == self.correctNum:
            return True
        else:
            return False
    
    def min(self) -> int:
        return self.minimum
    
    def max(self) -> int:
        return self.maximum
    
    def correct(self) -> int:
        return self.correctNum
    
    def hint(self, hintsUsed: int=1) -> list[int]:
        range = [(self.correctNum - round((randint(13, 20)/hintsUsed))),
                 (self.correctNum + round((randint(13, 20)/hintsUsed)))]
        
        return range

# Main Function
def main() -> None:
    guesser = NumberGuesser(0, 100)
    winner, guessCount, hintsUsed = False, 1, 0

    print("---------------Number Guessing Game---------------\n",
          f"Maximum Number: {guesser.max()}\n",
          f"Minimum Number : {guesser.min()}\n",
          f"Enter an integer or type 'hint' for a hint\n",
          "---------------Number Guessing Game---------------")

    while winner != True and guessCount <= 5:
        guess = input(f"Guess #{guessCount} > ")
        if guess.lower() == "hint":
            hintsUsed += 1
            range = guesser.hint()
            print(f"HINT: Number is between {range[0]} and {range[1]}")
        else:
            try:
                if guesser.guess(int(guess)):
                    print("You've won!")
                    winner = True
                else:
                    guessCount += 1
            except:
                print("Please insert either hint or an integer")

    if winner == True:
        winOrLose = "You've Won!"
    else:
        winOrLose = "You've Lost!"
    
    print("---------------GAME DETAILS---------------\n",
         f"{winOrLose}\n",
         f"Correct number : {guesser.correct()}\n",
         f"Hints used : {hintsUsed}\n",
         "----------------GAME DETAILS---------------")
    
if __name__ == "__main__":
    main()