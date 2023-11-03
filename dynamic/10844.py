n = int(input())
count = [[1 for _ in range(10)] for _ in range(n)]

count[0][0] = 0
for i in range(1, n):
    for num in range(10):
        if num == 0:
            count[i][num] = int(count[i-1][num+1]%1e9)
        elif num == 9:
            count[i][num] = int(count[i-1][num-1]%1e9)
        else:
            count[i][num] = int((count[i-1][num-1] + count[i-1][num+1])%1e9)

print(int(sum(count[n-1])%1e9))