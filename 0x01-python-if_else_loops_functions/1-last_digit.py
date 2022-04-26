#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_string = str(number)

if (int(number_string[-1:]) > 5):
	print("Last digit of {} is {} and is greater than 5".format(number, number_string[-1:]))
elif (int(number_string[-1:]) < 6):
	print("Last digit of {} is {} and is less than 6 and not 0".format(number, number_string[-1:]))
else:
	print("Last digit of {} is {}".format(number, number_string[-1:]))
