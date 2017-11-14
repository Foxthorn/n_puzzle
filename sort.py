import copy


class Sort:
    __size = 0
    __moves_list = []
    __pos_list = []
    __reset = []
    __goal = []
    __first = []
    __sec = []
    __third = []
    __fourth = []

    def __init__(self, matrix, goal):
        self.__reset = copy.deepcopy(matrix)
        self.__goal = copy.deepcopy(goal)
        for i in matrix:
            self.__size += 1

    def child_calculation(self, list_child):
        diff = []
        for child in list_child:
            k = 0
            num = 0
            for line in child:
                j = 0
                for i in line:
                    if i != self.__goal[k][j] and self.__goal[k][j] != 0:
                        num += 1
                    j += 1
                k += 1
            diff.append(num)
        return diff

    @staticmethod
    def fourth(x, y, puz):
        puz = copy.deepcopy(puz)
        temp = puz[x][y]
        puz[x][y] = puz[x][y + 1]
        puz[x][y + 1] = temp
        return puz

    @staticmethod
    def third(x, y, puz):
        puz = copy.deepcopy(puz)
        temp = puz[x][y]
        puz[x][y] = puz[x][y - 1]
        puz[x][y - 1] = temp
        return puz

    @staticmethod
    def sec(x, y, puz):
        puz = copy.deepcopy(puz)
        temp = puz[x][y]
        puz[x][y] = puz[x + 1][y]
        puz[x + 1][y] = temp
        return puz

    @staticmethod
    def first(x, y, puz):
        puz = copy.deepcopy(puz)
        temp = puz[x][y]
        puz[x][y] = puz[x - 1][y]
        puz[x - 1][y] = temp
        return puz

    def sort(self, puzzle):
        self.__pos_list.append(puzzle)
        pos = []
        child = []
        item_index = 0
        i = 0
        for row in puzzle:
            for i in row:
                if i == 0:
                    break
                item_index += 1
            if i == 0:
                break
        y = item_index % 3
        x = int(item_index / 3)
        if x != 0:
            self.__first = self.first(x, y, copy.deepcopy(puzzle))
            child.append(self.__first)
            pos.append("U")
        if x < self.__size - 1:
            self.__sec = self.sec(x, y, copy.deepcopy(puzzle))
            child.append(self.__sec)
            pos.append("D")
        if y != 0:
            self.__third = self.third(x, y, copy.deepcopy(puzzle))
            child.append(self.__third)
            pos.append("L")
        if y < self.__size - 1:
            self.__fourth = self.fourth(x, y, copy.deepcopy(puzzle))
            child.append(self.__fourth)
            pos.append("R")
        num = self.child_calculation(child)
        print num
        if puzzle != self.__goal:
            maxi = 0
            count = 0
            last = num[0]
            for i in num:
                if i < last:
                    last = i
                    maxi = count
                count += 1
            self.__moves_list.append(pos[maxi])
            if child[maxi] in self.__pos_list:
                self.sort(self.__pos_list[0])
            else:
                self.sort(child[maxi])
        else:
            print self.__pos_list
            print self.__moves_list
            return True
