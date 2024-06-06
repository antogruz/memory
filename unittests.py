#!/usr/bin/env python3

def runTests(tester):
    methodNames = findAllMethods(tester)
    testNames = [m for m in methodNames if "test" in m]
    for test in testNames:
        print(test)
        if "__before__" in methodNames:
            tester.__before__()
        getattr(tester, test)()


def assert_equals(expected, actual):
    if expected != actual:
        raise Exception("Expected", expected, "got", actual)

def assert_contains(expected, collection):
    if expected not in collection:
        raise Exception("Expected", expected, "to be in", collection)

def assert_similars(expected, actual):
    if not len(expected) == len(actual):
        raise Exception("Expected size of {}, but got {}. So actual {} is not similar to expected {}".format(len(expected), len(actual), actual, expected))
    for e in expected:
        assert_contains(e, actual)


def findAllMethods(object):
    return [method for method in dir(object) if callable(getattr(object, method))]

