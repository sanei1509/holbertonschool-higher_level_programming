#!/usr/bin/python3

for num in range(0, 99):
	if (num < 10):
 		print(num, "= 0x{:d}".format(num))
	if (num > 9 and num < 16):
		print(num, "= 0x{}".format(chr(87 + num)))
	if (num > 15 and num < 26):
		print(num, "= 0x{:d}".format(num - 6))
	if (num > 25 and num < 32):
		print(num, "= 0x{}".format(chr(71 + num)))
	if (num > 31 and num < 42):
		print(num, "= 0x{:d}".format(num - 12))
	if (num > 41 and num < 48):
		print(num, "= 2x{}".format(chr(55 + num)))
	if (num > 47 and num < 58):
		print(num, "= 0x{:d}".format(num - 18))
	if (num > 57 and num < 64):
		print(num, "= 3x{}".format(chr(39 + num)))
	if (num > 63 and num < 74):
		print(num, "= 0x{:d}".format(num - 24))
	if (num > 73 and num < 80):
		print(num, "= 4x{}".format(chr(23 + num)))
	if (num > 79 and num < 90):
		print(num, "= 0x{:d}".format(num - 30))
	if (num > 89 and num < 96):
		print(num, "= 5x{}".format(chr(7 + num)))
	if (num > 95 and num < 99):
		print(num, "= 0x{:d}".format(num - 36))
