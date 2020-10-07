import unittest
import homework_advanced


class TestGenerateAlphabet(unittest.TestCase):

    def test_letters(self):
        alphabet = homework_advanced.generate_alphabet()
        expected_letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        actual_letters = [list(alp.keys())[0] for alp in alphabet]

        self.assertEqual(set(actual_letters), set(expected_letters))

    def test_int_values(self):
        alphabet = homework_advanced.generate_alphabet()

        values = [list(alp.values())[0] for alp in alphabet]

        self.assertGreaterEqual(min(values), 0)
        self.assertLessEqual(max(values), 100)


class TestSortAlphabet(unittest.TestCase):

    def test_sort(self):
        def get_value_from_alphabet(data):
            return list(data.values())[0]

        alphabet = [
            {'a': 5}, {'b': 57}, {'c': 23}, {'d': 57}, {'e': 88}, {'f': 86}, {'g': 12}, {'h': 41}, {'i': 8},
            {'j': 50}, {'k': 1}, {'l': 61}, {'m': 79}, {'n': 69}, {'o': 3}, {'p': 30}, {'q': 75}, {'r': 70},
            {'s': 9}, {'t': 57}, {'u': 34}, {'v': 70}, {'w': 13}, {'x': 86}, {'y': 12}, {'z': 82}
        ]
        sorted_alphabet = homework_advanced.sort_alphabet(alphabet)
        for i in range(len(sorted_alphabet) - 1):
            current_value = get_value_from_alphabet(sorted_alphabet[i])
            next_value = get_value_from_alphabet(sorted_alphabet[i + 1])
            self.assertLessEqual(current_value, next_value)


if __name__ == "__main__":
    unittest.main()
