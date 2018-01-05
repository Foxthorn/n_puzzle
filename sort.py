from heuristics import *
from move import *


class Data(object):
    def __init__(self, puz, h, parent=None):
        self.puz = puz
        self.heuristic = h
        self.parent = parent


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

    def get_next(self, data):
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur.data == data:
                cur = cur.next
                return cur.data

    def get_last_node(self):
        cur = self.head
        while cur.next:
            cur = cur.next
        print cur.data.parent

    def get_lowest(self):
        cur = self.head
        low = cur.next
        while cur.next:
            cur = cur.next
            if cur.data.heuristic < low.data.heuristic:
                low = cur
        return low.data

    def update_h(self, parent, puz, h):
        cur = self.head
        while cur.next:
            cur = cur.next
            if cur.data.puz == puz:
                cur.data.heuristic = h
                cur.data.parent = parent
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
    open = List()
    closed = List()
    heuristics = Heuristics(h, goal)
    move = Move(goal)
    h_start = heuristics.calculate_h(start)
    start_data = Data(start, h_start)
    open.add(start_data)
    path = []
    while open.length() != 0:
        current = open.get_lowest()
        if current.puz == goal:
            for node in path:
                for line in node:
                    print line
                print "\n"
            print goal, "\n"
            print 'Total number of states ever selected in the "opened" set:', open.selected
            print "Maximum number of states ever represented in memory at the same :",
            print len(open.nodes) + len(closed.nodes)
            print "Maximum nodes held in open list :", open.max_held
            print "Total nodes added to closed list :", len(closed.nodes)
            return
        open.erase(current.puz)
        closed.add(current)
        expand = move.move(current.puz)
        for node in expand:
            if closed.find(node):
                continue
            if open.find(node):
                h_node = heuristics.calculate_h(node)
                if h_node < current.heuristic:
                    open.update_h(current.puz, node, h_node)
            else:
                h_node = heuristics.calculate_h(node)
                cur_data = Data(node, h_node, current.puz)
                open.add(cur_data)
    print "No Solution"
    return

