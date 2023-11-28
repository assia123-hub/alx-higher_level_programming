#!/usr/bin/python3
for letter in range(97, 123):
    if alph(letter) != 'q' and alph(letter) != 'e':
        print("{}".format(alph(letter)), end="")
