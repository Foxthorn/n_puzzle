import random
from solve import check_solvable


def generate_new(size, s):
    if s == 'u' and size % 2 == 0:
        solve = 0
    else:
        solve = 1
    if s == 's' and size % 2 != 0:
        solve = 1
    else:
        solve = 0
    iteration = 0
    new = [[0 for x in xrange(size)] for y in xrange(size)]
    mat = [x for x in range(size * size)]
    random.shuffle(mat)
    i = 0
    for y in range(size):
        for x in range(size):
            new[y][x] = mat[i]
            i += 1
    while check_solvable(new) == solve and iteration <= 1000:
        i = 0
        random.shuffle(mat)
        for y in range(size):
            for x in range(size):
                new[y][x] = mat[i]
                i += 1
        iteration += 1
    if iteration == 1000:
        print "Maximum iterations exceeded, puzzle may not be what was selected\n"
    return new
