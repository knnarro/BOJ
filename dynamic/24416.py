n = int(input())

recursives = [0 for _ in range(n+1)]
recursives[1] = 1
recursives[2] = 1
for i in range(3, n+1):
    recursives[i] = recursives[i-2] + recursives[i-1]

print(f'{recursives[n]} {n-2}')