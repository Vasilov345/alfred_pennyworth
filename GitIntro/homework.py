from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    count_room = 1
    if not data:
        return count_room - 1
    else:
        for time in range(len(data) - 1):
            if data[time][1] >= data[time + 1][0]:
                count_room += 1
        return count_room
