#!/usr/bin/env python3

import random

class Elements():
    def import_lines(self, fh, n = 99999):
        return [line.rstrip().split(" ") for line in fh.readlines()]

    def check(self, e):
        data_given = random.randint(0, 2)
        success = True

        print(e[data_given])
        for i in range(0, 4):
            if i == data_given:
                continue
            if standardized(input()) != standardized(str(e[i])):
                print("On attendait", e[i])
                success = False
        return success

import re
def standardized(string):
    string = string.lower()
    specialChars = {"e": "éèê", "o": "ô", "a": "àâ", " ": "-_’'"}
    for simple, complexes in specialChars.items():
        for complex in complexes:
            string = re.sub(complex, simple, string)
    return string
