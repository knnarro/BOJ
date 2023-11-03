p = [0, 1, 1, 1, 2, 2]
for i in range(6, 101):
    num = p[i-1] + p[i-5]
    p.append(num)

t = int(input())
for _ in range(t):
    n = int(input())
    print(p[n])