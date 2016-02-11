import numpy as np


class Grid:

    def __init__(self, datafile):
        self.file_matrix = Grid.txt_to_matrix(datafile)
        self.matrix = np.zeros(Grid.get_size(datafile))

    @staticmethod
    def txt_to_matrix(filename):
        f = open(filename)
        f.readline()
        matrix = []
        for i in f:
            row = []
            for j in i:
                if j == '.':
                    row.append(0)
                elif j == '#':
                    row.append(1)
            matrix.append(row)
        return np.matrix(matrix)

    @staticmethod
    def get_size(filename):
        size = open(filename).readline().replace('\n', '').split(' ')
        return (int(size[0]), int(size[1]))

    @staticmethod
    def calculate_size(n):
        return 2 * n + 1

    @staticmethod
    def center_point_to_edges(x, y, size):
        c_size = Grid.calculate_size(size)
        m = (c_size - 1) / 2
        return [(x - m, y - m), (x + m + 1, y + m + 1)]

    def draw_box(self, x, y, size):
        c_size = Grid.calculate_size(size)
        coors = Grid.center_point_to_edges(x, y, size)
        self.matrix[coors[0][0]:coors[1][0], coors[0][
            1]:coors[1][1]] = np.ones((c_size, c_size))

    def draw_line(self, x, y, direction, length):
        if direction == 'h':
            self.matrix[x, y: y + length] = np.ones((1, length))
        elif direction == 'v':
            self.matrix[x:x + length, y] = np.ones((length, 1))
        else:
            raise ValueError('Direction is v or h')

    def clean(self, x, y):
        self.matrix[x, y] = 0

    def check_correction(self):
        return np.array_equal(self.file_matrix, self.matrix)

    def cost_of_drawing_box(self, x, y, size):
        c_size = Grid.calculate_size(size)
        coors = Grid.center_point_to_edges(x, y, size)
        submatrix = self.matrix[
            coors[0][0]:coors[1][0], coors[0][1]:coors[1][1]
        ]
        number_of_zero = (c_size ** 2) - np.sum(submatrix)
        return ((c_size ** 2) - 2 * number_of_zero) - 1
