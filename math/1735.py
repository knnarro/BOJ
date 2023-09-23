from math import gcd, lcm

fractions = []
fractions.append(tuple(map(int, input().split())))
fractions.append(tuple(map(int, input().split())))

denominator = lcm(fractions[0][1], fractions[1][1])
numerator = denominator * (fractions[0][0] / fractions[0][1] + fractions[1][0] / fractions[1][1]) 
gcd = gcd(denominator, int(numerator))

print(f'{int(numerator/gcd)} {int(denominator/gcd)}')