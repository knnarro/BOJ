import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
nums = [[ 0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    seq = list(map(int, input().split()))
    for j in range(1, n+1):
        nums[i][j] = seq[j-1]

sums = [[ 0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + nums[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    sum = sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]
    print(f'{sum}\n')