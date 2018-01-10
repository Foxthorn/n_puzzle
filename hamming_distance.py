def hamming_distance(grid, goal):
    h = 0
    y = 0
    for row in grid:
        x = 0
        for e in row:
            if e != 0 and e != goal[y][x]:
                h += 1
            x += 1
        y += 1
    return h
