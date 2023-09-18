import sys
input = sys.stdin.readline
print = sys.stdout.write

# 카운팅 정렬
n = int(input())
numbers = [0] * 10001
for i in range(n):
    numbers[int(input())] += 1

for idx in range(1, 10001):
    for i in range(numbers[idx]):
        print(f'{idx}\n')