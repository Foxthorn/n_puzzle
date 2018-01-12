import sys
from goal import *
from file_check import setup_puzzle
from gen import generate_new


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
        print "\nUsage: python [filename] optional([-l : linear, -h : hamming, -m : manhattan)"
        print "To generate a file run the gen.py file"
        sys.exit(1)


def get_solve(av):
    if av == '-u':
        print "\n-- Generating an Unsolvable Puzzle --"
        return 'u'
    elif av == '-s':
        print "\n-- Generating a Solvable Puzzle --"
        return 's'
    else:
        print "\nUsage: python [filename] optional([-l : linear, -h : hamming, -m : manhattan)"
        print "To generate a file run the gen.py file"
        sys.exit(1)


def check_argv():
    if len(sys.argv) < 2:
        print "\nUsage: python [filename] optional( [-l : linear, -h : hamming, -m : manhattan )"
        sys.exit(1)
    if sys.argv[1] != '-g':
        if len(sys.argv) > 3:
            print "\nUsage: python [filename] optional( [-l : linear, -h : hamming, -m : manhattan )"
            sys.exit(1)
        try:
            fd = open(sys.argv[1])
            matrix, size, goal = setup_puzzle(fd)
        except:
            print "\n-- Unable to open file --"
            sys.exit(1)
        if len(sys.argv) == 2:
            print "\n-- No heuristic selected, Hamming + Manhattan will be used by default --"
            h = 'h'
        if len(sys.argv) == 3:
            h = get_heuristic(sys.argv[2])
    else:
        if len(sys.argv) < 2 or len(sys.argv) > 5:
            print "\n Too many parameters\n"
            print "\nUsage: python [-g] [size > 2] [-s : solvable, -u : unsolvable] " \
                  "optional( [-l : linear, -h : hamming, -m : manhattan ) \n"
        try:
            if not sys.argv[2].isdigit():
                print "\nInvalid size entered"
                sys.exit(1)
            size = int(sys.argv[2])
            if size <= 2:
                print "\nInvalid size entered"
                sys.exit(1)
            s = get_solve(sys.argv[3])
            if len(sys.argv) == 5:
                h = get_heuristic(sys.argv[4])
            else:
                h = 'h'
        except:
            print "\nError in parameters\n"
            print "Usage: python [-g] [size > 2] [-s : solvable, -u : unsolvable]"
            sys.exit(1)
        matrix = generate_new(size, s)
        g = Goal(size)
        goal = g.setup_goal()
    return matrix, size, h, goal
