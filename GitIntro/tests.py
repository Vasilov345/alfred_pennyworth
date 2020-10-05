import unittest

from git_intro.homework import calculate_rooms_number


class TestCalculateRoomsNumber(unittest.TestCase):

    def test_rooms_count(self):
        self.assertEqual(calculate_rooms_number([[1, 2], [2, 4]]), 2)
        self.assertEqual(calculate_rooms_number([[1, 2], [3, 4], [1, 5], [6, 7]]), 2)
        self.assertEqual(calculate_rooms_number([[1, 2], [3, 4]]), 1)

    def test_empty_data(self):
        self.assertEqual(calculate_rooms_number([]), 0)
