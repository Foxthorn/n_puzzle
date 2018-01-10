import time
from solve import a_star
from arguments import *


def main():
    print "-- Starting --"
    time.sleep(1)
    matrix, size, h, goal = check_argv()
    time.sleep(2)
    start = time.time()
    a_star(matrix, goal, size, h)
    end = time.time()
    print "Time taken to solve :", '{0:f}'.format(end - start)


if __name__ == '__main__':
    main()
