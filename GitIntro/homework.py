from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    rooms = 0
    for m in range(len(data)):
        for n in range(len(data[m])):
            if data[0][n] >= data[m - 1][n - 1]:
                rooms+=1
    return rooms
    
