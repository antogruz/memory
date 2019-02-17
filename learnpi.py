#!/usr/bin/env python3

from pi import pi
import sys

def main():
    if len(sys.argv) == 1:
        start = 0
    else:
        start = int(sys.argv[1])

    cmd = ""
    while cmd == "":
        show_six_digits(start)
        start += 6
        cmd = input()


def show_six_digits(start):
    decimal_index = 2
    print(sub(pi, start + decimal_index, 6))

def sub(string, start, size):
    return string[start : start + size]

main()
