import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

remainder = nums[0] % m
sums = [remainder]
counts = {remainder: 1}
for i in range(1, n):
    remainder = (sums[i-1]+nums[i]) % m
    sums.append(remainder)
    counts[remainder] = counts.get(remainder, 0) + 1

ans = 0
for i in range(0, m):
    count = counts.get(i, 0)
    ans += (count * (count-1) // 2)

ans += counts.get(0, 0)
print(ans)