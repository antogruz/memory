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
        pick = random.choice(data.keys)
        print(pick.header, pick.expected)
        elements = data.keys + data.nonKeys
        random.shuffle(elements)
        for element in elements:
            if element.header == pick.header:
                continue
            print(element.header + ":")
            if not element.check(input()):
                print("On attendait", element.expected)
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
        parser = Parser(line)
        self.keys = []
        self.nonKeys = []
        self.keys.append(SimpleCheck("Nom du département", parser.grabFirst(" : ")))
        self.keys.append(SimpleCheck("Numéro du département", parser.grabFirst(" ")))
        parser.grabPattern("(\([^)]+\))")
        self.nonKeys.append(Phones(parser.grabPhones()))
        cities = parser.line.split(" ")
        for i, city in enumerate(cities):
            self.keys.append(SimpleCheck("Ville" + str(i + 1), city))

    def __str__(self):
        return "{} _ {} _ {} _ {}".format(self.name, self.number, self.phones, self.cities)

class Parser:
    def __init__(self, line):
        self.line = re.sub("\n", "", line)

    def grabFirst(self, separator):
        first = self.line.split(separator)[0]
        self.line = chomp(re.sub(first + separator, "", self.line, 1))
        return first

    def grabPhones(self):
        return self.grabPattern(phonePattern())

    def grabPattern(self, pattern):
        elements = re.findall(pattern, self.line)
        for e in elements:
            self.line = chomp(re.sub(re.escape(e), "", self.line))
        return elements

import re

def getPhones(line):
    return re.findall(phonePattern(), line)

def phonePattern():
    return "[0-9][0-9]\.[0-9][0-9]"


def chomp(line):
    if not line:
        return ""
    while line[0] == " ":
        line = line[1:]
    return re.sub("[ ]+", " ", line)

def similars(a, b):
    if len(a) != len(b):
        return False
    for element in a:
        if element not in b:
            return False
    return True

class Phones:
    def __init__(self, values):
        self.expected = values
        self.header = "Numéros de téléphone"

    def check(self, answer):
        return similars(self.expected, getPhones(answer))

class SimpleCheck:
    def __init__(self, header, value):
        self.expected = str(value)
        self.header = header

    def check(self, answer):
        return standardized(answer) == standardized(self.expected)



from unittests import assert_equals, assert_true
def tests():
    print(Data("Finistère : 29 02.98 Brest Quimper Morlaix"))
    print(Data("Gironde : 33 05.56 (sud-ouest) 05.57 (nord-est) Bordeaux Mérignac Pessac"))
    print(Data("Côtes d'Armor : 22 02.96 Saint-Brieuc Lagnon Lamballe-Armor\n"))
    print(Data("Moselle : 57 03.87 (est) 03.82 (ouest) Metz Thionville Montigny-lès-Metz"))
    assert_equals("cotes d armor", standardized("Côtes d'Armor"))
    assert_true(Phones(["02.87", "02.82"]).check("02.82  02.87"))


if __name__ == "__main__":
    tests()
