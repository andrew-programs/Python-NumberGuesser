from random import randint

# NumberGuesser Class
class NumberGuesser:
    def __init__(self, minNum: int, maxNum: int):
        self.minNum = minNum
        self.maxNum = maxNum
        self.correctNum = randint(minNum, maxNum)
    
    # Guess method that checks if the number passed in is equal to current number.
    def guess(self, num: int) -> bool:
        """Checks if the number passed in is equal to the correct number. Returns boolean value after decision."""
        
        if num == self.correctNum:
            return True
        else:
            return False
    
    # A method that returns the minimum number.
    def min(self) -> int:
        """Returns the minimum number."""
        return self.minNum
    
    # A method that returns the maximum number.
    def max(self) -> int:
        """Returns the maximum number."""
        return self.maxNum
    
    # A method that returns the correct number.
    def correct(self) -> int:
        """Returns the correct number."""
        return self.correctNum
    
    # A method that returns a range of integers around the correct number, can shrink the more it's used.
    def hint(self, hintCount: int=1) -> list[int]:
        """Gives a range of where the number is. This will shrink as more hints are used."""

        range = [(self.correctNum - round((randint(13, 20)/hintCount))),
                 (self.correctNum + round((randint(13, 20)/hintCount)))]
        
        return range

# Example Main Function
def main() -> None:
    guesser = NumberGuesser(0, 100)
    winner, guessCount, hintsUsed = False, 1, 0

    print("---------------Number Guessing Game---------------\n"
          f"Maximum Number: {guesser.max()}\n"
          f"Minimum Number : {guesser.min()}\n"
          f"Enter an integer or type 'hint' for a hint\n"
          "---------------Number Guessing Game---------------")

    while guessCount != 5 and winner != True:
        guess = input(f"Guess #{guessCount} > ")
        
        # Attempts to convert guess into an integer
        try:
            guess = int(guess)
        except Exception:
            pass

        # Checks that guess is either an integer, hint, or neither.
        if type(guess) == int:
            if guesser.guess(int(guess)):
                print("You've won!")
                winner = True
            else:
                guessCount += 1
        elif guess.lower() == "hint":
            hintsUsed += 1
            range = guesser.hint(hintsUsed)
            print(f"HINT: Number is between {range[0]} and {range[1]}")
        else:
            print("Please insert either 'hint' or an integer")

    # Checks if you've won or lost.
    if winner == True:
        winOrLose = "You've Won!"
    else:
        winOrLose = "You've Lost!"
    
    print("---------------GAME DETAILS---------------\n"
         f"{winOrLose}\n"
         f"Correct number : {guesser.correct()}\n"
         f"Hints used : {hintsUsed}\n"
         f"Guesses used : {guessCount}\n"
          "---------------GAME DETAILS---------------")

# Ensures that the main function only runs on this file in the event that someone tries to import the class.
if __name__ == "__main__":
    main()