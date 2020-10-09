from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    rooms_counter = 1
    if not data:
        return rooms_counter - 1
    else:
        for time in range(len(data) - 1):
            if data[time][1] >= data[time + 1][0]:
                rooms_counter += 1
        return rooms_counter
