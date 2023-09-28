import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
c = list(map(int, input().split()))

d = deque()
for i, num in enumerate(b):
    if a[i] == 0:
        d.append(num)

for num in c:
    d.appendleft(num)
    print(f'{d.pop()} ')