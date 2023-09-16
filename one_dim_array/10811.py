import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
baskets = [i for i in range(n+1)]

for t in range(m):
    i, j = map(int, input().split())
    baskets = baskets[:i]+baskets[j:i-1:-1]+baskets[j+1:]

for basket in baskets[1:]:
    print(f'{basket} ')