#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    l_digit = number % (-10)
else:
    l_digit = number % 10

if (l-digit < 6):
    print(f"Last digit of {number} is {l_digit} and is less than 6 and not 0")
elif (l-digit > 5):
    print(f"Last digit of {number} is {l_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {l_digit} and is 0")
