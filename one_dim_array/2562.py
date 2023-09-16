import sys
input = sys.stdin.readline
print = sys.stdout.write

numbers = []
for i in range(9):
    number = int(input())
    numbers.append(number)

max = max(numbers)
answer = numbers.index(max) + 1
print(f'{max}\n{answer}')