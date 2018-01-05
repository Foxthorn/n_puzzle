def hamming_distance(current_puz, goal):
    k = 0
    num = 0
    for line in current_puz:
        j = 0
        for i in line:
            if i != goal[k][j] and goal[k][j] != 0:
                num += 1
            j += 1
        k += 1
    return num
