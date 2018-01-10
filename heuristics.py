from hamming_distance import hamming_distance
from linear import *


class Heuristics:
    def __init__(self, h, goal):
        i = 0
        self.h = h
        if self.h == 'h':
            print "\nUsing Hamming Distance + Manhattan Distance:\n"
        if self.h == 'm':
            print "\nUsing Manhattan Distance:\n"
        if self.h == 'l':
            print "\nUsing Linear Distance:\n"
        self.goal = goal
        for x in goal:
            i += 1
        self.size = i

    def calculate_h(self, puz):
        if self.h == 'h':
            return hamming_distance(puz, self.goal) + manhattan_distance(puz, self.goal)
        if self.h == 'm':
            return manhattan_distance(puz, self.goal)
        if self.h == 'l':
            return linear_distance(puz, self.goal, self.size)
