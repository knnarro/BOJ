import sys
from math import floor, ceil
input = sys.stdin.readline

def round(number):
    gap = number - int(number)
    if gap >= 0.5:
        return ceil(number)
    elif gap >= 0:
        return floor(number)
    elif gap > -0.5:
        return ceil(number)
    else:
        return floor(number)


n = int(input())
numbers = []
numbers_count = {}
for _ in range(n):
    number = int(input())
    numbers.append(number)
    count = numbers_count.get(number, 0)
    numbers_count[number] = count + 1
numbers.sort()
numbers_count = list(sorted(numbers_count.items(), key=lambda item: (item[1], -item[0]), reverse=True))

mean = round(sum(numbers)/len(numbers))
midian = numbers[len(numbers)//2]
if len(numbers_count) == 1:
    mode = numbers_count[0][0]
else:
    mode = numbers_count[0][0] if numbers_count[0][1] != numbers_count[1][1] else numbers_count[1][0]
range = numbers[-1] - numbers[0]

print(mean)
print(midian)
print(mode)
print(range)