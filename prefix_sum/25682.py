import sys
input = sys.stdin.readline

def execute():
    n, m, k = map(int, input().split())
    boards = [[0 for _ in range(m+1)]]
    sums_B = [[0 for _ in range(m+1)] for _ in range(n+1)]
    sums_W = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for _ in range(n):
        boards.append([0] + list(input().strip()))

    for i in range(1, n+1):
        for j in range(1, m+1):
            color_start_with_B = 'B' if (i+j) % 2 == 0 else 'W'
            color_start_with_W = 'W' if (i+j) % 2 == 0 else 'B'
            sums_B[i][j] = sums_B[i-1][j] + sums_B[i][j-1] - sums_B[i-1][j-1] + (0 if color_start_with_B == boards[i][j] else 1)
            sums_W[i][j] = sums_W[i-1][j] + sums_W[i][j-1] - sums_W[i-1][j-1] + (0 if color_start_with_W == boards[i][j] else 1)

    ans = k*k
    for i in range(k, n+1):
        for j in range(k, m+1):
            count_B = sums_B[i][j] - sums_B[i-k][j] - sums_B[i][j-k] + sums_B[i-k][j-k]
            count_W = sums_W[i][j] - sums_W[i-k][j] - sums_W[i][j-k] + sums_W[i-k][j-k]
            ans = min(ans, count_B, count_W)
    print(ans)

execute()