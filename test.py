import unittest
import numpy as np
from grid import Grid


class TestsGridStatics(unittest.TestCase):

    def setUp(self):
        self.filename = 'data/test.txt'

    def test_txt_to_matrix(self):
        my_matrix = np.matrix([
            [0, 0, 1],
            [0, 0, 0],
            [1, 1, 1]
        ])
        file_matrix = Grid.txt_to_matrix(self.filename)
        self.assertTrue(np.array_equal(my_matrix, file_matrix))

    def test_calculate_size(self):
        self.assertEqual(Grid.calculate_size(0), 1)
        self.assertEqual(Grid.calculate_size(1), 3)

    def test_center_point_to_edge(self):
        self.assertEqual(Grid.center_point_to_edges(1, 1, 0), [(1, 1), (2, 2)])
        self.assertEqual(Grid.center_point_to_edges(1, 1, 1), [(0, 0), (3, 3)])

    def test_get_size(self):
        self.assertEqual(Grid.get_size(self.filename), (3, 3))


class TestsGrid(unittest.TestCase):

    def setUp(self):
        self.grid = Grid('data/test.txt')

    def test_draw_box(self):
        self.grid.draw_box(1, 1, 0)
        self.assertTrue(
            np.array_equal(self.grid.matrix[1, 1], 1)
        )

    def test_one_sized_box(self):
        self.grid.draw_box(1, 1, 1)
        self.assertTrue(
            np.array_equal(
                self.grid.matrix, np.ones((3, 3))
            )
        )

    def test_clean(self):
        self.grid.draw_box(0, 0, 0)
        self.grid.clean(0, 0)
        self.assertTrue(
            np.array_equal(self.grid.matrix[0, 0], 0)
        )

    def test_draw_line(self):
        self.grid.draw_line(0, 0, 'h', 3)
        self.assertTrue(
            np.array_equal(
                self.grid.matrix[0, 0:3], np.ones((1, 3))[0]
            )
        )

    def test_check_correction(self):
        self.grid.draw_box(0, 2, 0)
        self.grid.draw_line(2, 0, 'h', 3)
        self.assertTrue(self.grid.check_correction())


if __name__ == '__main__':
    unittest.main()
