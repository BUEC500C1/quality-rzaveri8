import pytest
 # Below code from
 # https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
 # user enters a number and it gets converted
 # if user does not enter a number an error pops up and it will not be accepted.
# userIn = input('Enter an integer to convert:')

#How to make sure the user enters a number (integer) - www.101computing.net






def inputNumber(message):
  while True:
    try:
       userInput = int(raw_input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    if userInput <=0:
        print("Please input a number greater than 0")
    else:
       return userInput
       break


#MAIN PROGRAM STARTS HERE:
MyNum = inputNumber("Please input integer to convert:")
