import sys
import re
from goal import *


def setup_puzzle(fd):
    line = fd.readline()
    while line[0] == '#':
        line = fd.readline()
    size = get_size(line)
    file = fd.readlines()
    for c in xrange(len(file)):
        file[c] = re.sub(' +', ' ', file[c])
        file[c] = file[c].replace(" ", '.')
        file[c] = file[c].replace('\n', '.')
    c = 0
    while c < len(file):
        if len(file[c]) == 1:
            del(file[c])
        else:
            c += 1
    g = Goal(size)
    goal = g.setup_goal()
    check_numbers(file, size)
    mat = get_puzzle(file, size)
    double_check(mat, goal)
    return mat, size, goal


def double_check(mat, goal):
    num = []
    check = []
    for line in goal:
        for c in line:
            num.append(c)
    for line in mat:
        for c in line:
            if c not in num:
                print "\nInvalid number in file\n"
                sys.exit(1)
            if c not in check:
                check.append(c)
            else:
                print "\nDuplicate numbers in file\n"
                sys.exit(1)


def get_puzzle(file, size):
    mat = [[0 for x in xrange(size)] for y in xrange(size)]
    y = 0
    for j in xrange(len(file)):
        x = 0
        num = 0
        for i in xrange(len(file[j])):
            if file[j][i] == '#':
                break
            if file[j][i].isdigit() and file[j][i] != '.':
                num = num * 10 + ord(file[j][i]) - ord('0')
            if file[j][i] == '.' and i != 0:
                mat[y][x] = num
                num = 0
                x += 1
        y += 1
    return mat


def check_numbers(file, size):
    limit = size * size - 1
    count = 0
    if len(file) > size:
        print "\nSize of puzzle doesn't match size given\n" \
              "Ensure file ends with a newline\n"
        sys.exit(1)
    for i in xrange(len(file)):
        num = 0
        count = 0
        for j in xrange(len(file[i])):
            if not file[i][j].isdigit():
                if file[i][j] != '.':
                    print "\nInvalid number in file\n"
                    sys.exit(1)
            if file[i][j] == '#':
                break
            if file[i][j].isdigit():
                num = num * 10 + ord(file[i][j]) - ord('0')
            if file[i][j] == '.' and j != 0:
                num = 0
                count += 1
                if num > limit:
                    print "\nInvalid number in file\n"
                    sys.exit(1)
        if count != size:
            print "\nSize of puzzle doesn't match size given\n" \
                  "Ensure file ends with a newline\n"
            sys.exit(1)


def get_size(line):
    num = 0
    c = 0
    while not line[c].isdigit():
        c += 1
    while c < len(line):
        if line[c].isspace() and c != 0:
            break
        if line[c] == '#':
            break
        if line[c].isdigit():
            num = num * 10 + ord(line[c]) - ord('0')
        c += 1
    if num < 3:
        print "\nFirst uncommented line of file must be puzzle size and size must be greater then 2 \n"
        sys.exit(1)
    return num


def check_puzzle(puz, goal):
    for line in xrange(puz):
        for num in xrange(line):
            if puz[line][num] not in goal:
                print "\nInvalid number in puzzle\n"
                sys.exit(1)
