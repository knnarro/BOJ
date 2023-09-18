import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
coords = list(map(int, input().split()))
unique_coords = sorted(set(coords))
coords_mapping = {coord:index for index, coord in enumerate(unique_coords)}

for x in coords:
    print(f'{coords_mapping[x]} ')