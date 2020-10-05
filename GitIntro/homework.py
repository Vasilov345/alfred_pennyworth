from typing import List


def calculate_rooms_number(data: List[List[int]]) -> int:
    if not data:
        maxRoomsNumber = 0
    else:
        minTime = data[0][0]
        maxTime = data[-1][1]
        maxRoomsNumber = 0
        for time in range(minTime, maxTime):
            roomNumber = 0
            for meeting in data:
                if (meeting[0] <= time and time <= meeting[1]):
                    roomNumber += 1
            if roomNumber > maxRoomsNumber:
                maxRoomsNumber = roomNumber

    return maxRoomsNumber
