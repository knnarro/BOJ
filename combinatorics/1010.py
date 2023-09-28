from math import factorial
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    result = factorial(m) // factorial(m-n) // factorial(n)
    print(result)