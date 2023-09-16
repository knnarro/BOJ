import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
baskets = [0] * n

for case in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1, j):
        baskets[idx] = k

for basket in baskets:
    print(f'{basket} ')