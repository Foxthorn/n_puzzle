from copy import deepcopy


class Move:
    __child = []
    __goal = []
    __size = 0
    __x = 0
    __y = 0

    def __init__(self, goal):
        self.__goal = deepcopy(goal)
        for i in goal:
            self.__size += 1

    def move_right(self, curr):
        right = deepcopy(curr)
        temp = right[self.__x][self.__y]
        right[self.__x][self.__y] = curr[self.__x][self.__y + 1]
        right[self.__x][self.__y + 1] = temp
        return right

    def move_left(self, curr):
        left = deepcopy(curr)
        temp = left[self.__x][self.__y]
        left[self.__x][self.__y] = curr[self.__x][self.__y - 1]
        left[self.__x][self.__y - 1] = temp
        return left

    def move_down(self, curr):
        down = deepcopy(curr)
        temp = down[self.__x][self.__y]
        down[self.__x][self.__y] = curr[self.__x + 1][self.__y]
        down[self.__x + 1][self.__y] = temp
        return down

    def move_up(self, curr):
        up = deepcopy(curr)
        temp = up[self.__x][self.__y]
        up[self.__x][self.__y] = curr[self.__x - 1][self.__y]
        up[self.__x - 1][self.__y] = temp
        return up

    def move(self, current):
        self.__child = []
        self.__x, self.__y = find_x_y(self.__size, current)
        if self.__x > 0:
            up = self.move_up(deepcopy(current))
            self.__child.append(up)
        if self.__x < self.__size - 1:
            down = self.move_down(deepcopy(current))
            self.__child.append(down)
        if self.__y > 0:
            left = self.move_left(deepcopy(current))
            self.__child.append(left)
        if self.__y < self.__size - 1:
            right = self.move_right(deepcopy(current))
            self.__child.append(right)
        return self.__child


def find_x_y(size, current):
    item_index = 0
    i = 0
    for row in current:
        for i in row:
            if i == 0:
                break
            item_index += 1
        if i == 0:
            break
    y = item_index % size
    x = int(item_index / size)
    return x, y
