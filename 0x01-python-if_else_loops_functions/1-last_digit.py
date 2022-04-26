#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)
ld = number_string[-1:]

if (int(ld) == 0):
    print("Last digit of {} is {} and is 0".format(number, ld))
elif (int(ld) > 5):
    if (number < 0):
        print("Last digit of {} is -{} and is less than 5".format(number, ld))
    else:
        print("Last digit of {} is {} and is greater than 5".format(number, ld))
elif (int(ld) < 6):
    if (number < 0 and int(ld) != 0):
        print("Last digit of {} is -{} and is less than 6 and not 0".format(number, ld))
    elif (number > int(ld) != 0):
        print("Last digit of {} is {} and is less than 6 and not 0".format(number, ld))
