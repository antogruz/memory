#!/usr/bin/env python3

import random


def main():
    letters = [ [str(i), letter(i)] for i in range(1, 26) ]
    random.shuffle(letters)
    for couple in letters:
        test(couple)

def letter(n):
    return chr(ord('a') + n - 1)

def test(v):
    index = random.randint(0, len(v) - 1)
    data = v[index]
    print(data)

    for i in v:
        if i == data:
            continue
        if input() != i:
            print("Error : expected ", i)

main()

