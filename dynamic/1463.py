n = int(input())
count = [n for _ in range(n+1)]

count[n] = 0
for i in range(n, 0, -1):
    if i%3 == 0:
        count[i//3] = min(count[i] + 1, count[i//3])
    if i%2 == 0:
        count[i//2] = min(count[i] + 1, count[i//2])
    count[i-1] = min(count[i] + 1, count[i-1])

print(count[1])