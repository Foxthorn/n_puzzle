import numpy as np


class Puzzle:
    __size = 0

    def __init__(self, line):
        num = 0
        comm = 0
        for char in line:
            if char == "#":
                comm = 1
            if char.isdigit() and comm == 0:
                num = num * 10 + ord(char) - ord('0')
        self.__size = num

    def map_setup(self, line):
        print "Setting up Puzzle"
        matrix = [[0 for x in xrange(self.__size)] for y in xrange(self.__size)]
        del line[0]
        x = 0
        y = 0
        for char in line:
            comm = 0
            for c in char:
                if c == "#":
                    comm = 1
                if c.isdigit() and comm == 0:
                    matrix[y][x] = int(c)
                    x += 1
                if x > 2:
                    y += 1
                    x = 0
                if y > 2:
                    y = 0
        print "Finished Setup"
        return matrix
