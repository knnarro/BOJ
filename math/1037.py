from math import lcm

n = int(input())
divisors = list(map(int, input().split()))
divisors.sort()
multiple = divisors[0]

for idx in range(1, len(divisors)):
    multiple = max(multiple, lcm(divisors[idx-1], divisors[idx]))

if multiple in divisors:
    multiple *= divisors[0]

print(multiple)