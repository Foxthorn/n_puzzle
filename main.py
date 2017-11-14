import sys
import time
from sort import *
from puzzle import *
from goal import *

print "Getting Puzzle"
start = time.time()
f_object = open(sys.argv[1], "r")
line = f_object.readlines()
goal = Goal(line[0])
puzzle = Puzzle(line[0])
matrix = puzzle.map_setup(line)
end = time.time()
print "Time Elapsed :", '{0:f}'.format(end - start)
g_matrix = goal.setup_goal()
print "m", matrix
print "g", g_matrix
# print g_matrix[0], "\n", g_matrix[1], "\n", g_matrix[2], "\n"
sort = Sort(copy.deepcopy(matrix), copy.deepcopy(g_matrix))
start = time.time()
if sort.sort(copy.deepcopy(matrix)) is False:
    print "Unsolvable"
end = time.time()
print "Time Elapsed :", '{0:f}'.format(end - start)
