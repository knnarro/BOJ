import sys
from collections import deque
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
numbers = deque()
for i, number in enumerate(input().split()):
    numbers.append((i+1, int(number)))

result = []
count = 1
while len(numbers) > 0:
    if count >= 0:
        for i in range(count-1):
            numbers.append(numbers.popleft())
        removed = numbers.popleft()
    else:
        for i in range(abs(count)-1):
            numbers.appendleft(numbers.pop())
        removed = numbers.pop()
    result.append(str(removed[0]))
    count = removed[1]

print(f'{" ".join(result)}')