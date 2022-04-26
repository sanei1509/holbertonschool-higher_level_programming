#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
ld = number_string[-1:]

if (int(ld) < 6):
    if (number < 0 and int(ld) != 0):
        print(f"Last digit of {number} is -{ld} and is less than 6 and not 0")
    elif (number > int(ld) != 0):
        print(f"Last digit of {number} is {ld} and is less than 6 and not 0")
elif (int(ld) > 5):
    if (number < 0):
        print(f"Last digit of {number} is -{ld} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {ld} and is greater than 5")
if (int(ld) == 0):
	print(f"Last digit of {number} is {ld} and is 0")
	
