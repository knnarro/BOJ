import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
numbers = list(map(int, input().split()))
min = min(numbers)
max = max(numbers)

print(f'{min} {max}')