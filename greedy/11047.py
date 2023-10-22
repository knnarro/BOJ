import sys
input = sys.stdin.readline

n, k = map(int, input().split())
values = []
for _ in range(n):
    values.append(int(input()))

ans = 0
remainder = k
while remainder > 0:
    idx = 0
    for i in range(len(values)):
        if values[i] > remainder:
            break
        idx = i
    quotient = remainder // values[idx]
    remainder = remainder % values[idx]
    ans += quotient

print(ans)