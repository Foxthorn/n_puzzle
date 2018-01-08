from heuristics import *
from move import *


class Data(object):
    def __init__(self, puz, h, count, parent=None):
        self.puz = puz
        self.heuristic = h
        self.parent = parent
        self.count = count


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = Node()
        self.nodes = []
        self.max_held = 0
        self.selected = 0

    def get_data(self, puz):
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur.data.puz == puz:
                return cur.data

    def get_lowest(self):
        cur = self.head
        low = cur.next
        while cur.next:
            cur = cur.next
            if cur.data.heuristic < low.data.heuristic:
                low = cur
        return low.data

    def update_h(self, parent, puz, h, count):
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur.data.puz == puz:
                cur.data.heuristic = h
                cur.data.parent = parent
                if count < cur.data.count:
                    cur.data.count = count
                return

    def erase(self, puz):
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur.data.puz == puz:
                last_node.next = cur.next
                return

    def find(self, puz):
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur.data.puz == puz:
                return True
        return False

    def length(self):
        cur = self.head
        total = 0
        while cur.next:
            cur = cur.next
            total += 1
        return total

    def add(self, data):
        self.nodes.append(data.puz)
        new_node = Node(data)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        self.selected += 1
        if self.length() > self.max_held:
            self.max_held = self.length()

    def display(self):
        elem = []
        cur = self.head
        while cur.next:
            cur = cur.next
            elem.append(cur.data.puz)
        return elem


def a_star(start, goal, h):
    if check_solvable(start) == 1:
        return
    open = List()
    closed = List()
    heuristics = Heuristics(h, goal)
    move = Move(goal)
    h_start = heuristics.calculate_h(start)
    start_data = Data(start, h_start, 0)
    open.add(start_data)
    path = []
    while open.length() != 0:
        current = open.get_lowest()
        if current.puz == goal:
            while current.parent:
                path.append(current.parent)
                current = closed.get_data(current.parent)
            path.reverse()
            for node in path:
                for line in node:
                    print line
                print "\n"
            for line in goal:
                print line
            print "\n"
            print 'Total number of states ever selected in the "opened" set:', open.selected
            print "Maximum number of states ever represented in memory at the same :",
            print len(open.nodes) + len(closed.nodes)
            print "Total number of moves :", len(path)
            print "Maximum nodes held in open list :", open.max_held
            print "Total nodes added to closed list :", len(closed.nodes)
            return
        open.erase(current.puz)
        closed.add(current)
        expand = move.move(current.puz)
        for node in expand:
            h_node = heuristics.calculate_h(node) + current.count + 1
            if closed.find(node):
                continue
            if open.find(node):
                if h_node < current.heuristic + current.count:
                    open.update_h(current.puz, node, h_node)
                    closed.erase(current.puz)
            else:
                cur_data = Data(node, h_node, current.count + 1, current.puz)
                open.add(cur_data)
    print "No Solution"
    return


def check_solvable(puzzle):
    inv = 0
    j= 0
    while j < len(puzzle):
        i = 0
        while i < len(puzzle):
            char = puzzle[j][i]
            x = i
            y = j
            while y < len(puzzle):
                while x < len(puzzle):
                    if char > puzzle[y][x] != 0:
                        inv += 1
                    x += 1
                x = 0
                y += 1
            i += 1
        j += 1
    if inv % 2 == 0:
        print "\nUnsolvable puzzle"
        return 1
    return 0
