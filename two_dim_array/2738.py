import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
matrix_a = [[] for i in range(n)]
matrix_b = [[] for i in range(n)]

for i in range(n):
    row = list(map(int, input().split()))
    matrix_a[i] = row

for i in range(n):
    row = list(map(int, input().split()))
    matrix_b[i] = row

for i in range(n):
    row = [a+b for a, b in zip(matrix_a[i], matrix_b[i])]
    for num in row:
        print(f'{num} ')
    print('\n')