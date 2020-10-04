from typing import List


def calculate_ships(data: List[List[int]]):
    n = 0
    for i, row in enumerate(data):

        for j, element in enumerate(row):
            if element == 1:
                if (i == 0 or data[i - 1][j] == 0) and (j == 0 or data[i][j - 1] == 0):
                    n += 1

    return n
