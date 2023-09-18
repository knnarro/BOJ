import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

numbers.sort()
for number in numbers:
    print(f'{number}\n')