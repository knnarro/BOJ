digit = 1
n = int(input())

while True:
    if n <= digit: break
    n = n - digit
    digit += 1

numerator = n if digit % 2 == 0 else digit-n+1
denominator = digit-n+1 if digit % 2 == 0 else n

print(f'{numerator}/{denominator}')