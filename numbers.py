#!/usr/bin/env python3

import random
import os

filename = "numbers.txt"
def main():
    with open(filename, "r") as fh:
        lines = import_lines(fh)

    random.shuffle(lines)

    while lines:
        os.system("clear")
        lines = check_all(lines)

def import_lines(fh, n = 99999):
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
