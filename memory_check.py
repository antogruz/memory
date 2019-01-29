#!/usr/bin/env python3

import random
import os
import sys

from elements import Elements
from numbers import Numbers

def main():
    assert len(sys.argv) > 1

    filename = sys.argv[1]
    if filename == "elements.txt":
        data = Elements()
    else:
        data = Numbers()

    with open(filename, "r") as fh:
        lines = data.import_lines(fh)

    random.shuffle(lines)

    while lines:
        os.system("clear")
        lines = check_all(data, lines)

def check_all(data, array):
    fails = []
    for a in array:
        if not data.check(a):
            print("Fail", a)
            fails.append(a)
    return fails

main()

