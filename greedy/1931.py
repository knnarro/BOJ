import sys
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda meeting:(meeting[1], meeting[0]))

ans = 0
time = 0
for meeting in meetings:
    if time <= meeting[0]:
        ans += 1
        time = meeting[1]

print(ans)