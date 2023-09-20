from math import sqrt, ceil

n = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    is_prime = False
    for i in range(2, ceil(sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    if is_prime or num == 2:
        count += 1

print(count)