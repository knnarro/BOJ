a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

is_linear_runtime = (a1 * n0 + a0) <= (c * n0) and a1 <= c
print(1 if is_linear_runtime else 0)