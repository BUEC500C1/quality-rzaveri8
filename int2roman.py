import pytest
 # Some of the below code was adapted from the following website
 # https://www.w3resource.com/python-exercises/class-exercises/python-class-exercise-1.php
 # user enters a number and it gets converted
 # if user does not enter a number an error pops up and it will not be accepted.
#How to make sure the user enters a number (integer) - www.101computing.net

# Below code for user input...

def int_to_Roman(number):
    while True:
        try:
           userInput = int((number))
        except ValueError:
            return "ERROR: Not an integer"
            break
        if userInput <=0:
            return "ERROR: Not a positive integer"
            break
        if userInput >99999:
            return "Enter a valid Roman Numeral or Integer from 1 to 99999"
            break
        else:
           break
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
