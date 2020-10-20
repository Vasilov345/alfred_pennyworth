from typing import List

def calculate_rooms_number(data: List[List[int]]) -> int:
    count=0
    for x in range(len(data)):
            if (data[x][0] <= data[x-1][1]):
                count=count+1
    return count