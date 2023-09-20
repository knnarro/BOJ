from math import sqrt, floor

def is_prime(num):
    if num == 1 : return False
    if num in [2, 3]: return True
    is_prime = True
    for i in range(2, floor(sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
    return is_prime

start = int(input())
end = int(input())
prime = []
for num in range(start, end+1):
    if is_prime(num):
        prime.append(num)

if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])