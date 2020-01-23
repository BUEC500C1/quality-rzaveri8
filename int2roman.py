import pytest
 # Below code from
 # https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
 # user enters a number and it gets converted
 # if user does not enter a number an error pops up and it will not be accepted.
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

def int_to_Roman(number):
    #roman_num = number
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    temp_num = number
    while  temp_num > 0:
        for _ in range(temp_num // val[i]):
            roman_num += syb[i]
            temp_num -= val[i]
        i += 1
    return roman_num

#check_input(userIn)
print 'The Converted Number Is:', int_to_Roman(MyNum)
