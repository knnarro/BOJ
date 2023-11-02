a, b, c = map(int, input().split())

def get_remainder(base, power, divisor):
    if power == 1:
        return base%divisor
    
    remainder = get_remainder(base, power//2, divisor)
    if power % 2 == 0:
        remainder *= remainder
    else:
        remainder *= (remainder*base%divisor)
    return remainder%divisor

print(get_remainder(a, b, c))