from move import *
from heuristics import *
from display import *


class Node:
    def __init__(self, q=None, size=None, h=None, g=None, f=None, parent=None):
        self.q = q     # positions
        self.h = h     # heuristic
        self.g = g     # moves
        self.f = f
        self.size = size
        self.parent = parent


def a_star(puz, goal, size, heur):
    if check_solvable(puz) == 1:
        print "\nUnsolvable puzzle\n"
        print_puz(puz)
        return
    move = Move(goal)
    heuristic = Heuristics(heur, goal)
    h = heuristic.calculate_h(puz)
    start = Node(puz, goal, size, h, 0, h)
    open_nodes = [start]
    open_set = [start.q]
    closed_nodes = []
    closed_set = []
    i = 0
    mem = 0
    maxim = 0
    select = 0
    while open_nodes:
        current = sorted(open_nodes, key=lambda x: x.f)[0]
        if current.q == goal:
            path = [goal]
            if current.parent != 0:
                while current.parent.q != start.q:
                    path.append(current.parent.q)
                    current = current.parent
            for line in puz:
                print line
            print '\n'
            print_output(path, maxim, len(closed_set), i, select, len(path))
            return

        open_nodes.remove(current)
        open_set.remove(current.q)
        mem -= 1
        if mem >= maxim:
            maxim = mem

        closed_nodes.append(current)
        closed_set.append(current.q)
        select += 1

        new_g = current.g + 1
        expanded = move.move(current.q)
        for node in expanded:
            node_h = heuristic.calculate_h(node)
            node_address = Node(node, size, node_h, new_g, new_g + node_h, current)
            if node in closed_set:
                continue
            if node not in open_set:
                i += 1
                mem += 1
                open_nodes.append(node_address)
                open_set.append(node)
            elif new_g >= node_address.g:
                continue


def check_solvable(puzzle):
    inv = 0
    j = 0
    while j < len(puzzle):
        i = 0
        while i < len(puzzle):
            if puzzle[j][i] == 1:
                i += 1
                if i >= len(puzzle):
                    i = 0
                    j += 1
            char = puzzle[j][i]
            x = i
            y = j
            while y < len(puzzle):
                while x < len(puzzle):
                    if char > puzzle[y][x] > 0:
                        inv += 1
                    x += 1
                x = 0
                y += 1
            i += 1
        j += 1
    if inv % 2 == 0 and len(puzzle) % 2 != 0:
        return 1
    return 0
