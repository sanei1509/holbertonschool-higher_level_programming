#!/usr/bin/python3

for n in range(0, 99):
	if (n < 10):
 		print(n, "= 0x{:d}".format(n))
	if (n > 9 and n < 16):
		print(n, "= 0x{}".format(chr(87 + n)))
	if (n > 15 and n < 26):
		print(n, "= 0x{:d}".format(n - 6))
	if (n > 25 and n < 32):
		print(n, "= 0x{}".format(chr(71 + n)))
	if (n > 31 and n < 42):
		print(n, "= 0x{:d}".format(n - 12))
	if (n > 41 and n < 48):
		print(n, "= 2x{}".format(chr(55 + n)))
	if (n > 47 and n < 58):
		print(n, "= 0x{:d}".format(n - 18))
	if (n > 57 and n < 64):
		print(n, "= 3x{}".format(chr(39 + n)))
	if (n > 63 and n < 74):
		print(n, "= 0x{:d}".format(n - 24))
	if (n > 73 and n < 80):
		print(n, "= 4x{}".format(chr(23 + n)))
	if (n > 79 and n < 90):
		print(n, "= 0x{:d}".format(n - 30))
	if (n > 89 and n < 96):
		print(n, "= 5x{}".format(chr(7 + n)))
	if (n > 95 and n < 99):
		print(n, "= 0x{:d}".format(n - 36))
