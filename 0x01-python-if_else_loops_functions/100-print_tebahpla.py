#!/usr/bin/python3
for index in range(0, 26):
    letter = ord('z') - index
    if (index % 2 == 1):
        letter = chr(letter - ord('a') + ord('A'))
    else:
        letter = chr(letter)
    print("{}".format(letter), end='')
