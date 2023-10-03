import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
a = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

a.sort()
for number in numbers:
    low = 0
    high = len(a)-1
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if number == a[mid]:
            result = 1
            break
        elif number < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print(f'{result}\n')