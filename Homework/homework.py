from typing import List
from itertools import chain


def calculate_rooms_number(data: List[List[int]]) -> int:
    room_number = 0
    if not data:
        return room_number
    else:
        data = list(chain.from_iterable(data))
        data1 = len(data)
        data = set(data)
        data2 = len(data)
        room_number = data1 - data2 + 1
        return room_number
