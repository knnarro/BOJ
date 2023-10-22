import sys
input = sys.stdin.readline

n = int(input())
scores = [[0, 0] for _ in range(n+1)] # [i][0]: 직전 계단 안 밟음, [i][1]: 직전 계단 밟음

init = int(input())
scores[1] = [init, init]
for i in range(2, n+1):
    score = int(input())
    scores[i][0] = max(scores[i-2][0], scores[i-2][1]) + score
    scores[i][1] = scores[i-1][0] + score

print(max(scores[n]))