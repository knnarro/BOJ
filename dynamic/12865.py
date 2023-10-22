import sys
input = sys.stdin.readline
print = sys.stdout.write

n, k = map(int, input().split())
max_values = [[0 for _ in range(k+1)] for _ in range(n+1)] # max_values[i][j] == i번째 물건까지 판별했을 때, 무게 j의 최대 가치
ans = 0

for i in range(1, n+1):
    w, v = map(int, input().split())
    for j in range(1, k+1):
        if w <= j:
            max_values[i][j] = max(max_values[i-1][j], v+max_values[i-1][j-w])
        else:
            max_values[i][j] = max_values[i-1][j]
        ans = max(ans, max_values[i][j])

print(f'{ans}')