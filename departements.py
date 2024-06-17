#!/usr/bin/env python3

import random

class Departements:
    def import_lines(self, fh):
        return [ Data(l) for l in fh.readlines() if self.isDepartment(l) ]

    def isDepartment(self, line):
        if len(line) == 0:
            return False
        if line[0] == "-":
            return False
        return True

    def check(self, data):
        success = True
        pick = random.choice([data.name, data.number] + data.cities)
        print(pick)
        for element in [data.name, data.number] + data.phones + data.cities:
            if element == pick:
                continue
            if standardized(input()) != standardized(str(element)):
                print("On attendait", element)
                success = False
        return success

def standardized(string):
    string = string.lower()
    specialChars = {"e": "éèê", "o": "ô", "a": "àâ", " ": "-_’'"}
    for simple, complexes in specialChars.items():
        for complex in complexes:
            string = re.sub(complex, simple, string)
    return string


class Data:
    def __init__(self, line):
        line = re.sub("\n", "", line)
        self.name, left = grabFirst(line, " : ")
        self.number, left = grabFirst(left, " ")
        _, left = grabPattern(left, "(\([^)]+\))")
        self.phones, left = grabPattern(left, "[0-9][0-9]\.[0-9][0-9]")
        self.cities = left.split(" ")

    def __str__(self):
        return "{} _ {} _ {} _ {}".format(self.name, self.number, self.phones, self.cities)


import re
def grabFirst(line, separator):
    first = line.split(separator)[0]
    line = re.sub(first + separator, "", line, 1)
    return first, chomp(line)

def grabPattern(line, pattern):
    elements = re.findall(pattern, line)
    for e in elements:
        line = re.sub(re.escape(e), "", line)
    return elements, chomp(line)

def chomp(line):
    if not line:
        return ""
    while line[0] == " ":
        line = line[1:]
    return re.sub("[ ]+", " ", line)


from unittests import assert_equals
def tests():
    print(Data("Finistère : 29 02.98 Brest Quimper Morlaix"))
    print(Data("Gironde : 33 05.56 (sud-ouest) 05.57 (nord-est) Bordeaux Mérignac Pessac"))
    print(Data("Côtes d'Armor : 22 02.96 Saint-Brieuc Lagnon Lamballe-Armor\n"))
    assert_equals("cotes d armor", standardized("Côtes d'Armor"))

if __name__ == "__main__":
    tests()
