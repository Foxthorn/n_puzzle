import sys
import time
from goal import *
from sort import a_star


def setup_puzzle(fd):
    line = fd.readline()
    num = 0
    if line[0] == '#':
        line = fd.readline()
    for char in line:
        if char.isdigit():
            num = num * 10 + ord(char) - ord('0')
        if char == "#":
            break
    size = num
    matrix = [[0 for x in xrange(size)] for y in xrange(size)]
    num = 0
    for y in xrange(size):
        line = fd.readline()
        i = 0
        for x in xrange(len(line)):
            if line[x].isdigit():
                num = num * 10 + ord(line[x]) - ord('0')
            if line[x].isspace():
                matrix[y][i] = num
                i += 1
                num = 0
            if line[x] == '#':
                break
    matrix[y][i] = num
    return matrix, size


start = time.time()
fd = open(sys.argv[1])
matrix, size = setup_puzzle(fd)
g = Goal(size)
goal = g.setup_goal()
a_star(matrix, goal, 'h')
