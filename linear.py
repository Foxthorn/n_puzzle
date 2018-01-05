from manhattan_distance import manhattan_distance


# add manhattan with linear collisions
def linear_distance(matrix, goal, size):
    m = manhattan_distance(matrix, goal)
    linear = linear_x(matrix, goal, size)
    linear = linear + linear_y(matrix, goal, size)
    num = m + 2 * linear
    return num


def find_val(matrix, val, size):
    i = 0
    while i < size:
        j = 0
        while j < size:
            if matrix[i][j] == val:
                return i, j
            j += 1
        i += 1
    return

def linear_x(matrix, goal, size):
    i = 1
    tot = 0
    mat = [[0 for x in range(size)] for y in range(size)]
    while i < size * size:
        x_s, y_s = find_val(matrix, i, size)
        x_g, y_g = find_val(goal, i, size)
        if x_s == x_g:
            mat[x_s][y_s] = (y_g - y_s)
        else:
            mat[x_s][y_s] = size * size
        i += 1
    r = 0
    while r < size:
        c = 0
        while c < size:
            if mat[r][c] != size * size:
                i = 1
                while i + c < size:
                    if mat[r][c + i] != size * size:
                        if mat[r][c] + c > mat[r][c + i] + c + i:
                            tot += 1
                    i += 1
            c += 1
        r += 1
    del mat
    return tot


def linear_y(matrix, goal, size):
    i = 1
    tot = 0
    mat = [[0 for x in range(size)] for y in range(size)]
    while i < size * size:
        x_s, y_s = find_val(matrix, i, size)
        x_g, y_g = find_val(goal, i, size)
        if y_s == y_g:
            mat[x_s][y_s] = (x_g - x_s)
        else:
            mat[x_s][y_s] = size * size
        i += 1
    c = 0
    while c < size:
        r = 0
        while r < size:
            if mat[r][c] != size * size:
                i = 1
                while i + r < size:
                    if mat[r + i][c] != size * size:
                        if mat[r][c] + r > mat[r + i][c] + r + i:
                            tot += 1
                    i += 1
            r += 1
        c += 1
    del mat
    return tot
