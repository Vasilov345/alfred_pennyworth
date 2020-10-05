from typing import List


def calculate_ships(data: List[List[int]]):
    """
    Calculate ships number on field for sea battle

    Args:
        data: Two dimension array

    Returns: number of ships in int value
    Examples:
        calculate_ships(
        [1, 0, 0],
        [0, 0, 1])
        >>> 2
    """
    iteration_size = len(data)
    res_ships = 0
    for i in range(iteration_size):
        for j in range(iteration_size):
            #print (matrix [i][j])

            if matrix [i][j] == 1:
                try:
                    if matrix[i+1][j] and matrix[i][j+1] == 0:
                        continue
                except IndexError:
                    res_ships += 1
    print(res_ships)


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
calculate_ships(matrix)
