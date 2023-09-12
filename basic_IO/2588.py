a = int(input())
b = int(input())

for digit in str(b)[::-1]:
    digit = int(digit)
    print(a*digit)

print(a*b)