import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

baskets = []
for num in range(1, n+1):
    baskets.append(num)

for c in range(m):
    i, j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp

for basket in baskets:
    print(f'{basket} ')