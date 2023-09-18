import sys
from functools import cmp_to_key
input = sys.stdin.readline
print = sys.stdout.write


def compare_coordinate(prev, cur):
    if prev[0] > cur[0]:
        return 1
    elif prev[0] < cur[0]:
        return -1
    else:
        if prev[1] > cur[1]:
            return 1
        elif prev[1] < cur [1]:
            return -1
        else:
            return 0
        

n = int(input())
coordinates = []
for i in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))

coordinates.sort(key=cmp_to_key(compare_coordinate))
for coordinate in coordinates:
    print(f'{coordinate[0]} {coordinate[1]}\n')