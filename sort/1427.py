import sys
print = sys.stdout.write

numbers = list(input())
numbers.sort(reverse=True)
for number in numbers:
    print(f'{number}')