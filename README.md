## About NumberGuesser.py ##
This is a simple number guessing class that takes in a minimum and maximum value and generates a number that a user can attempt to guess using the guess method.

## Getting Started ##
To get started, initialize the logger object while passing in the **min number** and the **max number**.<br />
`guesser = NumberGuesser(minNum, maxNum)`

## Object Methods ##

### Guessing ###
`guesser.guess(num)`<br />
The guesser will compare the num passed into this method to the correct number. If it is equal, it returns True, otherwise, it returns False.

### Giving Hints ###
`guesser.hint(hintsCount)` <br />
The guesser takes in an optional argument of hintCount that will shrink the range the higher that value increase. This will return the range of numbers that the correct number is in.

### Retrieving Minimum Value ###
`guesser.min()`<br />
The guesser will return the minimum value that was passed during initialization.

### Retrieving Maximum Value ###
`guesser.max()`<br />
The guesser will return the maximum value that was passed during initialization.

### Retrieving Correct Value ###
`guesser.correct()`<br />
The guesser will return the correct value that was generated during initialization.

### EXAMPLE ###
There is a main function within the file that will not be ran outside of its main file. You can view it as an example of the class being used.