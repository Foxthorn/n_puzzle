class Goal:
    __size = 0

    def __init__(self, size):
        self.__size = size

    def spiral_part(self, x, y, n):
        if x == -1 and y == 0:
            return -1
        if y == (x + 1) and x < (n // 2):
            return self.spiral_part(x - 1, y - 1, n - 1) + 4 * (n - y)
        if (n - y) > x >= y:
            return self.spiral_part(y - 1, y, n) + (x - y) + 1
        if x >= (n - y) and y <= x:
            return self.spiral_part(x, y - 1, n) + 1
        if (n - y) <= x < y:
            return self.spiral_part(x + 1, y, n) + 1
        if x < (n - y) and y > x:
            return self.spiral_part(x, y - 1, n) - 1

    def setup_goal(self):
        array = [[0] * self.__size for x in xrange(self.__size)]
        for x in xrange(self.__size):
            for y in xrange(self.__size):
                array[x][y] = self.spiral_part(y, x, self.__size) + 1
                if array[x][y] == self.__size ** 2:
                    array[x][y] = 0
        return array
