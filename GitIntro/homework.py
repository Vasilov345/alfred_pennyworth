from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    """
    There is a list of meetings for office.
    Each meeting should have free room.
    Calculate how many rooms we need to prevent conflicts.

    Args:
        data: List of meetings with time of start and time of end

    Returns: Number of rooms

    Examples:
        calculate_rooms_number([[1, 2], [2, 4]])
        >>> 2
        calculate_rooms_number([[1, 2], [3, 4]])
        >>> 1
        calculate_rooms_number([[1, 2], [3, 4], [1, 5], [6, 7]])
        >>> 2
    """
    rooms_needed = 1
    if not data:
        return rooms_needed - 1
    for i in range(len(data)):
        if i < len(data) - 1:
            if data[i][1] >= data[i+1][0]:
                rooms_needed += 1
    print(rooms_needed)
    return rooms_needed




