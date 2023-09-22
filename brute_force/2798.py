import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))
length = len(cards)
ans = 0
for i in range(length):
    for j in range(i+1, length):
        for k in range(j+1, length):
            sum = cards[i]+cards[j]+cards[k]
            if sum <= m and sum > ans:
                ans = sum

print(ans)