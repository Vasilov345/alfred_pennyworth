import unittest

from homework_student import calculate_ships


class TestCalculateShips(unittest.TestCase):

    def test_10x10(self):
        matrix = [[1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 0, 1, 1, 1, 1]]

        self.assertEqual(calculate_ships(matrix), 11)

    def test_1x1(self):
        matrix = [[1]]
        self.assertEqual(calculate_ships(matrix), 1)

    def test_no_ships(self):
        matrix = [[]]
        self.assertEqual(calculate_ships(matrix), 0)

    def test_3x3(self):
        matrix = [[1, 0, 0],
                  [1, 0, 0],
                  [0, 0, 1]]
        self.assertEqual(calculate_ships(matrix), 2)


if __name__ == "__main__":
    unittest.main()
