from math import gcd

intervals = []
n = int(input())
prev = 0
for i in range(n):
    cur = int(input())
    if i > 0:
        intervals.append(cur-prev)
    prev = cur

_gcd = gcd(intervals[0], intervals[1])
for interval in intervals[2:]:
    _gcd = gcd(_gcd, interval)
    if _gcd == 1: break

trees = list(map(lambda x: x//_gcd - 1, intervals))
print(sum(trees))