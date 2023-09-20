n, k = map(int, input().split())
factors = [1]
for i in range(2, n+1):
    if n % i == 0:
        factors.append(i)

if len(factors) < k:
    print(0)
else:
    print(factors[k-1])