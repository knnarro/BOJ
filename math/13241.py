def get_gcd(x, y):
    dividend = x
    divisor = y
    while dividend % divisor != 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder
    return divisor

def get_lcm(x, y):
    gcd = get_gcd(x, y)
    lcm = int(x * y / gcd)
    return lcm

a, b = map(int, input().split())
print(get_lcm(a, b))