import sys
input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())
numbers = []

def select_num(count):
    if count > m:
        for number in numbers:
            print(f'{number} ')
        print(f'\n')
        return
    
    for i in range(1, n+1):
        if not i in numbers:
            numbers.append(i)
            select_num(count+1)
            numbers.pop()

select_num(1)