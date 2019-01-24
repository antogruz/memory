#!/usr/bin/env python3

import random
import os

def main():
    with open("numbers.txt", "r") as fh:
        couples = import_couples(fh)

    random.shuffle(couples)

    while couples:
        os.system("clear")
        couples = check_all(couples)

def import_couples(fh, n = 99999):
    couples = []
    i = 0

    for line in fh.readlines():
        couples.append((i, line.rstrip()))
        i += 1
        if i >= n:
            break

    return couples

def check_all(array):
    fails = []
    for a in array:
        if not check(a):
            print("Fail", a)
            fails.append(a)
    return fails


def check(couple):
    print(couple[0])
    return input() == couple[1]


from datetime import datetime
random.seed(datetime.now())
main()
