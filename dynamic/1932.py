import sys
input = sys.stdin.readline

n = int(input())
sums = [0 for _ in range(n)]
sums[0] = int(input())
for i in range(1, n):
    nums = list(map(int, input().split()))
    prev_sums = sums.copy()
    sums[0] += nums[0]
    for j in range(1, len(nums)):
        sums[j] = max(prev_sums[j-1], prev_sums[j]) + nums[j]

print(max(sums))