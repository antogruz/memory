#!/usr/bin/env python3

import random

class Numbers():
    def import_lines(self, fh, n = 99999):
        couples = []
        i = 0

        for line in fh.readlines():
            couples.append((i, line.rstrip()))
            i += 1
            if i >= n:
                break

        return couples


    def check(self, couple):
        print(couple[0])
        return input() == couple[1]

