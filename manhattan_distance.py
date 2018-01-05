def get_xy(value, matrix):
    y = 0
    for row in matrix:
        if value in row:
            return row.index(value), y
        y += 1


def manhattan_distance(state, goal):
    h = 0
    y = 0
    for row in state:
        x = 0
        for e in row:
            if e != 0:
                goal_x, goal_y = get_xy(e, goal)
                h += abs(goal_x - x) + abs(goal_y - y)
            x += 1
        y += 1
    return h
