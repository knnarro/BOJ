import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())))

start, end = 1, trees[-1]
while start <= end:
    mid = (start+end) // 2
    # mid 이상인 나무 중 가장 작은 나무의 인덱스 찾기
    i, j = 0, n - 1
    while i <= j:
        k = (i+j) // 2
        if trees[k] < mid:
            i = k + 1
        else:
            j = k - 1
    result = sum(trees[i:]) - len(trees[i:]) * mid
    if result >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)