#!/usr/bin/env python3
import random
import sys
import os

def main():
    assert len(sys.argv) > 1

    count = int(sys.argv[1])
    elements = []

    for i in range(count):
        elements.append(str(randomsix()))
        print(elements[-1])
        input()
        os.system("clear")

    for e in elements:
        if e != input():
            print("Error : it was", e)


def randomsix():
    return random.randint(sixdigits(), sevendigits())

def sixdigits():
    return 100000

def sevendigits():
    return sixdigits() * 10

main()
