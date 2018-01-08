import sys
import time
import re
from goal import *
from sort import a_star


def get_heuristic(av):
    if av == '-h':
        print "\n-- Hamming has been selected --"
        return 'h'
    elif av == '-l':
        print "\n-- Linear Conflict has been selected --"
        return 'l'
    elif av == '-m':
        print "\n-- Manhattan has been selected --"
        return 'm'
    else:
        print "Usage: python [filename] optional([-l : linear, -h : hamming, -m : manhattan)"
        sys.exit(1)


def setup_puzzle(fd):
    lines = fd.readline()
    num = 0
    while lines[0] == '#':
        lines = fd.readline
    if not lines[0].isdigit():
        print "The first uncommented line of the file needs to be the puzzle size"
        sys.exit(1)
    else:
        for char in lines:
            if char.isdigit():
                num = num * 10 + ord(char) - ord('0')
            if char == '#':
                break
        s = num
    file = fd.readlines()
    for c in xrange(len(file)):
        file[c] = re.sub(' +', ' ', file[c])
        file[c] = file[c].replace(" ", '.')
        file[c] = file[c].replace('\n', '.')
    for c in file:
        count = 0
        com = 0
        for char in c:
            if char.isdigit() and com == 0:
                count += 1
                com = 1
            if char == '.':
                com = 0
        if count != s:
            print "Size and numbers don't match"
            sys.exit(1)
    mat = [[0 for x in xrange(s)] for y in xrange(s)]
    y = 0
    for c in file:
        x = -1
        num = 0
        com = 0
        for char in c:
            if char.isdigit() and com == 0:
                com = 1
                x += 1
            if char == '.':
                mat[y][x] = num
                com = 0
                num = 0
            else:
                num = num * 10 + ord(char) - ord('0')
        y += 1
    check = []
    for line in mat:
        for c in line:
            if c not in check:
                check.append(c)
            else:
                print "Invalid File, ensure there is a newline at the end of the file"
                sys.exit(1)
    return mat, s


print "-- Starting --"
time.sleep(1)
if len(sys.argv) < 2 or len(sys.argv) > 4:
    print "Usage: python [filename] optional([-l : linear, -h : hamming, -m : manhattan)"
    print "To generate a file run the gen.py file"
    sys.exit(1)
try:
    fd = open(sys.argv[1])
    matrix, size = setup_puzzle(fd)
except:
    print "-- Unable to open file --"
    sys.exit(1)
if len(sys.argv) == 2:
    print "\n-- No heuristic selected, Hamming will be used by default --"
    h = 'h'
if len(sys.argv) == 3:
    h = get_heuristic(sys.argv[2])
time.sleep(2)
start = time.time()
g = Goal(size)
goal = g.setup_goal()
a_star(matrix, goal, h)
end = time.time()
print "\nTime taken to solve :", '{0:f}'.format(end - start)
