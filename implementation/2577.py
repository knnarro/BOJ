a = int(input())
b = int(input())
c = int(input())

counts = [0] * 10
num = str(a * b * c)
for digit in num:
    counts[int(digit)] += 1

for count in counts:
    print(count)